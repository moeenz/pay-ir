"""
    This module contains test cases for API endpoints.
"""

import unittest

from pay_ir.api.client import PayIrClient


class PayIrAPITestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)


    def setUp(self):
        self.client = PayIrClient('test')


    def test_send_api_correct_data(self):
        response = self.client.init_transaction(1000, 'http://localhost')
        trans_id = int(response['trans_id'])
        self.assertIsInstance(trans_id, int)
        self.assertGreater(trans_id, 0)
        self.assertIsInstance(response['payment_url'], str)
