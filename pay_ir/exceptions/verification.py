"""
    This module contains exceptions specific to verify API.
"""

from pay_ir.exceptions.base import BasePayIrException


class TransIdNotFoundException(BasePayIrException):
    """
        Happens if provided transaction id was not found.
    """

    def __init__(self):
        EXP_MESSAGE = 'Provided transaction id was not found.'
        super(TransIdNotFoundException, self).__init__(EXP_MESSAGE)
