from flask import Blueprint

index_blueprint = Blueprint('index_view', __name__, template_folder='templates')

def add_blueprints(app):
	app.register_blueprint(index_blueprint)
