from flask import Blueprint, request, jsonify
from flask_cors import CORS
from models import Job
from database import SessionLocal

job_routes = Blueprint("job_routes", __name__)
CORS(job_routes)

@job_routes.route("/", methods=["GET"])
def get_jobs():
    db = SessionLocal()
    try:
        jobs = db.query(Job).all()
        return jsonify([
            {k: v for k, v in job.__dict__.items() if k != '_sa_instance_state'}
            for job in jobs
        ])
    finally:
        db.close()

@job_routes.route("/", methods=["POST"])
def add_job():
    data = request.get_json()
    db = SessionLocal()
    try:
        new_job = Job(
            title=data.get("title"),
            company=data.get("company"),
            location=data.get("location")
        )
        db.add(new_job)
        db.commit()
        return jsonify({"message": "Job added"}), 201
    finally:
        db.close()

@job_routes.route("/<int:id>", methods=["DELETE"])
def delete_job(id):
    db = SessionLocal()
    try:
        job = db.query(Job).get(id)
        if job:
            db.delete(job)
            db.commit()
            return jsonify({"message": "Job deleted"})
        return jsonify({"message": "Job not found"}), 404
    finally:
        db.close()
