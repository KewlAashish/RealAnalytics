import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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

    # import models so that they are registered
    with app.app_context():
        from . import models
        db.create_all()
        
    return app