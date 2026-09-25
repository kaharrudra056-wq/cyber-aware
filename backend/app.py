import os
import sys
from flask import Flask
from flask_login import LoginManager

# Path setup
BACKEND_DIR  = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR     = os.path.dirname(BACKEND_DIR)
FRONTEND_DIR = os.path.join(ROOT_DIR, 'frontend')

# Add backend dir to sys.path so imports work
if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(FRONTEND_DIR, 'templates'),
        static_folder=os.path.join(FRONTEND_DIR, 'static')
    )

    from config import Config
    app.config.from_object(Config)

    from models import db
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'
    login_manager.init_app(app)

    from models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    from routes.auth  import auth_bp
    from routes.main  import main_bp
    from routes.quiz  import quiz_bp
    from routes.admin import admin_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(quiz_bp)
    app.register_blueprint(admin_bp)

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
