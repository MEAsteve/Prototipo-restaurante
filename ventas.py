ventas_restaurante = []
orden=[]

ventas_restaurante = [
 {"idVenta": 3, "nombreCliente": "Juan", "numeroMesa": 1, "platoPrincipal": "Pizza", "valorConsumo": 25000, "metodoPago": "EFECTIVO", "estadoPedido": "ENTREGADO"},
    {"idVenta": 2, "nombreCliente": "Ana", "numeroMesa": 2, "platoPrincipal": "Hamburguesa", "valorConsumo": 18000, "metodoPago": "TARJETA", "estadoPedido": "PENDIENTE"},
    {"idVenta": 1, "nombreCliente": "Luis", "numeroMesa": 3, "platoPrincipal": "Pasta", "valorConsumo": 22000, "metodoPago": "TRANSFERENCIA", "estadoPedido": "ENTREGADO"},
    {"idVenta": 6, "nombreCliente": "Marta", "numeroMesa": 4, "platoPrincipal": "Ensalada", "valorConsumo": 15000, "metodoPago": "EFECTIVO", "estadoPedido": "PENDIENTE"},
    {"idVenta": 5, "nombreCliente": "Pedro", "numeroMesa": 5, "platoPrincipal": "Sushi", "valorConsumo": 30000, "metodoPago": "TARJETA", "estadoPedido": "ENTREGADO"},
    {"idVenta": 4, "nombreCliente": "Laura", "numeroMesa": 6, "platoPrincipal": "Carne", "valorConsumo": 35000, "metodoPago": "TRANSFERENCIA", "estadoPedido": "PENDIENTE"},
    {"idVenta": 7, "nombreCliente": "Carlos", "numeroMesa": 7, "platoPrincipal": "Pollo", "valorConsumo": 20000, "metodoPago": "EFECTIVO", "estadoPedido": "ENTREGADO"},
    {"idVenta": 9, "nombreCliente": "Sofia", "numeroMesa": 8, "platoPrincipal": "Arepa", "valorConsumo": 12000, "metodoPago": "TARJETA", "estadoPedido": "PENDIENTE"},
    {"idVenta": 8, "nombreCliente": "Diego", "numeroMesa": 9, "platoPrincipal": "Tacos", "valorConsumo": 27000, "metodoPago": "TRANSFERENCIA", "estadoPedido": "ENTREGADO"},
    {"idVenta": 10, "nombreCliente": "Valentina", "numeroMesa": 10, "platoPrincipal": "Pizza", "valorConsumo": 26000, "metodoPago": "EFECTIVO", "estadoPedido": "PENDIENTE"},
]


def agregar_venta():
    m=10
    
    nombrecl = input("Ingrese el nombre del cliente: ")
    numMesa = input("Ingrese el numero de mesa: ")
    plato = input("Ingrese el plato pedido: ")
    totl = input("Ingrese el total del pedido: ")
    metodo = input("Ingrese el metodo de pago: ")
    estatus = input("Ingrese el estado de pedido: ")
    
    nueva = {
        "idVenta": m + 1,
        "nombreCliente": nombrecl,
        "numeroMesa": numMesa,
        "platoPrincipal": plato,
        "valorConsumo": totl,
        "metodoPago": metodo,
        "estadoPedido": estatus
    }
    ventas_restaurante.append(nueva)
    return nueva


        

        
def mostrar_ventas():
    for a in ventas_restaurante:
        print(a)
        
        return print()
    
   
    
def ordenar_ventas():
  ventas_restaurante.sort(key=lambda venta: venta["valorConsumo"])
  for a in ventas_restaurante:
        print(a)
   


def buscar_venta(id_buscar):
    for venta in ventas_restaurante:
        if venta["idVenta"] == id_buscar:
            return venta
    return None



def eliminar_venta():
    id_eliminar = int(input("Ingrese el ID de la venta a eliminar: "))

    for venta in ventas_restaurante:
        if venta["idVenta"] == id_eliminar:
            ventas_restaurante.remove(venta)
            print("Venta eliminada correctamente")
            return

    print("Venta no encontrada")