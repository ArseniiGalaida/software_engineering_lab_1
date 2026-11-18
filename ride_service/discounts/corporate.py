# Завдання №3. Відповідає за знижку 30% для Corporate-пасажирів (новий клас, наявний код не змінювався).

from .base import DiscountStrategy


class CorporateDiscount(DiscountStrategy):
    def apply(self, amount: float) -> float:
        return amount * (1 - 0.3)
