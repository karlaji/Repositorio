#Ejemplos del uso de if en python

esta_lloviendo = True
tenemos_hambre = False
python_es_genial = True
Ayer_pagaron = False
vamos_a_la_playa = False

#Funcion para solicitar datos por consola input("mensage")
# La funcion input simepre retorna un string. teneemos que cnvertirlo a numero antes de hacer operaciones numericas


numero_digitado =input ("Digita un numero: ") # Almaceno como string
numero_digitado_como_numero = float (numero_digitado)




if esta_lloviendo and tenemos_hambre:
    #Este código está dentro del if
    print ("Esta lloviendo y tenemos hambre")
elif 12 < numero_digitado_como_numero and python_es_genial or vamos_a_la_playa:
    print ("Python es genial o vamos_a_la_playa")
else:
    print("esto se ejecuta si ninguna condición anterior es verdadera")




