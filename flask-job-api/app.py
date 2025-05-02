from flask import Flask
from flask_cors import CORS
from routes import job_routes
from database import init_db

app = Flask(__name__)
CORS(app)

app.register_blueprint(job_routes, url_prefix="/jobs")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
