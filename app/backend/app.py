from flask import Flask, jsonify, request
import os
import pymysql
import boto3
import json
from datetime import datetime

app = Flask(__name__)

s3 = boto3.client("s3")

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
S3_BUCKET = os.getenv("S3_BUCKET")


def get_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        connect_timeout=5
    )


def create_table_if_not_exists():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                email VARCHAR(150),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
    conn.close()


@app.route("/")
def home():
    return jsonify({
        "service": "backend",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthyy"
    })


@app.route("/db")
def db():
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
        conn.close()

        return jsonify({
            "database": "connected",
            "query_result": result[0]
        })

    except Exception as e:
        return jsonify({
            "database": "connection_failed",
            "error": str(e)
        }), 500


@app.route("/register", methods=["POST"])
def register():
    try:
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")

        conn = pymysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            connect_timeout=5
        )

        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100),
                    email VARCHAR(150),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            cursor.execute(
                "INSERT INTO users (name, email) VALUES (%s, %s)",
                (name, email)
            )
            conn.commit()
            user_id = cursor.lastrowid

        conn.close()

        s3 = boto3.client("s3")
        file_key = f"registrations/user-{user_id}.json"

        s3.put_object(
            Bucket=os.getenv("S3_BUCKET"),
            Key=file_key,
            Body=json.dumps({
                "event": "user_registered",
                "user_id": user_id,
                "name": name,
                "email": email,
                "time": datetime.utcnow().isoformat()
            }),
            ContentType="application/json"
        )

        return jsonify({
            "status": "success",
            "message": "User saved to RDS and event sent to S3",
            "user_id": user_id,
            "s3_file": file_key
        })

    except Exception as e:
        return jsonify({
            "status": "failed",
            "error": str(e)
        }), 500


@app.route("/users")
def users():
    try:
        create_table_if_not_exists()

        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, name, email, created_at FROM users")
            rows = cursor.fetchall()
        conn.close()

        users_list = []
        for row in rows:
            users_list.append({
                "id": row[0],
                "name": row[1],
                "email": row[2],
                "created_at": str(row[3])
            })

        return jsonify(users_list)

    except Exception as e:
        return jsonify({
            "status": "failed",
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)