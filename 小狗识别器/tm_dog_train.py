import os
from PIL import Image
import numpy as np
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.optimizers import SGD, RMSprop, Adam
from keras.layers import Conv2D, MaxPooling2D

#--------------------------------------------------------------------------------------------

ima_train = os.listdir('./train')

def read_train_image(filename):
    img = Image.open('./train/' + filename).convert('RGB')
    return np.array(img)

x_train = []

# 图片其实就是一个矩阵（每一个像素都是0-255之间的数）

for i in ima_train:
    x_train.append(read_train_image(i))

x_train = np.array(x_train)

y_train = []
for filename in ima_train:
    y_train.append(int(filename.split('_')[0]))

# 标签（0/1/2/3）
y_train = np.array(y_train)
y_train = y_train - 1
print(y_train)
# -----------------------------------------------------------------------------------------

ima_test = os.listdir('./test')

def read_test_image(filename):
    img = Image.open('./test/'+filename).convert('RGB')
    return np.array(img)

x_test = []

for i in ima_test:
    x_test.append(read_test_image(i))

x_test = np.array(x_test)


y_test = []
for filename in ima_test:
    y_test.append(int(filename.split('_')[0]))

y_test = np.array(y_test)
y_test = y_test - 1

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

#-------------------------------------------------------------------------------------

y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
print(y_train, y_test)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

x_train /= 255
x_test /= 255

print(x_train.shape)
print(y_train.shape)

model = Sequential()
# input: 100x100 images with 3 channels -> (100, 100, 3) tensors.
# this applies 32 convolution filters of size 3x3 each.
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(4, activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=10, epochs=32)
model.save_weights('./dog_weights.h5', overwrite=True)

# model.load_weights('dog_weights.h5')
score = model.evaluate(x_test, y_test, batch_size=10)
print(score)

# classes = model.predict_classes(x_test)[0]
#
# test_accuracy = np.mean(np.equal(y_test, classes))
# print("accuarcy:", test_accuracy)


# 3-泰迪 2-柯基 1-拉布拉多 0-京巴
