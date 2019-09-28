# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body1 import Body1  # noqa: E501
from swagger_server.test import BaseTestCase


class TestEventController(BaseTestCase):
    """EventController integration test stubs"""

    def test_add_party(self):
        """Test case for add_party

        Добавить заявку на участие в мероприятие
        """
        body = Body1()
        response = self.client.open(
            '/v2/event',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
