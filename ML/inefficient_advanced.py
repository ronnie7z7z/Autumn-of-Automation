#This code is complete but a cheap version of the actual code
#It is unable to present accuracies of different features but tells us the overall accuracy if considered 32 independent classes

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
base_dir = os.path.join(os.getcwd(),'Advanced_Assignment_Dataset')

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


#Defining the 32 labels
classes1 = ['left', 'right', 'straight', 'up']
classes2 = ['angry','happy','neutral','sad']
classes3 = ['open','sunglasses']

for cl1 in classes1:
    for cl2 in classes2:
        for cl3 in classes3:
            code = base_dir +'/'+ cl1 +'_'+ cl2 +'_'+ cl3
            images = glob.glob(code + '_[1-9].pgm') + glob.glob(code + '_[1-9]?.pgm')  #The duplicates are eliminated here itself!
            num_train = int(round(len(images)*0.75))
            train, val = images[:num_train], images[num_train:]

            for t in train:
                if not os.path.exists(os.path.join(base_dir, 'train', cl1) + cl2 + cl3):
                    os.makedirs(os.path.join(base_dir, 'train', cl1) + cl2 + cl3)
                shutil.move(t, os.path.join(base_dir, 'train', cl1) + cl2 + cl3)

            for v in val:
                if not os.path.exists(os.path.join(base_dir, 'val', cl1) + cl2+ cl3):
                    os.makedirs(os.path.join(base_dir, 'val', cl1)+ cl2 + cl3)
                shutil.move(v, os.path.join(base_dir, 'val', cl1)+ cl2 + cl3)

train_dir = os.path.join(base_dir, 'train')
val_dir = os.path.join(base_dir, 'val')

batch_size = 100
IMG_SHAPE = 100

image_gen_train = ImageDataGenerator(
    rescale=1.0/255 #No need of variations as every person's face is almost at the middle of the camera 
)

train_data_gen = image_gen_train.flow_from_directory(
    batch_size=batch_size,
    directory=train_dir,
    shuffle=True,
    target_size=(IMG_SHAPE,IMG_SHAPE),
    class_mode='sparse'
)

image_gen_val = ImageDataGenerator(rescale=1.0/255)

val_data_gen = image_gen_val.flow_from_directory(batch_size=batch_size,
    directory=val_dir,
    target_size=(IMG_SHAPE, IMG_SHAPE),
    class_mode='sparse'
)


model = Sequential()

model.add(Conv2D(16, (3,3), padding='same', activation='relu', input_shape=(IMG_SHAPE,IMG_SHAPE, 1)))
model.add(MaxPooling2D(pool_size=(2, 2),strides=2))

model.add(Conv2D(32, (3,3), padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2),strides=2))

model.add(Flatten())
model.add(Dropout(0.2))
model.add(Dense(256, activation='relu'))

model.add(Dense(32))

model.compile(optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)

epochs = 50

history = model.fit_generator(
    train_data_gen,
    steps_per_epoch=int(np.ceil(train_data_gen.n / float(batch_size))),
    epochs=epochs,
    validation_data=val_data_gen,
    validation_steps=int(np.ceil(val_data_gen.n / float(batch_size)))
)

acc = history.history['acc']
val_acc = history.history['val_acc']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()