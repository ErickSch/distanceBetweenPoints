import Location as loc
import plots
import math

#Calculo de distancia
def calc_distancia(client, suc):
    x1 = client.x
    x2 = suc.x
    
    y1 = client.y
    y2 = suc.y

    distancia = round(math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2)), 3)
    return distancia

#Ejecutar la interfaz en la consola
def start_gui():
    resp = 0

    while(resp != -1):
        print(""" 
            -------------------------------
            1. Crear cliente
            2. Crear sucursal
            3. Graficar mapa
            4. Buscar sucursal mas cercana
            
            -1. Salir
            -------------------------------
        """)
        resp = int(input('Ingrese accion: '))

        #Crear cliente
        if(resp == 1):
            nombre = input("Ingrese nombre de cliente: ")
            x = int(input("Ingrese coordenada x del cliente: "))
            y = int(input("Ingrese coordenada y del cliente: "))
            plots.casas.append(loc.Location(nombre, x, y))
            print("Cliente creado exitosamente!!")
        
        #Crear sucursal
        elif(resp == 2):
            nombre = input("Ingrese nombre de sucursal: ")
            x = int(input("Ingrese coordenada x del sucursal: "))
            y = int(input("Ingrese coordenada y del sucursal: "))
            plots.sucursales.append(loc.Location(nombre, x, y))
            print("Sucursal creado exitosamente!!")

        #Mostrar la grafica
        elif(resp == 3):
            plots.plot_puntos()

        #Calcular y mostrar la distancia entre un cliente y su sucursal mas cercana
        elif(resp == 4):
            
            #Elegir cliente a para calcular
            seguir = False
            print("-------------------------------")
            print("Clientes:")
            while(seguir == False):
                for i in range(len(plots.casas)):
                    print(f"\t-{plots.casas[i].nombre}")
                
                print("-------------------------------")
                nombre_cliente = input("Ingresa nombre de cliente: ")
                for i in range(len(plots.casas)):
                    if (plots.casas[i].nombre == nombre_cliente):
                        cliente = plots.casas[i]
                        seguir = True
                    if(i == len(plots.casas)-1 and seguir == False):
                        print(f'Cliente "{nombre_cliente}" no existe')
                        
                
                        

            #Calcular distancia entre cliente y la sucursal mas cercana
            distancia = calc_distancia(cliente, plots.sucursales[0])
            sucursal = plots.sucursales[0]
            nombre_sucursal = sucursal.nombre
            for i in range(1, len(plots.sucursales)):
                calculo_dist = calc_distancia(cliente, plots.sucursales[i])
                if (calculo_dist < distancia):
                    sucursal = plots.sucursales[i]
                    distancia = calculo_dist
                    nombre_sucursal = plots.sucursales[i].nombre


            print(f'Sucursal "{nombre_sucursal}" se encuentra a {distancia} km de {nombre_cliente} y es la mas cercana')
            plots.plot_distancia(cliente, sucursal)

        elif(resp == -1):
            print("Programa terminado")
            break
        
        #Si el numero de accion no existe
        else:
            print("La accion no existe")
        
    


