import connexion

from swagger_server.models.article import Article  # noqa: E501
from swagger_server.models.body import Body  # noqa: E501
from swagger_server import config
import sqlite3


def dict_factory(cursor, row):
    """Для удобного вывода словаря из базы"""
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def add_article(body):  # noqa: E501
    """Создать новую статью

     # noqa: E501

    :param body: Нужно отправить текст статьи и логин пользователя который её написал
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501

        conn = sqlite3.connect(config.database)
        conn.row_factory = dict_factory
        cursor = conn.cursor()

        # получаем данные для модели ордера
        author = body.author
        text = body.text

        # регистрируем ордер в базе данных
        cursor.execute(f"""INSERT INTO article('text','user_id')
                          VALUES ('{text}', '{author}')
                          """)

        cursor.execute(f"""SELECT * FROM article WHERE id = (SELECT MAX(id) FROM article)
                          """)

        article = cursor.fetchone()

        conn.commit()  # сохраняем изменения

    return article


def get_article(id):  # noqa: E501
    """Получить статью

    По id статьи можно получить более подробную информацию о ней # noqa: E501

    :param id: Уникальный id статьи
    :type id: int

    :rtype: Article
    """
    return 'do some magic!'
