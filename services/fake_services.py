from abc import abstractmethod
from models.boa_constrictor import Boa_Constrictor
from models.huron import Huron


class Fake_Service:
    def __init__(self):
        pass

    @abstractmethod
    def get_boas() -> list[Boa_Constrictor]:
        # nombre, edad, peso, pais_origen, impuestos
        return [
            Boa_Constrictor("Anaconda", 2, 5.5, "Brasil", 1500.0),
            Boa_Constrictor("Python", 8, 25.0, "Colombia", 3000.0),
            # Boa_Constrictor("Blanca", 5, 12.0, "Perú", 5000.0),
            # Boa_Constrictor("Rescate", None, 3.0, "Venezuela", 0.0),
            # Boa_Constrictor("Gigante", 10, 30.0, "Ecuador", 4000.0)
        ]

    @abstractmethod
    def get_hurones() -> list[Huron]:
        # nombre, edad, peso, pais_origen, impuestos
        return [
            Huron("Loki", 3, 1.2, "Rusia", 800.0),
            Huron("Luna", 2, 0.9, "Canadá", 1000.0),
            # Huron("Odin", 4, 1.5, "Estados Unidos", 1200)
        ]
