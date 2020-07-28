import os
import glob
import numpy as np
# print(os.getcwd())

# os.makedirs()

# os.rename('keep','demo.txt')
# print(os.stat('demo.txt').st_size)

# for dirpath, dirnames, filenames in os.walk(os.getcwd()): #It yields 3 valued tuple 
#     print('Current Path:', dirpath)
#     print('Directories:', dirnames)
#     print('Files:', filenames)
# print(os.listdir())

# print(os.environ.get('HOME'))
# file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
# print(file_path)

# print(os.path.basename('/tmp/test/test.txt')) #Fake file
# print(os.path.dirname('/tmp/test/test.txt'))
# print(os.path.split('/tmp/test/test.txt'))
# print(os.path.splitext('/tmp/test/test.txt'))

# print(os.path.exists('/tmp/test/test.txt'))

# print(os.path.isdir('/tmp/test/test.txt'))
# print(os.path.isfile('/tmp/test/test.txt'))

# print(dir(os.getcwd()))

# base_dir = os.path.join(os.getcwd(),'Advanced_Assignment_Dataset')
# print(base_dir)
# Defining different levels of labels
# classes1 = ['left', 'right', 'straight', 'up']
# classes2 = ['angry','happy','neutral','sad']
# classes3 = ['open','sunglasses']

# img_pathc1 = os.path.join(base_dir, classes1[0],classes2[0],classes3[0])
# print(img_pathc1)


# for cl1 in classes1:
#     for cl2 in classes2:
#         for cl3 in classes3:
#             code = base_dir +'/'+ cl1 +'_'+ cl2 +'_'+ cl3
#             print(code)

# img = glob.glob(os.path.join(base_dir,'train',classes1[0],classes2[0],classes3[0])+classes1[0]+'_'+classes2[0]+'_'+classes3[0]+'_1.pgm')
# print(os.listdir(base_dir))

# os.listdir(base_dir)
