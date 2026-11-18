# Завдання №2. Відповідає за доменні моделі: поїздку (Ride) та складові тарифу (FareItem).

from dataclasses import dataclass


@dataclass
class FareItem:
    description: str
    price: float


@dataclass
class Ride:
    id: str
    passenger_type: str
    fare_items: list[FareItem]
    passenger_email: str
    driver_email: str
    passenger_phone: str
    driver_phone: str
