import random
usuarios=[]

for _ in range(10):
    nombre=random.choice(['Juajo','Laloca','Sara uvu','Lyz,ugu','Todos ugu'])
    contraseña=random.choice(['Admini123', 'Arbolesugu0000'])
    edad=random.randint(18,64)
    usuario=[nombre,contraseña,edad]
    usuarios.append(usuario)
    
    print(usuarios)