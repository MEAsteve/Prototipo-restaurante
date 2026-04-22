from ventas import (agregar_venta, ventas_restaurante)
from ventas import mostrar_ventas
from ventas import ordenar_ventas
from ventas import buscar_venta
from ventas import eliminar_venta

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Mostrar ventas")
        print("2. Ordenar ventas")
        print("3. Buscar venta")
        print("4. Eliminar venta")
        print("5. Agregar venta")
        print("6. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            mostrar_ventas()
        elif opcion == "2":
            ordenar_ventas()
        elif opcion == "3":
            bv=input("inrese el Id venta abuscar")
            buscar_venta(bv)
        elif opcion == "4":
            eliminar_venta()
        elif opcion == "5":
            agregar_venta()
        elif opcion == "6":
            break
        else:
            print("Opción inválida")

