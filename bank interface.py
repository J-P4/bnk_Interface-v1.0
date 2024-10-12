import json

us = { 
    "clave": 1234,
    "id": 567,
    "cuenta": 289,
    "id_cuenta_us": 1001, 
    "cuenta_segundo_us": 100,
    "cuenta_2nd_us_Vzla": True
}

#Hice esta función para evitar que se utilicen números negativos
#Igualmente tiene algunos problemas para procesar comandos que lleven modulos u otras cosas
def no_negatives(value):
    if value < 0:
        print("El valor no puede ser negativo.")
        return False
    return True

# Guardamos los datos del usuario en un archivo JSON
with open('usuario.json', 'w') as usuario_Data:
    json.dump(us, usuario_Data)

try:
    with open('usuario.json', 'r') as usuario_Data:
        us = json.load(usuario_Data)

    id_us = int(input("introduzca su id: "))
    clave_us = int(input("introduzca su clave: "))

    if id_us == us["id"] and clave_us == us["clave"]:
        while True:
            menu = int(input(''' 
                             
                    Seleccione la operación a relaizar
                    1. Estado de cuenta
                    2. Retiro
                    3. Deposito
                    4. Salir
                    
                    '''))

            if menu == 1:
                print(f'Estado de cuenta: {us["cuenta"]}')
            elif menu == 2:
                withdraw = int(input("ingrese el monto a retirar: "))
                if no_negatives(withdraw):
                    us["cuenta"] -= withdraw
                    with open('usuario.json', 'w') as usuario_Data:
                        json.dump(us, usuario_Data)
                    print(f'Has retirado {withdraw}')
            elif menu == 3:
                send_to = int(input("ingrese el monto a debitar: "))
                if no_negatives(send_to):
                    send_to_2nd = int(input("ingrese el id de la cuenta del segundo usuario: "))
                    if send_to_2nd == us["id_cuenta_us"]:
                        us["cuenta_segundo_us"] += send_to
                        with open('usuario.json', 'w') as usuario_Data:
                            json.dump(us, usuario_Data)
                        print(f'deposito exitoso de {send_to}')
                    else:
                        print(f'ID de cuenta no válido')
            elif menu == 4:
                salida = int(input("desea salir? (1. si, 2. no): "))
                if salida == 1:
                    print("Sesión finalizada")
                    break
                elif salida == 2:
                    continue
            else:
                print("Opción inválida")
    else:
        print("usuario o contraseña incorrecta")
except ValueError as e:
    print(e)
    #Hice estos dos excepts para evitar tanto errores con el json como con los numeros
    #En el caso del Value error se define a e como la excepcion de la función de arriba
except FileNotFoundError:
    print("Archivo JSON no encontrado")



