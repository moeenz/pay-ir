"""
    This module contains exceptions specific to send API.
"""

from pay_ir.exceptions.base import BasePayIrException


class AmountNotFoundException(BasePayIrException):
    """
        Happens if no amount value was provided.
    """

    def __init__(self):
        EXP_MESSAGE = 'You should have provided the API key.'
        super(AmountNotFoundException, self).__init__(EXP_MESSAGE)


class AmountNotIntegerException(BasePayIrException):
    """
        Happens if not an integer was provided for amount value.
    """

    def __init__(self):
        EXP_MESSAGE = 'You should have provided the API key.'
        super(AmountNotIntegerException, self).__init__(EXP_MESSAGE)


class AmountNotCorrect(BasePayIrException):
    """
        Happens if given amount is below 1000.
    """

    def __init__(self):
        EXP_MESSAGE = 'You should have provided the API key.'
        super(AmountNotCorrect, self).__init__(EXP_MESSAGE)


class RedirectUrlNotFoundException(BasePayIrException):
    """
        Happens if not redirect url was provided.
    """

    def __init__(self):
        EXP_MESSAGE = 'You should have provided the API key.'
        super(RedirectUrlNotFoundException, self).__init__(EXP_MESSAGE)


class RedirectUrlsNotMatchingException(BasePayIrException):
    """
        Happens if redirect url is not registered for the payment gateway.
    """

    def __init__(self):
        EXP_MESSAGE = 'You should have provided the API key.'
        super(RedirectUrlsNotMatchingException, self).__init__(EXP_MESSAGE)
