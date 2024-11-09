from models.guarderia import Guarderia
from services.fake_services import Fake_Service

# Creamos las instancias
guarderia = Guarderia('La Guarderia')
boas = Fake_Service.get_boas()
hurones = Fake_Service.get_hurones()

# Asociamos los boas y hurones
for boa in boas:
    guarderia.agregar_boa(boa)

for huron in hurones:
    guarderia.agregar_huron(huron)

# Prueba de alimentación sin boa
print(guarderia.alimentar_boa(None))

# Prueba de alimentación con boa
contador = 1
while contador <= 21:
    print(guarderia.alimentar_boa(boas[0]))
    contador += 1

# Para lanzar las pruebas, ejecutar desde la consola:
# python -m unittest discover -s tests
