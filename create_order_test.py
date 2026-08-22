import sender_stand_request


def test_create_order_and_get_by_track():
    # Создаём заказ
    response = sender_stand_request.create_order()

    # Сохраняем трек созданного заказа
    track = response.json()["track"]

    # Получаем заказ по треку
    order_response = sender_stand_request.get_order_by_track(track)

    # Проверяем код ответа
    assert order_response.status_code == 200