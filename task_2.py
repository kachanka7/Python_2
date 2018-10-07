import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'w') as f:
        orders_list = ['orders', ]
        order_info = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
        orders_list.append(order_info)
        json.dump(orders_list, f, indent=4)


write_order_to_json('printer', '1', '6700', 'Ivanov I.I.', '24.09.2017')