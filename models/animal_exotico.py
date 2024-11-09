from abc import abstractmethod
from models.animal import Animal


class Animal_Exotico(Animal):
    '''
    Representa a un animal exótico.

    Args:
        nombre (str): Nombre del animal.
        edad (int): Edad del animal en años.
        peso (float): Peso del animal en kilogramos.
        pais_origen (str): País de origen del animal.
        impuestos (float): Impuestos de importación del animal.

    Methods:
        calcular_flete (): float Valor a pagar por el flete. Impuestos por peso del animal.
        comer (float): Número de kilos que el animal come.
        dar_informacion (): str Cadena de texto con información básica sobre el animal.
        hacer_sonido (): str String que representa en sonido.
        obtener_kilos_comidos (): float Kilos de alimento recibido por el animal.
    '''

    def __init__(self, nombre: str, edad: int, peso: float, pais_origen: str, impuestos: float):
        super().__init__(nombre, edad, peso)
        self.pais_origen = pais_origen
        self.impuestos = impuestos

    # abstract methods - - - - - - - - - - - - - - - - - - - - - -
    @abstractmethod
    def hacer_sonido(self) -> str:
        pass

    # methods - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def calcular_flete(self) -> float:
        '''
        Valor del flete a pagar por el traslado desde el país de origen.

        Returns:
            float: Impuestos * peso del animal.
        '''
        return float(self._impuestos * self._peso)

    # attributes - - - - - - - - - - - - - - - - - - - - - - - - -
    @property
    def pais_origen(self) -> str:
        return self._pais_origen

    @pais_origen.setter
    def pais_origen(self, value: str) -> None:
        if isinstance(value, str):
            self._pais_origen = value
        else:
            raise TypeError('El pais origen debe ser una cadena de caracteres.')

    @property
    def impuestos(self) -> float:
        return self._impuestos

    @impuestos.setter
    def impuestos(self, value: float) -> None:
        if isinstance(value, float):
            self._impuestos = value
        else:
            raise TypeError('Los impuestos deben ser un número flotante.')
