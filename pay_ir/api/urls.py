"""
    This module contains url address for pay.ir endpoints.
"""

# Endpoint for sending requests to get a transaction id.
API_URL_SEND = 'https://pay.ir/payment/send'
# Bank payment page in which user enters his/her card information for payment.
API_URL_PAYMENT_GATEWAY = 'https://pay.ir/payment/gateway/{trans_id}'
# Verification and committing transactions endpoint.
API_URL_VERIFY = 'https://pay.ir/payment/verify'
