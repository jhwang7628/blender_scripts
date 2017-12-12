import bpy 
import bpy_extras

sce = bpy.context.scene
obj = bpy.context.object

with open('leroy_box_top_y-up.kin', 'w') as stream: 
    for f in range(sce.frame_start, sce.frame_end+1): 
        sce.frame_set(f)
        print ('=== Frame %u' %(f)) 
    
        global_matrix = bpy_extras.io_utils.axis_conversion(to_forward="-Z", to_up="Y").to_4x4()
        print (global_matrix)
        mat = global_matrix * bpy.context.object.matrix_world * global_matrix.transposed()
        entries = []
        for ii in range(4): 
            for jj in range(4): 
                entries.append(mat[ii][jj])
        # mat_str = (' ').join([str('%.12f'%(x)) for x in entries])  
        # line = '%u %s\n' %(f, mat_str)
        
        tra, rot, sca = mat.decompose()
        # format: frame, translate_x, translate_y, translate_z, quaternion_w, quaternion_x, quaternion_y, quaternion_z
        line = '%u %.12f %.12f %.12f %.12f %.12f %.12f %.12f\n' %(f, tra[0], tra[1], tra[2], rot.w, rot.x, rot.y, rot.z)
        
        print (line)
        stream.write(line)