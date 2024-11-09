import unittest
from models.boa_constrictor import Boa_Constrictor


class TestBoaConstrictor(unittest.TestCase):
    def test_hacer_sonido(self):
        boa = Boa_Constrictor('Anaconda', 2, 5.5, 'Brasil', 1500.0)
        self.assertEqual(boa.hacer_sonido(), '¡Tsss!')

    def test_calcular_flete(self):
        boa = Boa_Constrictor('Anaconda', 2, 5.5, 'Brasil', 1500.0)
        self.assertEqual(boa.calcular_flete(), 8250.0)

    def test_comer(self):
        boa = Boa_Constrictor('Anaconda', 2, 5.5, 'Brasil', 1500.0)
        self.assertRaises(TypeError, boa.comer, 1)
        self.assertRaises(ValueError, boa.comer, -1.0)
        boa.comer(5.0)
        self.assertEqual(boa.obtener_kilos_comidos(), 5)
        boa.comer(5.0)
        self.assertEqual(boa.obtener_kilos_comidos(), 10)

    def test_ratones_consumidos(self):
        boa = Boa_Constrictor('Anaconda', 2, 5.5, 'Brasil', 1500.0)
        self.assertEqual(boa.ratones_consumidos(), 0)
        boa.comer_raton()
        self.assertEqual(boa.ratones_consumidos(), 1)
        boa.comer_raton()
        self.assertEqual(boa.ratones_consumidos(), 2)


if __name__ == '__main__':
    unittest.main()
