"""
    This module contains base class for pay.ir exceptions.
"""


class BasePayIrException(BaseException):
    """
        Base exception class for all other pay.ir exceptions occurring.
    """

    def __init__(self, message):
        super(BasePayIrException, self).__init__(message)


class ApiKeyNotFoundException(BasePayIrException):
    """
        Happens if not API key was provided.
    """

    def __init__(self):
        EXP_MESSAGE = 'You should have provided the API key.'
        super(ApiKeyNotFoundException, self).__init__(EXP_MESSAGE)


class PaymentGatewayNotFoundException(BasePayIrException):
    """
        Happens if no payment gateway was registered in pay.ir
    """

    def __init__(self):
        EXP_MESSAGE = 'No payment gateway is registered.'
        super(PaymentGatewayNotFoundException, self).__init__(EXP_MESSAGE)


class SellerNotActiveException(BasePayIrException):
    """
        Happens if target seller is active yet.
    """

    def __init__(self):
        EXP_MESSAGE = 'Seller is not active.'
        super(SellerNotActiveException, self).__init__(EXP_MESSAGE)


class TransactionFailedException(BasePayIrException):
    """
        Happens if transaction failed.
    """

    def __init__(self):
        EXP_MESSAGE = 'Transaction failed.'
        super(TransactionFailedException, self).__init__(EXP_MESSAGE)
