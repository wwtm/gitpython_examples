import os
from PIL import Image
import numpy as np
import keras
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Flatten
from keras.optimizers import SGD
from keras.layers import Conv2D, MaxPooling2D

name = input('上传图片的名称（例如：XX.jpg）为：')

img = Image.open('pic/' + name)
new_img = img.resize((100, 100), Image.BILINEAR)
new_img.save('pic/' + name)

img = Image.open('pic/' + name).convert('RGB')
img = np.array(img)

# 预处理图片 变成100 x 100
x_test = []

x_test.append(img)

x_test = np.array(x_test)

x_test = x_test.astype('float32')
x_test /= 255

# keras.backend.clear_session()

model = Sequential()

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

model.load_weights('dog_weights.h5')
classes = model.predict_classes(x_test)[0]

target = ['京巴', '拉布拉多', '柯基', '泰迪']
# 3-泰迪 2-柯基 1-拉布拉多 0-京巴


print("识别结果为:" + target[classes])
