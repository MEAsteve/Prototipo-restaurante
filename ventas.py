ventas_restaurante = []

def agregar_venta():
    m=0
    
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
    return nueva

nv=agregar_venta()

ventas_restaurante.append(nv)

    
    



for a in ventas_restaurante:
    print(a)