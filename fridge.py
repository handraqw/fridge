import datetime
from decimal import Decimal

goods = {
    'Пельмени Универсальные': [
        # Первая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('0.5'), 'expiration_date': datetime.date(2025, 10, 15)},
        # Вторая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2025, 11, 1)},
    ],

    'Молоко': [
        {'amount': Decimal('3'), 'expiration_date': datetime.date(2025, 11, 3)}
    ],

    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ],
}


def add(items, title, amount, expiration_date=None):
    ...


def add_by_note(items, note):
    ...


def find(items, needle):
    ...


def amount(items, needle):
    ...