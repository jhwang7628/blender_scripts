import bpy 

##
filename = 'box_transformation.kin'

##
sce = bpy.context.scene
obj = bpy.context.object

with open(filename, 'w') as stream: 
    for f in range(sce.frame_start, sce.frame_end+1): 
        sce.frame_set(f)
        print ('=== Frame %u' %(f)) 
    
        mat = bpy.context.object.matrix_world 
        print (mat)
        entries = []
        for ii in range(4): 
            for jj in range(4): 
                entries.append(mat[ii][jj])
        mat_str = (' ').join([str('%.12f'%(x)) for x in entries])  
        line = '%u %s\n' %(f, mat_str)
        print (line)
        stream.write(line)
        
                