#This code is supposed to be the ideal multi-feature classification model
#But it is incomplete, I'm adding to it at the moment as I gather some useful methods that I can find

import os
import numpy as np
import glob
import shutil
import scipy
import tensorflow as tf
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

#Storing address of folder containing the images
root = os.path.join(os.getcwd())
base_dir = os.path.join(root,'Advanced_Assignment_Dataset')

#Conversion of pgm files to jpg or png
# for filename in os.listdir(base_dir):
#     if filename.endswith(".pgm"):
#         os.chdir(base_dir)
#         name = filename[:-4]
#         os.rename(name + '.pgm',name + '.png')
#         os.chdir(root)
#         continue
#     else:
#         continue

#Defining different levels of labels
classes1 = ['left', 'right', 'straight', 'up']
classes2 = ['angry','happy','neutral','sad']
classes3 = ['open','sunglasses']
tp = ['train','val']

#Creation and distribution of images in their respective directories

for cl1 in classes1:
    for cl2 in classes2:
        for cl3 in classes3:
            code = base_dir +'/'+ cl1 +'_'+ cl2 +'_'+ cl3
            images = glob.glob(code + '_[1-9].pgm') + glob.glob(code + '_[1-9]?.pgm')  #The duplicates are eliminated here itself! hehe!
            num_train = int(round(len(images)*0.75))
            train, val = images[:num_train], images[num_train:]

            for t in train:
                if not os.path.exists(os.path.join(base_dir, 'train', cl1, cl2, cl3)):
                    os.makedirs(os.path.join(base_dir, 'train', cl1, cl2, cl3))
                shutil.move(t, os.path.join(base_dir, 'train', cl1, cl2, cl3))

            for v in val:
                if not os.path.exists(os.path.join(base_dir, 'val', cl1, cl2, cl3)):
                    os.makedirs(os.path.join(base_dir, 'val', cl1, cl2, cl3))
                shutil.move(v, os.path.join(base_dir, 'val', cl1, cl2, cl3))

train_dir = os.path.join(base_dir, 'train')
val_dir = os.path.join(base_dir, 'val')

batchsize = 100
ImgShape = 100

image_gen_train = ImageDataGenerator( #No need of different orientations/zoom or such as people are almost in the same position and dist from the camera
    rescale=1./255
)

train_data_gen = image_gen_train.flow_from_directory(
    batch_size=batchsize,
    directory=train_dir,
    shuffle=True,
    target_size=(ImgShape,ImgShape),
    class_mode='sparse'
)

image_gen_val = ImageDataGenerator(rescale=1./255)

val_data_gen = image_gen_val.flow_from_directory(batch_size=batchsize,
    directory=val_dir,
    target_size=(ImgShape, ImgShape),
    class_mode='sparse'
)



            
   