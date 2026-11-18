# Завдання №2. Відповідає за Email-сповіщення водія та пасажира.

from ..models import Ride
from .base import Notifier


class EmailNotifier(Notifier):
    def notify(self, ride: Ride) -> None:
        print(f"Sending Email to {ride.driver_email}: Ride {ride.id} is confirmed.")
        print(f"Sending Email to {ride.passenger_email}: Your ride is processed.")
