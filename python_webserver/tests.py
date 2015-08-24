
# from python_webserver import operations
import operations
from cloudify.exceptions import NonRecoverableError
from cloudify.mocks import MockCloudifyContext

import unittest


class TestWebServer(unittest.TestCase):

    def test_http_webserver(self):
        ctx = MockCloudifyContext(
            node_id='id',
            properties={
                'port': 8080
            })
        operations.start(ctx)
#         operations.verify_http_server(8080)
        operations.stop(ctx)
#         self.assertRaises(NonRecoverableError, operations.verify_http_server, 8080)
