# Куличкова Алина, 10-кoгорта инженер по тестированию QA+, Финальный проект
import sender_stand_request
import data
# Выполнить тест на получения заказа по треку заказа.
# Проверить, что код ответа равен 200.


def test_get_order_by_track():
    new_order_track = sender_stand_request.post_new_order(data.body).json()['track']

# print(new_order_track)
    get_track = sender_stand_request.get_order_by_number(new_order_track)
# print(get_track.status_code)
# print(get_track.json())

    assert get_track.status_code == 200







