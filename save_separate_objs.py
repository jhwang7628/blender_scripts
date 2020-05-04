# Ref: https://blender.stackexchange.com/questions/5382/export-multiple-objects-to-obj
import bpy

#example path to store files
path = '/Users/juiwang/code/physics-demo/meshes/Dn_meshes/scene/separated'

#store selection
obs = bpy.context.selected_objects

for ob in obs:
    #deselect all but just one object and make it active
    bpy.ops.object.select_all(action='DESELECT')
    ob.select_set(state=True)
    bpy.context.view_layer.objects.active = ob

    #store object location then zero it out
    location = ob.location.copy()
    bpy.ops.object.location_clear()

    #export fbx
    filename = path + ob.name + '.obj'
    print('filename = ', filename)
    bpy.ops.export_scene.obj(filepath=filename, use_selection=True)

    #restore location
    ob.location = location

#reselect originally selected objects
for ob in obs:
    ob.select_set(state=True)
