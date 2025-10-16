import datetime
from decimal import Decimal

goods = {
    'Пельмени Универсальные': [
        # Первая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('0.5'), 'expiration_date': datetime.date(2023, 7, 15)},
        # Вторая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)},
    ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ],
}

def date_convert(expiration_date):
    expiration_date = expiration_date.split('-')
    return datetime.date(int(expiration_date[0]), int(expiration_date[1]), int(expiration_date[2]))



def add(items, title, amount, expiration_date=None):
    if title not in items:
        items[title] = [{'ammount': Decimal(amount), 'expiration_date': date_convert(expiration_date)}]


print(goods)
print()
add(goods, 'Cheese', '4', '2025-10-23')
print()
print(goods)