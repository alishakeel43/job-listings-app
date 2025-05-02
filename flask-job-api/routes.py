from flask import Blueprint, request, jsonify
from models import Job
from database import session

job_routes = Blueprint("job_routes", __name__)

@job_routes.route("/", methods=["GET"])
def get_jobs():
    jobs = session.query(Job).all()
    return jsonify([
        {k: v for k, v in job.__dict__.items() if k != '_sa_instance_state'}
        for job in jobs
    ])

@job_routes.route("/", methods=["POST"])
def add_job():
    data = request.get_json()
    new_job = Job(
        title=data.get("title"),
        company=data.get("company"),
        location=data.get("location")
    )
    session.add(new_job)
    session.commit()
    return jsonify({"message": "Job added"}), 201

@job_routes.route("/<int:id>", methods=["DELETE"])
def delete_job(id):
    job = session.query(Job).get(id)
    if job:
        session.delete(job)
        session.commit()
        return jsonify({"message": "Job deleted"})
    return jsonify({"message": "Job not found"}), 404
