# Завдання №3. Відповідає за оплату через PayPal (новий клас, наявний код не змінювався).

from .base import PaymentProcessor


class PayPalPayment(PaymentProcessor):
    def pay(self, amount: float) -> None:
        print(f"Processing PayPal payment for {amount}")
        # PayPal API call...
