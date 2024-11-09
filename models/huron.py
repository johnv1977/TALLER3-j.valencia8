from models.animal_exotico import Animal_Exotico


class Huron(Animal_Exotico):
    '''
    Representa un Huron.
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
        super().__init__(nombre, edad, peso, pais_origen, impuestos)

    # methods - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def hacer_sonido(self) -> str:
        return '¡Eek Eek!'
