import bpy
import random
spacing = 2.5

for x in range (10):
    for y in range (10):
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(spacing*x,spacing*y,random.random()*2), scale=(1, 1, 1))
        item = bpy.context.object
        if random.random() <= 0.5:
            item.data.materials.append(bpy.data.materials["Verde"])
        else:
            item.data.materials.append(bpy.data.materials["Preto"])