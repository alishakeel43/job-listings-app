from flask import Flask
from flask_cors import CORS
from routes import job_routes
from database import Base, engine

app = Flask(__name__)
CORS(app)

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Register blueprints
app.register_blueprint(job_routes, url_prefix="/jobs")

@app.route("/")
def index():
    return "Welcome to the Job API (MySQL)!"

if __name__ == "__main__":
    app.run(debug=True)
