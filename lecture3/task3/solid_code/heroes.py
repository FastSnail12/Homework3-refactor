from abc import ABC, abstractmethod
from weapons_arsenal import Lasers, Gun


class AbstractOrdinaryHero(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def attack(self):
        pass


class AbstractSuperHero(AbstractOrdinaryHero):
    @abstractmethod
    def ultimate(self):
        pass


class Superman(AbstractSuperHero, Lasers):
    name = 'Clark Kent'

    def attack(self):
        self.ultimate()

    def ultimate(self):
        self.attack_weapon()


class ChuckNorris(AbstractOrdinaryHero, Gun):
    name = 'Chuck Norris'

    def attack(self):
        self.attack_weapon()
