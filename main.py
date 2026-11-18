# Завдання №2–3. Відповідає за збирання залежностей і передачу їх у RideService (Dependency Injection), а також за демонстрацію підключення нових модулів Завдання 3.

from ride_service.discounts.standard import StandardDiscount
from ride_service.discounts.vip import VipDiscount
from ride_service.models import FareItem, Ride
from ride_service.notifications.email import EmailNotifier
from ride_service.payments.credit_card import CreditCardPayment
from ride_service.payments.crypto import CryptoPayment
from ride_service.repositories.mysql import MySQLRideRepository
from ride_service.ride_service import RideService

# Завдання 3: нові модулі
from ride_service.discounts.corporate import CorporateDiscount
from ride_service.notifications.sms import SmsNotifier
from ride_service.payments.paypal import PayPalPayment

def make_ride(ride_id: str, passenger_type: str) -> Ride:
    return Ride(
        id=ride_id,
        passenger_type=passenger_type,
        fare_items=[FareItem("Base fare", 50.0), FareItem("Distance 12 km", 150.0)],
        passenger_email="passenger@example.com",
        driver_email="driver@example.com",
        passenger_phone="+380501112233",
        driver_phone="+380674445566",
    )


def main() -> None:
    discounts = {"VIP": VipDiscount(), "Standard": StandardDiscount()}

    print("--- До розширення: VIP / CreditCard / Email ---")
    service = RideService(
        discounts=discounts,
        payment=CreditCardPayment(),
        repository=MySQLRideRepository(),
        notifier=EmailNotifier(),
    )
    service.process_ride(make_ride("R-1", "VIP"))

    print("\n--- Після розширення: Corporate / PayPal / SMS ---")
    extended_service = RideService(
        discounts={**discounts, "Corporate": CorporateDiscount()},
        payment=PayPalPayment(),
        repository=MySQLRideRepository(),
        notifier=SmsNotifier(),
    )
    extended_service.process_ride(make_ride("R-2", "Corporate"))

    print("\n--- Незареєстрований клієнт: Crypto / Email ---")
    extended_service = RideService(
        discounts={**discounts, "Corporate": CorporateDiscount()},
        payment=CryptoPayment(),
        repository=MySQLRideRepository(),
        notifier=EmailNotifier(),
    )
    extended_service.process_ride(make_ride("R-3", "Unknown"))


if __name__ == "__main__":
    main()
