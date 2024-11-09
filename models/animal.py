from abc import abstractmethod
from models.ianimal import IAnimal


class Animal(IAnimal):
    '''
    Representa a un animal. Implementa ABC y IAnimal.

    Args:
        nombre (str): Nombre del animal.
        edad (int): Edad del animal en años.
        peso (float): Peso del animal en kilogramos.

    Methods:
        comer (float): Número de kilos que el animal come.
        dar_informacion (): str Cadena de texto con información básica sobre el animal.
        hacer_sonido (): str String que representa en sonido.
        obtener_kilos_comidos (): float Kilos de alimento recibido por el animal.
    '''

    def __init__(self, nombre: str, edad: int, peso: float):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self._kilos_comidos = 0

    @abstractmethod
    def hacer_sonido(self) -> str:
        '''
        Representa el sonido del animal.

        Returns:
            str: String que representa en sonido.
        '''
        pass

    # methods - - - - - - - - - - - - - - - - - - - - - - - -
    def comer(self, kilos: float) -> None:
        #  validar que kilos sea un número flotante positivo
        if not isinstance(kilos, float):
            raise TypeError('Los kilos deben ser un número flotante.')
        elif kilos < 0:
            raise ValueError('Los kilos deben ser un número positivo.')

        self._kilos_comidos += kilos

    def dar_informacion(self) -> str:
        '''
        Genera un texto con información básica sobre el animal.

        Returns:
            str: String con la información del animal (atributo:valor)'.
        '''
        info = f'{self.__class__.__name__} ::'
        atributos = vars(self)
        for atributo, valor in atributos.items():
            info += f' {atributo}: {valor}.'
        return info

    def obtener_kilos_comidos(self) -> float:
        return self._kilos_comidos

    # attributes - - - - - - - - - - - - - - - - - - - - - - -
    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str) -> None:
        if isinstance(value, str):
            self._nombre = value
        else:
            raise TypeError('El nombre debe ser una cadena de caracteres.')

    @property
    def edad(self) -> int:
        return self._edad

    @edad.setter
    def edad(self, value: int) -> None:
        if isinstance(value, int):
            self._edad = value
        else:
            raise TypeError('La edad debe ser un número entero.')

    @property
    def peso(self) -> float:
        return self._peso

    @peso.setter
    def peso(self, value: float) -> None:
        if isinstance(value, float):
            self._peso = value
        else:
            raise TypeError('El peso debe ser un número flotante.')
