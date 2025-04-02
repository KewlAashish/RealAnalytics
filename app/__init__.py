import os
import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load PostgreSQL connection from environment variable
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database with app context
    db.init_app(app)

    # Import and register the routes
    from .routes import main  
    app.register_blueprint(main)

    # Import models so they are registered
    with app.app_context():
        from . import models

        # Retry DB connection for up to 10 seconds
        for i in range(10):
            try:
                db.create_all()
                print("✅ Database connection and table creation successful.")
                break
            except OperationalError:
                print(f"🔁 DB connection failed (attempt {i+1}/10). Retrying...")
                time.sleep(1)
        else:
            raise Exception("❌ Database connection failed after 10 retries.")

    return app
