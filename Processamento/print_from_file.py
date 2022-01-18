import bpy
import numpy as np
from numpy import savetxt
from numpy import loadtxt
raio = 0.8
espaco = 2

#Funções 3D
def desenha_bolinhas(lista):
    for i in range(np.shape(lista)[0]):
        bpy.ops.mesh.primitive_uv_sphere_add(radius=raio, enter_editmode=False, align='WORLD', location=(lista[i][0],lista[i][1],lista[i][2]), scale=(1, 1, 1))

    
#Os cubos sobrepõe muito ruim os resultados -Ficou ruim no 2D tbm
def desenha_cubos(lista):
    for i in range(np.shape(lista)[0]):
        bpy.ops.mesh.primitive_cube_add(size=raio, enter_editmode=False, align='WORLD', location=(lista[i][0],lista[i][1],lista[i][2]), scale=(1, 1, 1))

#No 2D talvez ficou legal. 
def desenha_torus(lista):
    for i in range(np.shape(lista)[0]):
        bpy.ops.mesh.primitive_torus_add(align='WORLD', location=(lista[i][0],lista[i][1],lista[i][2]), rotation=(0, 0, 0))
    
def desenha_circulo(lista):
    for i in range(np.shape(lista)[0]):
       bpy.ops.mesh.primitive_circle_add(radius=raio, fill_type='TRIFAN', enter_editmode=False, align='WORLD', location=(lista[i][0],lista[i][1],lista[i][2]), scale=(1, 1, 1))

#Funcoes 2D
def desenha_bolinhas_2D(lista):
    for i in range(np.shape(lista)[0]):
        bpy.ops.mesh.primitive_uv_sphere_add(radius=raio, enter_editmode=False, align='WORLD', location=(lista[i][0]*espaco,lista[i][1]*espaco,0), scale=(1, 1, 1))    
    
#Os cubos sobrepõe muito ruim os resultados -Ficou ruim no 2D tbm
def desenha_cubos_2D(lista):
    for i in range(np.shape(lista)[0]):
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(lista[i][0]*espaco,lista[i][1]*espaco,0), scale=(1, 1, 1))

#No 2D talvez ficou legal. 
def desenha_torus_2D(lista):
    for i in range(np.shape(lista)[0]):
        bpy.ops.mesh.primitive_torus_add(align='WORLD', location=(lista[i][0],lista[i][1],0), rotation=(0, 0, 0))
    
def desenha_circulo_2D(lista):
    for i in range(np.shape(lista)[0]):
       bpy.ops.mesh.primitive_circle_add(radius=raio, fill_type='TRIFAN', enter_editmode=False, align='WORLD', location=(lista[i][0]*espaco,lista[i][1]*espaco,0), scale=(1, 1, 1))


def desenha_quadrado_2D(lista):
    for i in range(np.shape(lista)[0]):
        bpy.ops.mesh.primitive_plane_add(enter_editmode=False, align='WORLD', location=(lista[i][0],lista[i][1],0), scale=(1, 1, 1))
        

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
    m = np.loadtxt(r"C:\Users\lalad\Documents\Blender\square_pattern_2.txt", dtype=int)
    limpa_tela()
    #desenha_bolinhas_2D(m)
    desenha_circulo_2D(m)
    #desenha_quadrado_2D(m)
    #desenha_cubos_2D(m)
    junta_objetos()
    #mat = newShader("Shader", 0.494,0.894, 0.658)
    mat = newShader("Shader2", 0.658, 0.428, 0.038)