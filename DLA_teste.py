import bpy
import random
import math

#Variáveis globais
tree = []
walkers = []
MAX_grid = 10
MIN_grid = 0
raio = 1

#Insere a starting point
ponto = {"x":limite_grid/2, "y":limite_grid/2, "z":limite_grid/2}
tree.append(ponto)

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

"""def cria_lista_caminhos aleatorios(num):
    aux = [] 
    for i in range(num):"""
       

def distancia_euclidiana(a,b):
    d = sqrt(pow((b["x"] - a["x"]),2)+pow((b["y"] - a["y"]),2)+pow((b["z"] - a["z"]),2))
    return d

"""def checa_colisao():
    for i in len(tree):
        for j in len(walkers):
            d = distancia_euclidiana(tree[i],walkers[j])
            if d < raio*2:"""
                
    
#max_bolinhas = 100
#num_coordenadas = 3


#bpy.ops.mesh.primitive_uv_sphere_add(radius=raio, enter_editmode=False, align='WORLD', location=(lim/2,lim/2, lim/2), scale=(1, 1, 1))

#desenhar todos os pontos que pertencem a lista tree"""