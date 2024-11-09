from models.animal_exotico import Animal_Exotico


class Boa_Constrictor(Animal_Exotico):
    '''
    Representa una Boa Constrictor.
    Args:
        nombre (str): Nombre del animal.
        edad (int): Edad del animal en años.
        peso (float): Peso del animal en kilogramos.
        pais_origen (str): País de origen del animal.
        impuestos (float): Impuestos de importación del animal.

    Methods:
        calcular_flete (): float Valor a pagar por el flete. Impuestos por peso del animal.
        comer (float): Número de kilos que el animal come.
        comer_raton ():  Método que registra la acción de comer un ratón.
        dar_informacion (): str Cadena de texto con información básica sobre el animal.
        hacer_sonido (): str String que representa en sonido.
        obtener_kilos_comidos (): float Kilos de alimento recibido por el animal.
        ratones_consumidos (): int Número de ratones que la Boa a ha consumido.
    '''

    def __init__(self, nombre: str, edad: int, peso: float, pais_origen: str, impuestos: float):
        super().__init__(nombre, edad, peso, pais_origen, impuestos)
        self.__ratones_consumidos = 0

    # methods - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def hacer_sonido(self) -> str:
        return '¡Tsss!'

    def comer_raton(self) -> None:
        if self.__ratones_consumidos >= 10:
            raise ValueError('Demasiados ratones!')
        self.__ratones_consumidos += 1

    def ratones_consumidos(self) -> int:
        return self.__ratones_consumidos
