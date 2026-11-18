# Завдання №2. Відповідає за оркестрацію обробки поїздки: валідацію, знижку, оплату, збереження та сповіщення. Залежить лише від абстракцій.

from collections.abc import Mapping

from .discounts.base import DiscountStrategy
from .models import Ride
from .notifications.base import Notifier
from .payments.base import PaymentProcessor
from .repositories.base import RideRepository


class RideService:
    def __init__(
        self,
        discounts: Mapping[str, DiscountStrategy],
        payment: PaymentProcessor,
        repository: RideRepository,
        notifier: Notifier,
    ) -> None:
        self._discounts = discounts
        self._payment = payment
        self._repository = repository
        self._notifier = notifier

    def process_ride(self, ride: Ride) -> None:
        if not ride.fare_items:
            raise ValueError("Ride has no fare items")

        subtotal = sum(item.price for item in ride.fare_items)
        strategy = self._discounts.get(ride.passenger_type)
        total = strategy.apply(subtotal) if strategy else subtotal

        self._payment.pay(total)
        self._repository.save(ride)
        self._notifier.notify(ride)
