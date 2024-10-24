import random
contrasenia = "☺♥qwertyuiopasdfghjklñzxcvbnm♥☺"
longitud = int(input("ingresa la longitud de la contraseña: "))
guarda_resultado = ""
for i in range (longitud):
    guarda_resultado += random.choice(contrasenia)
    resultado = guarda_resultado
print (f"esta es tu contraseña {guarda_resultado}")
palabra = input("quieres terminar el juego ")
if palabra == "no":
    jugar = True
    while jugar:
        print ("entra a la casa")
        print ("cual es el codigo")
        resultado = input("cual es la contrasenia ")
        if resultado == guarda_resultado:
            print ("bien")
            jugar = False
        else:
            print ("mal")
