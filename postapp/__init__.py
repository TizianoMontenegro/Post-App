import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='developing',
        DATABASE=os.path.join(app.instance_path, 'postapp.sqlite'),
    )

    if test_config == None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed to
        app.config.from_mapping(test_config)
    
    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # A page with some text
    @app.route('/hello')
    def hello():
        return 'hello bro'
    
    # Register with the Application
    from . import db
    db.init_app(app)

    return app
