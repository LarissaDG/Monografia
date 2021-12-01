import bpy
import random
import math


#Variáveis globais
tree = []
walkers = []
MAX_grid = 10
MIN_grid = 0
raio = 1
threshold = raio*2 
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
    remove = []
    for j in range(len(walkers)):
        for i in range(len(tree)):
            d = distancia_euclidiana(tree[i],walkers[j])
            if d < threshold:
                print("BOOOM!!!!!!")
                print(tree[i])
                print(walkers[j])
                print("\n")
                remove.append(j)
                break
                
    remove.sort(reverse=True)
    
    print(remove)
    print(len(walkers))
    
    for i in remove:
        aux = walkers.pop(i)
        tree.append(aux)
        
            
    return tree, walkers
    
            
def rand_anda(ponto):
    
    ponto["x"] += random.randint(-2,2)
    while(ponto["x"] > MAX_grid or ponto["x"] < MIN_grid):
        ponto["x"] += random.randint(-2,2)
        
    ponto["y"] += random.randint(-2,2)
    while(ponto["y"] > MAX_grid or ponto["y"] < MIN_grid):
        ponto["y"] += random.randint(-2,2) 
        
    ponto["z"] += random.randint(-2,2)
    while(ponto["z"] > MAX_grid or ponto["z"] < MIN_grid):
        ponto["z"] += random.randint(-2,2)
            
    return ponto

def desenha_bolinhas(lista):
    for i in range(len(lista)):
        bpy.ops.mesh.primitive_uv_sphere_add(radius=raio, enter_editmode=False, align='WORLD', location=(lista[i]["x"],lista[i]["y"],lista[i]["z"]), scale=(1, 1, 1))    
    
#Os cubos sobrepõe muito ruim os resultados
def desenha_cubos(lista):
    for i in range(len(lista)):
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(lista[i]["x"],lista[i]["y"],lista[i]["z"]), scale=(1, 1, 1))

#No 2D talvez fique legal. No 3D ficou ruim
def desenha_torus(lista):
    for i in range(len(lista)):
        bpy.ops.mesh.primitive_torus_add(align='WORLD', location=(lista[i]["x"],lista[i]["y"],lista[i]["z"]), rotation=(0, 0, 0))
    

#A função abaixo foi tirada de Aaron J. Olson            
def limpa_tela():
    if bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)


if __name__ == '__main__':  
    #Insere a starting point
    ponto = {"x":MAX_grid/2, "y":MAX_grid/2, "z":MAX_grid/2}
    
    
    #bpy.ops.mesh.primitive_uv_sphere_add(radius=raio, enter_editmode=False, align='WORLD', location=(ponto["x"],ponto["y"],ponto["z"]), scale=(1, 1, 1))    
    
    tree.append(ponto)
        
    #Crio os caminhos aleatorios
    walkers = cria_lista_caminhos_aleatorios()

    #Testado
    
    #desenha_bolinhas(walkers)
    
    #for i in range(num_iteracoes):
    while(len(tree)<num_iteracoes):
        #limpo tela
        limpa_tela()
        
        #Verifico colisão, se houve colisão tiro de uma lista e ponho na outra
        tree, walkers = checa_colisao(tree,walkers)
        
        #Os que não foram removidos
        #Atualizo o X,Y e Z dos caminhantes
        for i in range(len(walkers)):
            walkers[i] = rand_anda(walkers[i])
            print(walkers[i])
        
        #Imprimo bolinhas
        #desenha_bolinhas(tree)
        #desenha_bolinhas(walkers)
       
    desenha_bolinhas(tree) 
    #desenha_cubos(tree)  
    #desenha_torus(tree) 
    print("Finish")
        