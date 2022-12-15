from matplotlib import pyplot as plt
import Location as loc



#Casas de clientes predefinidos en mapa
casas = [loc.Location('Paola', 5, 7), loc.Location('Luis', 3, 2)]

#Sucursales predefinidas en mapa
sucursales = [loc.Location('1', 8, 9), loc.Location('2', 4, 7), loc.Location('3', 7, 3)]


#Graficar mapa
def plot_puntos():
    fig, ax = plt.subplots()

    #Limites de la grafica
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.grid()

    #Graficar sucursales con negro
    for i in range(len(sucursales)):
        ax.plot(sucursales[i].x, sucursales[i].y, 'o', color='black')
        ax.annotate(sucursales[i].nombre, (sucursales[i].x + 0.1, sucursales[i].y))

    #Graficar casas de clientes con azul
    for i in range(len(casas)):
        ax.plot(casas[i].x, casas[i].y, 'o', color='blue')
        ax.annotate(casas[i].nombre, (casas[i].x + 0.1, casas[i].y))
    
    plt.title('Mapa de clientes y sucursales')
    plt.xlabel('km')
    plt.ylabel('km')

    plt.show() 

#Graficar con camino entre cliente y sucursal dados
def plot_distancia(cliente, sucursal):
    fig, ax = plt.subplots()

    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.grid()

    for i in range(len(sucursales)):
        ax.plot(sucursales[i].x, sucursales[i].y, 'o', color='black')
        ax.annotate(sucursales[i].nombre, (sucursales[i].x, sucursales[i].y))

    for i in range(len(casas)):
        ax.plot(casas[i].x, casas[i].y, 'o', color='blue')
        ax.annotate(casas[i].nombre, (casas[i].x, casas[i].y))
    
    x_distancia = [cliente.x, sucursal.x]
    y_distancia = [cliente.y, sucursal.y]
    
    ax.plot(x_distancia, y_distancia, '--', color='red')

    plt.title('Mapa de clientes y sucursales')
    plt.xlabel('km')
    plt.ylabel('km')


    plt.show() 




# fruits = ['apple', 'blueberry', 'cherry', 'orange']
# counts = [40, 100, 30, 55]
# bar_labels = ['red', 'blue', '_red', 'orange']
# bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

# ax.bar(fruits, counts, label=bar_labels, color=bar_colors)