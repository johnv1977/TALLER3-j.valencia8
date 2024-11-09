from abc import ABC, abstractmethod


class IAnimal(ABC):
    '''
    Interfaz IAnimal.

    Methods:
        comer (float): Número de kilos que el animal come.
        obtener_kilos_comidos (): float Kilos de alimento recibido por el animal.
    '''

    @abstractmethod
    def comer(self, kilos: float) -> None:
        '''
        Representa el comer del animal.

        Args:
            kilos (float): Número de kilos que el animal come.

        Returns:
            None
        '''
        pass

    @abstractmethod
    def obtener_kilos_comidos(self) -> float:
        '''
        Kilos de alimento recibido por el animal.

        Returns:
            float: Kilos de alimento recibido.
        '''
        pass
