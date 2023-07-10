import os
os.system("cls")

menu = """
1. Comprar entradas
2. Mostrar ubicacion disponibles
3. Ver listado de asistentes
4. Mostrar ganancias totales
5. Salir
"""
cont = 0

lista_rut = []
lista_asiento = []

escenario0 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
escenario1 = ['11','12','13','14','15','16','17','18','19','20']
escenario2 = ['21','22','23','24','25','26','27','28','29','30']
escenario3 = ['31','32','33','34','35','36','37','38','39','40']
escenario4 = ['41','42','43','44','45','46','47','48','49','50']
escenario5 = ['51','52','53','54','55','56','57','58','59','60']
escenario6 = ['61','62','63','64','65','66','67','68','69','70']
escenario7 = ['71','72','73','74','75','76','77','78','79','80']
escenario8 = ['81','82','83','84','85','86','87','88','89','90']
escenario9 = ['91','92','93','94','95','96','97','98','99','100']

def comprar():
    while True:
        try:
            aComprar = int(input("Cantidad de boletos a comprar?[Considere de 1 a 3 boletos]: \n"))
            if aComprar < 4 and aComprar >0:
                print("Cantidad de boletos válida!")
                print(escenario0)
                print(escenario1)
                print(escenario2)
                print(escenario3)
                print(escenario4)
                print(escenario5)
                print(escenario6)
                print(escenario7)
                print(escenario8)
                print(escenario9)                
                break
            else:
                print("Error de cantidad")
        except:
            print("Ha ocurrido una excepcion1")
    for i in range(0, aComprar):
        i += 1
        try:
            asiento = input("Asiento deseado?[Asiento no disponible mostrado con X]: \n")
            for i in range(len(escenario0)):
                    if asiento == escenario0[i]:
                        run()
                        lista_asiento.append(asiento)
                        escenario0.remove(asiento)
                        escenario0.insert(i, 'X')
                        print(escenario0)
                    elif escenario0[i] == 'X':
                         print("No esta disponible")
            for i in range(len(escenario1)):
                    if asiento == escenario1[i]:
                        run()
                        lista_asiento.append(asiento)
                        escenario1.remove(asiento)
                        escenario1.insert(i, 'X')
                        print(escenario1)
                    elif escenario1[i] == 'X':
                         print("No esta disponible")
            for i in range(len(escenario2)):
                    if asiento == escenario2[i]:
                        run()
                        lista_asiento.append(asiento)
                        escenario2.remove(asiento)
                        escenario2.insert(i, 'X')
                        print(escenario2)
                    elif escenario2[i] == 'X':
                         print("No esta disponible")
            for i in range(len(escenario3)):
                    if asiento == escenario3[i]:
                        run()
                        lista_asiento.append(asiento)
                        escenario3.remove(asiento)
                        escenario3.insert(i, 'X')
                        print(escenario3)
                    elif escenario3[i] == 'X':
                         print("No esta disponible")
            for i in range(len(escenario4)):
                    if asiento == escenario4[i]:
                        run()
                        lista_asiento.append(asiento)
                        escenario4.remove(asiento)
                        escenario4.insert(i, 'X')
                        print(escenario4)
                    elif escenario4[i] == 'X':
                         print("No esta disponible")
            for i in range(len(escenario5)):
                    if asiento == escenario5[i]:
                        run()
                        lista_asiento.append(asiento)
                        escenario5.remove(asiento)
                        escenario5.insert(i, 'X')
                        print(escenario5)
                    elif escenario5[i] == 'X':
                         print("No esta disponible")
            for i in range(len(escenario6)):
                    if asiento == escenario6[i]:
                        run()
                        lista_asiento.append(asiento)
                        escenario6.remove(asiento)
                        escenario6.insert(i, 'X')
                        print(escenario6)
                    elif escenario6[i] == 'X':
                         print("No esta disponible")    
            for i in range(len(escenario7)):
                    if asiento == escenario7[i]:
                        run()
                        lista_asiento.append(asiento)
                        escenario7.remove(asiento)
                        escenario7.insert(i, 'X')
                        print(escenario7)
                        print(f"Tu asiento es {escenario7[i]}")
                    elif escenario7[i] == 'X':
                         print("No esta disponible")
            for i in range(len(escenario8)):
                    if asiento == escenario8[i]:
                        run()
                        lista_asiento.append(asiento)
                        escenario8.remove(asiento)
                        escenario8.insert(i, 'X')
                        print(escenario8)
                    elif escenario8[i] == 'X':
                         print("No esta disponible")    
            for i in range(len(escenario9)):
                    if asiento == escenario9[i]:
                        run()
                        lista_asiento.append(asiento)
                        escenario9.remove(asiento)
                        escenario9.insert(i, 'X')
                        print(escenario9)
                    elif escenario9[i] == 'X':
                         print("No esta disponible")
        except:
            print("Error de excepcion2")

def mostrar():
            print(escenario0)
            print(escenario1)
            print(escenario2)
            print(escenario3)
            print(escenario4)
            print(escenario5)
            print(escenario6)
            print(escenario7)
            print(escenario8)
            print(escenario9)
    
def run():
    while True:    
        run = input("Rut del cliente?[No considerar guion ni punto ni numero verificador]: \n")
        for i in range(len(run)):
            if run[i] == '-' or run[i] == '.':
                print("Por favor escribir bien")
        else:
            print("Se ha agregado de manera exitosa!")
            lista_rut.append(run)
            break
def listado():
     print(" RUT    |   Asiento")
     for i in range(len(lista_rut)):
        print(f"{lista_rut[i]}, {lista_asiento[i]}")     


def ganancias():
     cPlat = 0
     cGold = 0
     cSilver = 0
     for i in range(len(escenario1)):
        if escenario1[i] == 'X':
             cPlat = cPlat + 1
             print(cPlat)
       
 
               

while True:
    try:
        opc = int(input(menu))
        if opc == 1:
            comprar()
        elif opc == 2:
             mostrar()
        elif opc == 3:
             listado()
        elif opc == 4:
             ganancias()
        elif opc == 5:
             print("Hasta luego\nPrograma de Ignacio Sorko\n10/07/2023")
             break             
    except:
        print("Error de excepcion")