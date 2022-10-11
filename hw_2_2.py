"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.
"""

import json


def write_order_to_json(item: str, quantity: str, price: str, buyer: str, date: str) -> None:
    """
    Writing function arguments to json file (in dictionary format)
    :param item: good
    :param quantity: quantity
    :param price: price
    :param buyer: buyer
    :param date: date in string format
    :return None: result - writing to a json file
    """

    with open('orders.json', 'r', encoding='utf-8') as f_out:
        data = json.load(f_out)

    with open('orders.json', 'w', encoding='utf-8', ) as f_in:
        orders_list = data['orders']
        order_info = {'item': item, 'quantity': quantity,
                      'price': price, 'buyer': buyer, 'date': date}
        orders_list.append(order_info)
        # используем параметр ensure_ascii=False
        # Если ensure_ascii = True, все не-ASCII символы в выводе будут экранированы
        # последовательностями \uXXXX, и результатом будет строка, содержащая только ASCII символы.
        # Если ensure_ascii = False, строки запишутся как есть.
        json.dump(data, f_in, indent=4, ensure_ascii=False)


# initialisation (чтобы не удалять данные при каждой новой проверке скрипта)
# with open('orders_2.json', 'w', encoding='utf-8') as f_in:
#     json.dump({'orders': []}, f_in, indent=4)


write_order_to_json('принтер', '10', '6700', 'Иванов И.И.', '24.09.2017')
write_order_to_json('сканер', '20', '10000', 'Петров П.П.', '11.01.2018')
write_order_to_json('компьютер', '5', '40000', 'Сидоров С.С.', '2.05.2019')
