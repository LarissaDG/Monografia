import bpy
import numpy as np
from numpy import savetxt
from numpy import loadtxt
raio = 0.8
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
        bpy.ops.mesh.primitive_uv_sphere_add(radius=raio, enter_editmode=False, align='WORLD', location=(lista[i][0],lista[i][1],0), scale=(1, 1, 1))    
    
#Os cubos sobrepõe muito ruim os resultados -Ficou ruim no 2D tbm
def desenha_cubos_2D(lista):
    for i in range(np.shape(lista)[0]):
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(lista[i][0],lista[i][1],0), scale=(1, 1, 1))

#No 2D talvez ficou legal. 
def desenha_torus_2D(lista):
    for i in range(np.shape(lista)[0]):
        bpy.ops.mesh.primitive_torus_add(align='WORLD', location=(lista[i][0],lista[i][1],0), rotation=(0, 0, 0))
    
def desenha_circulo_2D(lista):
    for i in range(np.shape(lista)[0]):
       bpy.ops.mesh.primitive_circle_add(radius=raio, fill_type='TRIFAN', enter_editmode=False, align='WORLD', location=(lista[i][0],lista[i][1],0), scale=(1, 1, 1))


def desenha_quadrado_2D(lista):
    for i in range(np.shape(lista)[0]):
        bpy.ops.mesh.primitive_plane_add(enter_editmode=False, align='WORLD', location=(lista[i][0],lista[i][1],0), scale=(1, 1, 1))
        

#A função abaixo foi tirada de Aaron J. Olson            
def limpa_tela():
    if bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
        

if __name__ == '__main__':
    m = np.loadtxt(r"C:\Users\lalad\Documents\Blender\lista_2D_2.txt", dtype=int)
    #desenha_bolinhas(m)
    desenha_circulo_2D(m)
    #desenha_quadrado_2D(m)