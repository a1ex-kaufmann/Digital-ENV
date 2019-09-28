import connexion
import six

from swagger_server.models.body1 import Body1  # noqa: E501
from swagger_server import util


def add_party(body):  # noqa: E501
    """Добавить заявку на участие в мероприятие

     # noqa: E501

    :param body: Подать заявку на участие в мероприятиях от добровольцев России
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body1.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
