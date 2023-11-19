import requests
import config
import data


# Выполнить запрос на создание заказа.
def post_new_order(body):
    return requests.post(config.URL_SCOOTER + config.CREATING_AN_ORDER,
                         json=body)


# Выполнить запрос на получения заказа по треку заказа.

def get_order_by_number(order):

    return requests.get(config.URL_SCOOTER + config.ORDER_BY_NUMBER + "?t=" + str(order))


