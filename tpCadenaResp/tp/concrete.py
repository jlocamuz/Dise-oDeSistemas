from interface import AbstractHandler, Handler


class Executive(AbstractHandler):

    def handle(self, monto):
        if monto <= 1000:
            self._approved = True
            return 'Crédito aprobado por el ejecutivo'
        else:
            return super().handle(monto)
    

class Leader(AbstractHandler):

    def handle(self, monto):
        if 10000 < monto <= 50000:
            self._approved = True
            return 'Crédito aprobado por el lider'
        else:
            return super().handle(monto)
    

class Manager(AbstractHandler):

    def handle(self, monto):
        if 50000 < monto <= 100000:
            self._approved = True
            return 'Crédito aprobado por el manager'
        else:
            return super().handle(monto)


class Director(AbstractHandler):

    def handle(self, monto):
        if monto > 100000:
            self._approved = True
            return 'Crédito aprobado por el Director'
        else:
            return super().handle(monto)
    
def main(handler: Handler):
    monto = 400
    who_approves = handler.handle(monto)
    if who_approves:
        print(f'{who_approves}')
    