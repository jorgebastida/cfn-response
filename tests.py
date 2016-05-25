import sys
import unittest
from functools import partial

try:
    from urllib2 import HTTPError
except ImportError:
    from urllib.error import HTTPError

try:
    from mock import patch, Mock, call
except ImportError:
    from unittest.mock import patch, Mock, call

from cfnresponse import send

if sys.version_info >= (3, 0):
    open_director_patch = partial(patch, 'urllib.request.OpenerDirector.open')
else:
    open_director_patch = partial(patch, 'urllib2.OpenerDirector.open')


class TestCfnResponse(unittest.TestCase):

    def _event(self):
        return {
            'StackId': 'stack_id',
            'RequestId': 'request_id',
            'LogicalResourceId': 'logical_resource_id',
            'ResponseURL': 'http://localhost/response'
        }

    def _context(self):
        return Mock(log_stream_name='log_stream_name')

    @open_director_patch()
    def test_cfn_send_success(self, open_mock):
        open_mock.return_value = Mock()
        open_mock.return_value.msg = 'OK'
        open_mock.return_value.getcode.return_value = 200
        response = send(
            event=self._event(),
            context=Mock(log_stream_name='log_stream_name'),
            response_status='response_status',
            response_data='response_data',
        )
        self.assertTrue(response)

    @open_director_patch()
    def test_cfn_send_error(self, open_mock):

        class MockHTTPError(HTTPError):
            def __init__(self, code=503):
                self.code = code

        open_mock.side_effect = MockHTTPError
        response = send(
            event=self._event(),
            context=Mock(log_stream_name='log_stream_name'),
            response_status='response_status',
            response_data='response_data',
        )
        self.assertFalse(response)
