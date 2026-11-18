# Завдання №3. Відповідає за SMS-сповіщення водія та пасажира замість Email (новий клас, наявний код не змінювався).

from ..models import Ride
from .base import Notifier


class SmsNotifier(Notifier):
    def notify(self, ride: Ride) -> None:
        print(f"Sending SMS to {ride.driver_phone}: Ride {ride.id} is confirmed.")
        print(f"Sending SMS to {ride.passenger_phone}: Your ride is processed.")
