import random 

longitud= int(input("¿De cúantos caracteres quieres que genere la contraseña que vas a utilizar?")) 
caracteres="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" 
contraseña=''.join(random.choice(caracteres) for i in range(longitud))

print("Tu contraseña es la siguiente:", contraseña)