import random
contrasenia = "☺♥qwertyuiopasdfghjklñzxcvbnm♥☺"
longitud = int(input("ingresa la longitud de la contraseña: "))
guarda_resultado = ""
for i in range (longitud):
    guarda_resultado += random.choice(contrasenia)
print (f"esta es tu contraseña {guarda_resultado}")
