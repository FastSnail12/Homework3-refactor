from abc import ABC, abstractmethod


class AbstractAlert(ABC):
    @abstractmethod
    def create_news(self, name_hero, place):
        pass


class Newspapers(AbstractAlert):
    def create_news(self, name_hero, place_name):
        print(f'The newspapers write: {name_hero} saved the {place_name}!')
