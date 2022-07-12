from abc import ABC, abstractmethod


class AbstractPlace(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def get_antagonist(self):
        pass


class Kostroma(AbstractPlace):
    name = 'Kostroma'

    def get_antagonist(self):
        print('Orcs hid in the forest')


class Tokyo(AbstractPlace):
    name = 'Tokyo'

    def get_antagonist(self):
        print('Godzilla stands near a skyscraper')


class Jupiter(AbstractPlace):
    coordinates = [3.5, 8.0]

    @property
    def name(self):
        value = f"'{self.coordinates[0]}"
        for coordinate in range(1, len(self.coordinates)):
            value += f', {self.coordinates[coordinate]}'
        return value + "'"

    def get_antagonist(self):
        print('The asteroid is flying towards the Earth')
