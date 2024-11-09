from models.boa_constrictor import Boa_Constrictor
from models.huron import Huron


class Guarderia:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.__boas = []
        self.__hurones = []

    def agregar_boa(self, boa: Boa_Constrictor) -> None:
        if isinstance(boa, Boa_Constrictor):
            self.__boas.append(boa)
        elif len(self.__boas) == 2:
            raise ValueError('Ya hay 2 boas en la guarderia.')
        else:
            raise TypeError('El boa debe ser un boa constrictor.')

    def agregar_huron(self, huron: Huron) -> None:
        if isinstance(huron, Huron):
            self.__hurones.append(huron)
        elif len(self.__hurones) == 2:
            raise ValueError('Ya hay 2 hurones en la guarderia.')
        else:
            raise TypeError('El huron debe ser un huron.')

    def alimentar_boa(self, boa: Boa_Constrictor) -> None:
        if not isinstance(boa, Boa_Constrictor):
            return 'Esta Boa no existe!'
        else:
            try:
                boa.comer_raton()
                return 'Éxito'
            except Exception:
                return 'La boa está llena.'

    @property
    def boas(self) -> list[Boa_Constrictor]:
        return self.__boas

    @property
    def hurones(self) -> list[Huron]:
        return self.__hurones

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str) -> None:
        if isinstance(value, str):
            self._nombre = value
        else:
            raise TypeError('El nombre debe ser una cadena de caracteres.')
