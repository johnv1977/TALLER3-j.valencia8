import unittest
from models.huron import Huron


class TestHuron(unittest.TestCase):
    def test_hacer_sonido(self):
        huron = Huron('Loki', 3, 1.2, 'Rusia', 800.0)
        self.assertEqual(huron.hacer_sonido(), '¡Eek Eek!')

    def test_calcular_flete(self):
        huron = Huron('Loki', 3, 1.2, 'Rusia', 800.0)
        self.assertRaises(TypeError, huron.calcular_flete, 'string')
        self.assertRaises(TypeError, huron.calcular_flete, 3.5)
        self.assertEqual(huron.calcular_flete(), 960)


if __name__ == '__main__':
    unittest.main()
