import json

def abrir():
    mijson=[]
    with open('productos.json', 'r', encoding='utf=8') as openfile:
        mijson = json.load(openfile)
    return mijson

def guardar(data):
    with open('productos.json', 'w', encoding='utf=8') as outfile:
        json.dump(data,outfile)

#inicio
booleano = True

while booleano == True:
    

    seleccion = int(input("elegir la opcion: " ))

    if seleccion == 1:
        general=abrir()
        for i in general["Panaderia"]:
            print(i["Nombre"])



            #holas

print("---------------------------------")
print("                                 ")
print("---------------------------------") 

