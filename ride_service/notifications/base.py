# Завдання №2. Відповідає за інтерфейс сповіщень (Notifier).

from abc import ABC, abstractmethod

from ..models import Ride


class Notifier(ABC):
    @abstractmethod
    def notify(self, ride: Ride) -> None: ...
