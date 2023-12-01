    def is_ripe(self) -> bool:
        return self.__stage == len(Tomato.states) - 1


class TomatoBush:
    def __init__(self, count: int):
        self.__tomatoes: list[Tomato, ...] = [Tomato(i) for i in range(count)]

    def grow_all(self) -> None:
        for t in self.__tomatoes:
            t.grow()

    def all_are_ripe(self) -> bool:
        return all([t.is_ripe() for t in self.__tomatoes])

    def give_away_all(self) -> None:
        self.__tomatoes.clear()


class Gardener:
    def __init__(self, name: str, plant: TomatoBush):
        self.name: str = name
        self._plant: TomatoBush = plant

    def work(self) -> None:
        self._plant.grow_all()

    def harvest(self) -> bool:
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Урожай собран")
            return True
        else:
            print("Растение еще не созрело")
            return False

    @staticmethod
    def knowledge_base() -> None:
        print("Справка")
