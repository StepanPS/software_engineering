from ind.classes import TomatoBush, Gardener

if __name__ == '__main__':
    bush = TomatoBush(10)
    gardener = Gardener("Пётр", bush)
    for _ in range(4):
        gardener.harvest()
        gardener.work()
