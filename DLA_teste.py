import bpy
import random
import math

#Variáveis globais
tree = []
walkers = []
MAX_grid = 10
MIN_grid = 0
raio = 1
threshold = raio * 2
num_iteracoes = 10

def rand_face():
    #escolhe face
    rand = random.randint(1,6)
    
    if rand == 1:
        ponto = {"x":random.randint(MIN_grid,MAX_grid), "y":random.randint(MIN_grid,MAX_grid), "z":MIN_grid}
    if rand == 2:
        ponto = {"x":random.randint(MIN_grid,MAX_grid), "y":MIN_grid, "z":random.randint(MIN_grid,MAX_grid)}
    if rand == 3:
        ponto = {"x":MIN_grid, "y":random.randint(MIN_grid,MAX_grid), "z":random.randint(MIN_grid,MAX_grid)}
    if rand == 4:
        ponto = {"x":MAX_grid, "y":random.randint(MIN_grid,MAX_grid), "z":random.randint(MIN_grid,MAX_grid)}
    if rand == 5:
         ponto = {"x":random.randint(MIN_grid,MAX_grid), "y":MAX_grid, "z":random.randint(MIN_grid,MAX_grid)}
    if rand == 6:
         ponto = {"x":random.randint(MIN_grid,MAX_grid), "y":random.randint(MIN_grid,MAX_grid), "z":MAX_grid}
    return ponto

def cria_lista_caminhos_aleatorios(num=10):
    aux = [] 
    for i in range(num):
        ponto = rand_face()
        aux.append(ponto)
    return aux
       

def distancia_euclidiana(a,b):
    d = sqrt(pow((b["x"] - a["x"]),2)+pow((b["y"] - a["y"]),2)+pow((b["z"] - a["z"]),2))
    return d

def checa_colisao(tree,walkers):
    for i in range(len(tree)):
        for j in range(len(walkers)):
            d = distancia_euclidiana(tree[i],walkers[j])
            if d < threshold:
                aux = walkers[j]
                del walkers[j]
                tree.append(aux)
    return tree, walkers

def checa_dentro_grid(ponto):
    if ponto["x"] > MAX_grid or ponto["x"] < MIN_grid:
        return 1
    if ponto["y"] > MAX_grid or ponto["y"] < MIN_grid:
        return 1
    if ponto["z"] > MAX_grid or ponto["z"] < MIN_grid:
        return 1
    return 0
    
            
def rand_anda(ponto):
    aux = 1
    while(aux):
        ponto["x"] += random.randint(-2,2)  
        ponto["y"] += random.randint(-2,2)  
        ponto["z"] += random.randint(-2,2) 
        aux = checa_dentro_grid(ponto)
    if aux == 0:
        print("Ponto:")
        print(ponto)
        print("\n")
        return ponto
        

if __name__ == '__main__':
    #Insere a starting point
    ponto = {"x":limite_grid/2, "y":limite_grid/2, "z":limite_grid/2}
    tree.append(ponto)
    #Crio os caminhos aleatorios
    walkers = cria_lista_caminhos_aleatorios()
    
    original_tree = tree
    original_walkers = walkers
    
    for i in range(len(walkers)):
            print(walkers[i])
    
    for i in range(num_iteracoes):
        #Verifico colizão
        tree, walkers = checa_colisao(tree,walkers)
        
        print("\n")
        for i in range(len(walkers)):
            print(walkers[i])
        print("\n")
        
        if original_tree != tree:
            print("OK")
        if original_walkers != walkers:
            print("OK")
        if original_tree == tree:
            print("NOT OK")
        if original_walkers == walkers:
            print("NOT OK")
        
        #Atualizo o X,Y e Z dos caminhantes
        for i in range(len(walkers)):
            walkers[i] = rand_anda(walkers[i])
            print(walkers[i])
    print("Finish")
        
    
    
    #desenhar todos os pontos que pertencem a lista tree    
    
"""max_bolinhas = 100
num_coordenadas = 3
bpy.ops.mesh.primitive_uv_sphere_add(radius=raio, enter_editmode=False, align='WORLD', location=(lim/2,lim/2, lim/2), scale=(1, 1, 1))"""