import bpy
import numpy as np
# verts contains indices of all selected vertices
# Ref: https://stackoverflow.com/questions/15429796/blender-scripting-indices-of-selected-vertices
verts = [i.index for i in bpy.context.active_object.data.vertices if i.select]
print(verts)
np.savetxt('test.txt', verts, fmt='%u')
