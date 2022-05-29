from flask import Flask
from main.main import main_blueprint
from loader.loader import loader_blueprint
import logger_init

def main():
    app = Flask(__name__)
    app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
    app.config['UPLOAD_EXTENSIONS'] = ('.jpg', '.png', ".gif")

    app.register_blueprint(main_blueprint)
    app.register_blueprint(loader_blueprint)

    app.run()


if __name__ == '__main__':
    main()
