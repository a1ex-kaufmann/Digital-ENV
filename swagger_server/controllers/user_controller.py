import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def get_user(login):  # noqa: E501
    """Получить данные о пользователе

    По логину можно получить более подробную информацию о нем # noqa: E501

    :param login: Уникальный логин пользователя
    :type login: str

    :rtype: User
    """
    return 'do some magic!'
