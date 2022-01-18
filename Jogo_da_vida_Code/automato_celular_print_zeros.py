import bpy
import random
import numpy as np

#Variaveis globais
espaco = 1.6 #Para não sobrepor nem um pouco usar valor = 2
largura = 10
altura = largura
viver = 0.5
gen = 10

def morto_vivo():
    if random.random() <= viver:
        return 1;
    else:
        return 0;

def cria_matriz_tabuleiro():
    #inicializa a matriz do tabuleiro com zeros
    tabuleiro = np.zeros([largura,altura],dtype=int)
    for x in range (largura):
        for y in range(altura):
            tabuleiro[x][y] = morto_vivo()
    return tabuleiro

#Salva os dados de entrada como uma matriz
def salva_param(tabuleiro):
    aux_text = np.array2string(tabuleiro, separator=';')
    print(aux_text)
    file = open(r"C:\Users\lalad\Documents\Blender\input.txt","w")
    file.write(aux_text)
    file.close()

#Salva uma lista de coordenadas correspondente aos pontos da matriz com valor igual a 1
def salva_param_coord(tabuleiro, op):
    if op == 1:
        file = open(r"C:\Users\lalad\Documents\Blender\input.txt","w")
    if op == 2:
        file = open(r"C:\Users\lalad\Documents\Blender\output.txt","w")
    for x in range (largura):
        for y in range (altura):
            if tabuleiro[x][y] == 0:
                aux = []
                aux.append(x)
                aux.append(y)
                aux_text = str(aux[0]) + " " + str(aux[1])+ "\n"
                print(aux_text)
                file.write(aux_text)
                
    file.close()
    
def desenha_tabuleiro(tabuleiro):
    for x in range (largura):
        for y in range (altura):
            if tabuleiro[x][y] == 0:
                bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(x*espaco,y*espaco,0), scale=(1, 1, 1))

def desenha_tabuleiro_altura(tabuleiro):
    for x in range (largura):
        for y in range (altura):
            if tabuleiro[x][y] == 0:
                bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(x*espaco,y*espaco,random.random()*2), scale=(1, 1, 1))


def is_dentro(x,y):
    if x < 0 or y < 0 or x >= largura or y >= altura:
        return False
    else:
        return True
                
def checavizinhos(tabuleiro,x,y):
    count = 0
    if((is_dentro(x,y+1)) and (tabuleiro[x][y+1] == 1)):
        count +=1
    if((is_dentro(x,y-1)) and (tabuleiro[x][y-1] == 1)):
        count +=1
    if((is_dentro(x+1,y)) and (tabuleiro[x+1][y] == 1)):
        count +=1
    if((is_dentro(x-1,y)) and (tabuleiro[x-1][y] == 1)):
        count +=1
    if((is_dentro(x+1,y+1)) and (tabuleiro[x+1][y+1] == 1)):
        count +=1
    if((is_dentro(x+1,y-1)) and (tabuleiro[x+1][y-1] == 1)):
        count +=1
    if((is_dentro(x-1,y+1)) and (tabuleiro[x-1][y+1] == 1)):
        count +=1
    if((is_dentro(x-1,y-1)) and (tabuleiro[x-1][y-1] == 1)):
        count +=1
    return count 

#Será que eu tenho que atribuir? Testar
def morre (tabuleiro,x, y):
    tabuleiro[x][y] = 0
    return tabuleiro

def nasce (tabuleiro,x,y):
    tabuleiro[x][y] = 1
    return tabuleiro

def geracao(tabuleiro):
    tabuleiro_antigo = tabuleiro
    for x in range (largura):
        for y in range (altura): 
            if(tabuleiro[x][y] == 1):
                vizinhos = checavizinhos(tabuleiro_antigo,x,y)
                if (vizinhos <= 1 or vizinhos > 3):
                    tabuleiro = morre(tabuleiro,x,y)
            if(tabuleiro[x][y] == 0):
                vizinhos = checavizinhos(tabuleiro_antigo,x,y)
                if(vizinhos == 3):
                    tabuleiro = nasce(tabuleiro,x,y)
    return tabuleiro

#A função abaixo foi tirada de Aaron J. Olson            
def limpa_tela():
    if bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)

def junta_objetos():
    if bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.join()


#Função tirada de https://vividfax.github.io/2021/01/14/blender-materials.html
def newMaterial(name_of_material):
    mat = bpy.data.materials.get(name_of_material)
    
    if(mat) is None:
        mat = bpy.data.materials.new(name=name_of_material)
    mat.use_nodes = True
    
    if mat.node_tree:
        mat.node_tree.links.clear()
        mat.node_tree.nodes.clear()
    return mat

def newShader(name_of_material, r, g, b):
    mat = newMaterial(name_of_material)
    
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    
    output = nodes.new(type='ShaderNodeOutputMaterial')

    shader = nodes.new(type='ShaderNodeBsdfGlossy')
    nodes["BSDF - Polimento"].inputs[0].default_value = (r, g, b, 1)
    nodes["BSDF - Polimento"].inputs[1].default_value = 0

    links.new(shader.outputs[0], output.inputs[0])

    return mat
    

if __name__ == '__main__':
    limpa_tela()
    
    tabuleiro = cria_matriz_tabuleiro()
    salva_param_coord(tabuleiro,1)
    #desenha_tabuleiro(tabuleiro)
    
    for i in range(gen):
       tabuleiro = geracao(tabuleiro)
       #print(tabuleiro)
       
    #print(tabuleiro)
    desenha_tabuleiro(tabuleiro) #Pode ser substituido por desenha_tabuleiro_altura
    
    junta_objetos()
    mat = newShader("Shader2", 0.658, 0.428, 0.038)
    bpy.context.active_object.data.materials.append(mat)
    
    salva_param_coord(tabuleiro,2)  
