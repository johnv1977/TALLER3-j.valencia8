from services.fake_services import Fake_Service


# Instances
boas = Fake_Service.get_boas()
hurones = Fake_Service.get_hurones()
boa_1 = boas[0]
huron_1 = hurones[0]


class Console_Service():

    @staticmethod
    def info_boas() -> None:
        print('\nInfo Boas::')
        for boa in boas:
            print(f'{boa.dar_informacion()}')

    @staticmethod
    def info_hurones() -> None:
        print('\nInfo Hurones::')
        for huron in hurones:
            print(f'{huron.dar_informacion()}')

    @staticmethod
    def calcular_flete() -> None:
        print('\nCalcular fletes::')

        for boa in boas:
            print(f'Boa: {boa.nombre}, desde {boa.pais_origen} -> Flete ${boa.calcular_flete()}')

        for huron in hurones:
            print(f'Huron: {huron.nombre}, desde {huron.pais_origen} -> Flete ${huron.calcular_flete()}')

    @staticmethod
    def boa_comer() -> None:
        print('\nBoa comer ::')
        print(f'Boa {boa_1.nombre}, kilos comidos: {boa_1.obtener_kilos_comidos()}')
        print('boa.comer(5.5)')
        boa_1.comer(5.5)
        print(f'Boa {boa_1.nombre}, kilos comidos: {boa_1.obtener_kilos_comidos()}')

    @staticmethod
    def boa_comer_raton() -> None:
        print('\nBoa comer_raton ::')
        print(f'Boa {boa_1.nombre}, ratones consumidos: {boa_1.ratones_consumidos()}')
        print('boa.comer_raton()')
        boa_1.comer_raton()
        print('boa.comer_raton()')
        boa_1.comer_raton()
        print(f'Boa {boa_1.nombre}, ratones consumidos: {boa_1.ratones_consumidos()}')

    @staticmethod
    def huron_comer() -> None:
        print('\nHuron comer ::')
        print(f'{huron_1.nombre}, kilos comidos: {huron_1.obtener_kilos_comidos()}')
        print('huron.comer(3.25)')
        huron_1.comer(3.25)
        print(f'{huron_1.nombre}, kilos comidos: {huron_1.obtener_kilos_comidos()}')

    @staticmethod
    def hacer_sonido() -> None:
        print('\nHacer sonido::')
        print(f'Boa 1 :: {boa_1.hacer_sonido()}')
        print(f'Huron 1 :: {huron_1.hacer_sonido()}\n')
        pass
