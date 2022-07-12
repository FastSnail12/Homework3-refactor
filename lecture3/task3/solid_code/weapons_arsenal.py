from abc import ABC, abstractmethod


class AbstractWeapons(ABC):
    @abstractmethod
    def attack_weapon(self):
        pass


class Gun(AbstractWeapons):
    def attack_weapon(self):
        print('PIU PIU')


class Lasers(AbstractWeapons):
    def attack_weapon(self):
        print('Wzzzuuuup!')


class MartialArts(AbstractWeapons):
    def attack_weapon(self):
        print('Bump')
