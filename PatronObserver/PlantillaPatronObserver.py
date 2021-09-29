"""
Define a one-to-many dependency between objects so that when one object
changes state, all its dependents are notified and updatedautomatically.
"""

import abc

class Subject(metaclass=abc.ABCMeta):
    """
    Know its observers. Any number of Observer objects may observe a
    subject.
    Send a notification to its observers when its state changes.
    """

    def __init__(self):
        self._observers = set() # lista de observadores
        self._subject_state = None 
    # agregar observadores
    def attach(self, observer):
        pass
    # eliminar observadores
    def detach(self, observer):
        pass
    # notifica a todos los observadores de la lista que hubo un cambio en state
    def _notify(self):
        pass

    # getter and setter 
    @property
    @abc.abstractmethod
    def subject_state(self):
        return self._subject_state

    # cambia state y notifica a sus observadores 
    @subject_state.setter
    @abc.abstractmethod
    def subject_state(self, arg):
        self._subject_state = arg
        self._notify()


class ConcreteSubject(Subject):
    """
    Know its observers. Any number of Observer objects may observe a
    subject.
    Send a notification to its observers when its state changes.
    """

    def __init__(self):
        print("Creando sujeto...")
        self._observers = set() # lista de observadores
        self._subject_state = None 
    # agregar observadores
    def attach(self, observer):
        print("Agregando observador...")
        # le adjunta al objeto observer la referencia a si mismo
        observer._subject = self
        # lo agrega a la lista
        self._observers.add(observer)
    # eliminar observadores
    def detach(self, observer):
        print("Eliminando observador...")
        # le desadjunta al objeto observer la referencia a si mismo
        observer._subject = None
        self._observers.discard(observer)

    # notifica a todos los observadores de la lista que hubo un cambio en state
    def _notify(self):
        print("Notificando a observadores...")
        for observer in self._observers:
            observer.update(self._subject_state)

    # getter and setter 
    @property
    def subject_state(self):
        return self._subject_state
    # cambia state y notifica a sus observadores 
    @subject_state.setter
    def subject_state(self, arg):
        self._subject_state = arg
        self._notify()

# metaclass=abc.ABCMETA: 
# abc — Abstract Base Classes




class Observer(metaclass=abc.ABCMeta):
    """
    Define an updating interface for objects that should be notified of
    changes in a subject.
    """

    def __init__(self):
        self._subject = None
        self._observer_state = None

    @abc.abstractmethod
    def update(self, arg):
        pass


class ConcreteObserver(Observer):
    """
    Implement the Observer updating interface to keep its state
    consistent with the subject's.
    Store state that should stay consistent with the subject's.
    """

    def update(self, arg):
        print("Recibiendo informacion del sujeto...", arg)
        self._observer_state = arg
        # ...


def main():

    subject = ConcreteSubject()
    concrete_observer = ConcreteObserver()
    subject.attach(concrete_observer)
    subject.subject_state = 123


if __name__ == "__main__":
    main()