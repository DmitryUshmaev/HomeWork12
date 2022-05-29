from flask import Blueprint, render_template, request, send_from_directory, abort, current_app
from main.main import DATABASE
import os
import logging

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder="templates")

logger_mine = logging.getLogger("logger")


@loader_blueprint.route('/post/')
def post_form():
    return render_template("post_form.html")


@loader_blueprint.route("/uploads/<path:path>")
@loader_blueprint.route("/uploads", methods=['POST'])
def upload_page(path=None):
    """
    Вьюшка загрузки нового сообщения, методом POST загрузка, без метода рендер
    :param path: путь загрузки

    """
    if request.method == 'POST':
        picture = request.files.get("picture")
        if not picture:
            logger_mine.error("Попытка загрузки неразрешенного типа файла")
            abort(400)
        elif picture.filename == "":
            logger_mine.info("Попытка загрузки сообщения без файла")
            abort(400)
        elif (
                os.path.splitext(picture.filename)[1].lower()
                not in current_app.config["UPLOAD_EXTENSIONS"]
        ):
            logger_mine.info("Попытка загрузки неразрешенного типа файла")
            abort(400)
        picture.save(f"./static/images/{picture.filename}")
        text = request.values.get("content")
        DATABASE.json_write({"pic": "../static/images/" + picture.filename, "content": text})
        return render_template("post_uploaded.html", added_text=text, added_picture=f"./static/images/{picture.filename}")
    else:
        return send_from_directory("uploads", path)


@loader_blueprint.errorhandler(413)
@loader_blueprint.errorhandler(400)
def file_type_not_allowed(error):
    return (f"<h1><center><font color='red'>Error with picture file</font>"
            f"<br>File size are too big."
            f"<br>Sending message without picture not file_type_not_allowed"
            f"<br>Only JPEG, PNG, GIF are allowed</center></h1><hr>")
