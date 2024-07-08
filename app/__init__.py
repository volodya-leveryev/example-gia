from flask import Flask
from flask_migrate import Migrate

from app import admin, models, views


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'

    admin.admin.init_app(app)
    models.db.init_app(app)
    Migrate(app, models.db, render_as_batch=True)

    app.add_url_rule('/', 'index_page', view_func=views.index_page)
    app.add_url_rule('/p/<int:product_id>', 'product_page', view_func=views.product_page)

    return app
