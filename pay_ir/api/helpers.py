"""
    This module contains helper functions to perform on
        API requests/response content.
"""

from pay_ir.exceptions.base import ApiKeyNotFoundException,\
    PaymentGatewayNotFoundException, SellerNotActiveException, TransactionFailedException

from pay_ir.exceptions.payment import AmountNotFoundException,\
    AmountNotIntegerException, AmountNotCorrect, RedirectUrlNotFoundException,\
    RedirectUrlsNotMatchingException

from pay_ir.exceptions.verification import TransIdNotFoundException


# Success code received from API server.
SUCCESS_CODE = 1

# Dictionary of all possible error codes in send API
#   and their corresponding exception.
INIT_RESPONSE_MAPPER = {
    '-1': ApiKeyNotFoundException,
    '-2': AmountNotFoundException,
    '-3': AmountNotIntegerException,
    '-4': AmountNotCorrect,
    '-5': RedirectUrlNotFoundException,
    '-6': PaymentGatewayNotFoundException,
    '-7': SellerNotActiveException,
    '-8': RedirectUrlsNotMatchingException,
    'failed': TransactionFailedException
}

# Dictionary of all possbile error codes in verify API
#   and their corresponding exception.
VERIFY_RESPONSE_MAPPER = {
    '-1': ApiKeyNotFoundException,
    '-2': TransIdNotFoundException,
    '-3': PaymentGatewayNotFoundException,
    '-4': SellerNotActiveException,
    '-5': TransactionFailedException
}


def init_has_exceptions(status):
    """
        Raises proper exception according to 'send' API response.
            If all well then it will return False.
    """

    if int(status) == SUCCESS_CODE:
        return False
    else:
        raise INIT_RESPONSE_MAPPER[status]()


def verify_has_exceptions(status):
    """
        Raises proper exception according to 'verify' API response.
            If all well then it will return False.
    """

    if int(status) == SUCCESS_CODE:
        return False
    else:
        raise VERIFY_RESPONSE_MAPPER['errorCode']()
