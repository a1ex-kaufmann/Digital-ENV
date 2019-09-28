# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.article import Article  # noqa: E501
from swagger_server.models.body import Body  # noqa: E501
from swagger_server.test import BaseTestCase


class TestArticleController(BaseTestCase):
    """ArticleController integration test stubs"""

    def test_add_article(self):
        """Test case for add_article

        Создать новую статью
        """
        body = Body()
        response = self.client.open(
            '/v2/article',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_article(self):
        """Test case for get_article

        Получить статью
        """
        response = self.client.open(
            '/v2/article/{id}'.format(id=789),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
