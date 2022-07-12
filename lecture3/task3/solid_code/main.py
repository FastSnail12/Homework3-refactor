from heroes import Superman, ChuckNorris
from places import Kostroma, Tokyo, Jupiter
from alerts import Newspapers


def save_the_place(hero, place, alerts):
    place.get_antagonist()
    hero.attack()
    alerts.create_news(hero.name, place.name)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma(), Newspapers())
    print('-' * 20)
    save_the_place(ChuckNorris(), Tokyo(), Newspapers())
    print('-' * 20)
    save_the_place(ChuckNorris(), Jupiter(), Newspapers())
