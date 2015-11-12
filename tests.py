import unittest
import urllib2

try:
    from mock import patch, Mock, call
except ImportError:
    from unittest.mock import patch, Mock, call

from cfnresponse import send

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

    @patch('urllib2.OpenerDirector.open')
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

    @patch('urllib2.OpenerDirector.open')
    def test_cfn_send_error(self, open_mock):

        class MockHTTPError(urllib2.HTTPError):
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
