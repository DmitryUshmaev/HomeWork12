from flask import Blueprint, render_template, request
from functions import DataBase

main_blueprint = Blueprint('index_blueprint', __name__, template_folder="templates")

DATABASE = DataBase()


@main_blueprint.route('/')
def index_page():
    """
    Вьюшка для отображения главной страницы поиска. Обновляем базу данных на предмет новых записей
    :return:
    """
    DATABASE.database_loader()
    return render_template('index.html')


@main_blueprint.route("/post_list/")
def post_list_page():
    """
    Вьюшка выводит результат поиска по введеным пользователем данным

    """
    search_request = request.args.get('s')
    if search_request:
        return render_template("post_list.html",
                               posts=DATABASE.search_in_database(search_request),
                               search_request=search_request)
    return render_template("post_list.html")


@main_blueprint.errorhandler(404)
def page_not_found(error):
    return f"<h1><center><font color='red'>Error 404</font><br>Page not found!</center></h1><hr>"


@main_blueprint.errorhandler(400)
def database_not_found(error):
    return (
        f"<h1><center><font color='red'>Error</font>"
        f"<br>Databae not found!</center></h1>"

    )
