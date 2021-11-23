import concrete


if __name__ == '__main__':

    director = concrete.Director()
    lider = concrete.Leader()
    gerente = concrete.Manager()
    ejecutivo = concrete.Executive()

    director.set_successor(lider).set_successor(gerente).set_successor(ejecutivo)

    obj.main(director)