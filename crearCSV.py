import csv 
#Con esto creamos un formato, visual nada más, pa ponerlos bonitos uvu
#El 'w' es write, pa escribir mi pa

def crearCSVUSuarios(lista,nombreArchivo):
    with open('data/'+nombreArchivo,mode='w',newline='',encoding='utf-8') as archivoCSV:
        writer=csv.writer (archivoCSV)
        writer.writerow(['Nombre','Contraseña','Edad'])
        writer.writerow(lista)
        
def refrigerios(lista,nombreArchivo):
    with open('data/'+nombreArchivo,mode='w',newline='',encoding='utf-8') as archivoCSV:
        writer=csv.writer (archivoCSV)
        writer.writerow(['usuarios','refrigerios'])
        writer.writerow(lista)