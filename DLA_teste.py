import bpy
import numpy as np
import math

#Variáveis globais
tree = []
walkers = []
limite_grid = 10
raio = 1

#Insere a starting point
ponto = {"x":limite_grid/2, "y":limite_grid/2, "z":limite_grid/2}
tree.append(ponto)


def distancia_euclidiana(a,b):
    d = sqrt(pow((b["x"] - a["x"]),2)+pow((b["y"] - a["y"]),2)+pow((b["z"] - a["z"]),2))
    return d


"""max_bolinhas = 100
num_coordenadas = 3

#Inicializo a lista da arvore:
def inicializa_arvore():
    tree = np.zeros([max_bolinhas,num_coordenadas],dtype=int)
    #Estou confusa sobre como colocar um novo elemento no array.
    tree = np.append([lim/2,lim/2,lim/2])
    return 

#cria um Random Walkerexec(compile(open(filename).read(), filename, 'exec'))
walker = np.random.rand(max_bolinhas-1, 3) * lim

#Criar um ponto no centro do meu grid



bpy.ops.mesh.primitive_uv_sphere_add(radius=raio, enter_editmode=False, align='WORLD', location=(lim/2,lim/2, lim/2), scale=(1, 1, 1))


def checa_colisao():
    for i in len(tree):
        d = distancia_euclidiana(walker, tree[i])
        if d < raio*2:


#desenhar todos os pontos que pertencem a lista tree"""