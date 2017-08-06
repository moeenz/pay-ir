"""
    This module contains pay.ir API client.
"""

import requests

from pay_ir.utils.reqres import get_json
from pay_ir.api.helpers import init_has_exceptions, verify_has_exceptions
from pay_ir.api.urls import API_URL_SEND, API_URL_PAYMENT_GATEWAY, API_URL_VERIFY


class PayIrClient:
    """
        Requesting client for pay.ir payment APIs. This will perform
            gateway methods and return their response. Supported APIs are:

            - send: Initializes a transaction by generating a transId.
            - verify: Verifies a performed payment and If successful,
                returning it's amount.
    """


    def __init__(self, api_key):
        self.api_key = api_key


    def init_transaction(self, amount, redirect_url, factor_number=None):
        """
            Sends an initial request to 'API_URL_SEND' to retrieve a
                transaction id. Sent data contains these variables:

                    - api (string): You API key for pay.ir
                    - amount (integer): Transaction amount in rials, should be greater than 1000.
                    - redirect (string): Urlencoded return address registered in pay.ir panel.
                    - factorNumber (string): (optional).

            Returns:
                A dictionary on success with format of:
                ```
                {
                    "trans_id": <transaction_id>,
                    "payment_url": Redirect url to bank payment page.
                }
                ```

            Raises:
                One of exceptions.payment according to the returned status code.
        """

        if amount < 1000:
            raise ValueError('amount value should not be less than 1000.')
        if not isinstance(amount, int):
            raise TypeError('amount should be of int type.')

        if not isinstance(redirect_url, str):
            raise TypeError('redirect_url should be of str type.')

        if factor_number and not isinstance(factor_number, str):
            raise TypeError('factor_number should be of str type.')

        init_data = {
            'api': self.api_key,
            'amount': amount,
            'redirect': redirect_url,
            'factorNumber': factor_number if factor_number is not None else ''
        }

        response = get_json(requests.post(API_URL_SEND, data=init_data))
        if not init_has_exceptions(response['status']):
            return {
                'trans_id': response['transId'],
                'payment_url': API_URL_PAYMENT_GATEWAY.format(trans_id=response['transId'])
            }


    def verify_transaction(self, trans_id):
        """
            If you had e succesful payment after redirecting
                to payment page (having a status code of 1) you
                can call this method to verify the payment.

            Returns:
                Amount of transaction if it was successful.

            Raises:
                One of exceptions.verification according to the returned status code.
        """

        if not isinstance(trans_id, int):
            raise TypeError('trans_id should be of int type.')

        verify_data = {
            'api': self.api_key,
            'transId': trans_id
        }

        response = get_json(requests.post(API_URL_VERIFY, data=verify_data))
        if not verify_has_exceptions(response['status']):
            return response['amount']
