from abc import ABC, abstractmethod


class IVehiculoPublico(ABC):
    @abstractmethod
    def pagar_transporte(self):
        ...


class IVehiculoFuel(ABC):
    @abstractmethod
    def rellenar_deposito(self):
        ...


class IVehiculoVolador(ABC):
    @abstractmethod
    def volar(self, velocidad):
        ...


class AvionRyanar(IVehiculoVolador, IVehiculoFuel):
    def __init__(self, deposito: bool):
        self.deposito = "lleno" if deposito else "vacio"

    def rellenar_deposito(self):
        if self.deposito == "vacio":
            return "Hay que rellenar el deposito"
        else:
            return "El deposito esta lleno"

    def volar(self, velocidad):
        return f"Estoy volando a {velocidad} nudos :D"


class TrenRenfe(IVehiculoPublico, IVehiculoFuel):
    def __init__(self, pasajeros, pybons: int):
        self.pasajeros = pasajeros
        self.pybons = "Suficientes" if pybons > 50 % else "No suficientes"

    def pagar_transporte(self):
        return True if self.pybons == "Suficientes" else False

    def rellenar_deposito(self):
        return True if self.pasajeros > 100 else False
