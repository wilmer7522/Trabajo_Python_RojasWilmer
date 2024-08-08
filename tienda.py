from os import system
from datetime import date
import json


def abrir():
    mijson=[]
    with open('productos.json', 'r', encoding='utf=8') as openfile:
        mijson = json.load(openfile)
    return mijson

def abrirVentas():
    venta=[]
    with open('ventas.json', 'r', encoding='utf=8') as openfile:
        venta = json.load(openfile)
    return venta

def abrirCompras():
    compra=[]
    with open('compras.json', 'r', encoding='utf=8') as openfile:
        compra = json.load(openfile)
    return compra

def guardar(data):
    with open('productos.json', 'w', encoding='utf=8') as outfile:
        json.dump(data,outfile)

def guardarVentas(dataVenta):
    with open('ventas.json', 'w', encoding='utf=8') as outfile:
        json.dump(dataVenta,outfile)

def guardarCompras(dataCompra):
    with open('compras.json', 'w', encoding='utf=8') as outfile:
        json.dump(dataCompra,outfile)

#inicio
        
general = True

while general == True:

    booleano = True

    while booleano == True:
        print("---------------------------------")
        print("     Bienvenido a PanCamp        ")
        print("---------------------------------") 
    
        try:
            seleccion = int(input("Ver Productos 1: \nVentas 2: \nCompras 3:  \nVer Ventas Realizadas 4: \nVer Compras Realizadas 5: \nIngrese opcion:"))
            
            booleano = False
        except ValueError:
            input("ingrese un valor valido")
            system("cls")

    if seleccion == 1:
        general=abrir()
        for i in general[0]["Panaderia"]:
            print(f" ID" ,i["id"], i["Nombre"], "$", i["Precio"])

    if seleccion== 2:
        nuevaVenta = {}
        fecha= date.today()
        nuevaVenta["fechaVenta"] = fecha.isoformat()
        nuevaVenta["nombreCliente"] = input("Nombre del cliente: ")
        nuevaVenta["nombreEmpleado"] = input("nombre del empleado: ")
        nuevaVenta["producto"] = (input("nombre del producto: "))
   

        venta = abrirVentas()
        venta[0]["ventas"].append(nuevaVenta)
        guardarVentas(venta)
        print("venta registrada exitosamente.")


    if seleccion== 3:
        nuevaCompra = {}
        fecha= date.today()
        nuevaCompra["fechaCompra"] = fecha.isoformat()
        nuevaCompra["nombreProveedor"] = input("Nombre del Proveedor: ")
        nuevaCompra["contactoProveedor"] = input("Contacto de Proveedor: ")
        nuevaCompra["producto"] = (input("nombre del producto: "))
        nuevaCompra["cantidad"] = int(input("Cantidad Comprada: "))
        nuevaCompra["Precio"] = int(input("Precio del Producto: "))
   

        compra = abrirCompras()
        compra[0]["compras"].append(nuevaCompra)
        guardarCompras(compra)
        print("Compra registrada exitosamente.")

    if seleccion == 4:
        sell=abrirVentas()
        for i in sell[0]["ventas"]:
            print(f"Fecha de Venta:",i["fechaVenta"],"\n","Cliente:",  i["nombreCliente"],"\n","Empleado:", i["nombreEmpleado"],"\n","Producto:", i["producto"])
                
    if seleccion == 5:
        shop=abrirCompras()
        for i in shop[0]["compras"]:
            print(f"Fecha de Compra:",i["fechaCompra"],"\n","Proveedor:",  i["nombreProveedor"],"\n","Contacto:", i["contactoProveedor"],"\n","Producto:", i["producto"], "Cantidad:" ,i["cantidad"], "Precio:", i["Precio"])
                



            #holas

print("---------------------------------")
print("                                 ")
print("---------------------------------") 

