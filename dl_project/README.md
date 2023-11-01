### 딥러닝 한 번에 끝내기_CR6 프로젝트: 딥러닝 프로젝트

| 평가문항  | 상세기준 | 
| :--- | :--- | 
| 1. Boston 주택 가격 예측 프로젝트를 성공적으로 완료하였는가? | 프로젝트의 지시 사항을 따라 데이터 전처리, 모델 구성, 모델 학습을 올바르게 진행하였다. | 
| 2. Reuters 데이터의 분류 프로젝트를 성공적으로 완료하였는가? | 프로젝트의 지시 사항을 따라 데이터 전처리, 모델 구성, 모델 학습을 올바르게 진행하였다. |   
| 3. CIFAR10 데이터의 분류 프로젝트를 성공적으로 완료하였는가? | 프로젝트의 지시 사항을 따라 데이터 전처리, 모델 구성, 모델 학습을 올바르게 진행하였다. | 

### 각 프로젝트의 모델 구성

**Boston Housing**

```
from tensorflow.keras import models, layers

# input_shape은 (train_data.shape[1], )으로 구성합니다.
model = models.Sequential()
model.add(layers.Dense(64, input_shape=(train_data.shape[1], ), activation='relu'))

# model.add(layers.BatchNormalization())
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(1))

# 회귀(예측)을 위한 모델이므로 loss를 mse, metrics를 mae로 사용합니다.
model.compile(optimizer='adam',
              loss='mse',
              metrics=['mae'])

# model.save('boston_housing_model_init')
model.summary()
```

>중간에 삽입했던 BatchNormalization()을 삭제하고, model.save()을 주석 처리했다. 시각화하여 그래프로 확인하였을 때 초기 테스트에 비하면 학습이 안정적으로 이뤄진 것을 확인할 수 있다. 

**Reuters**

```
from tensorflow.keras import models, layers

model = models.Sequential()
model.add(layers.Dense(128, input_shape=(10000, ), name='input'))
model.add(layers.BatchNormalization())
model.add(layers.Activation('relu'))
model.add(layers.Dense(128, name='hidden'))
# model.add(layers.BatchNormalization())
# model.add(layers.Activation('relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(46, activation='softmax', name='output'))

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# model.save('reuters_model_init')
model.summary()
```

>중간에 삽입되어 있었던 BatchNormalization()와 Activation('relu')를 주석처리하여 모델을 단순하게 변형했다. Boston Housing Project의 경우처럼 model.save()를 주석 처리한 후 학습을 실행하였다. 이전 테스트에 비해 모델의 성능이 향상되었고, 결과값은 80% 정도로 나타났다.

**CIFAR10**

```
# Dence Layer

import tensorflow as tf
from tensorflow.keras import layers, models

model = models.Sequential()
model.add(layers.Dense(2048, input_shape =(32 * 32 * 3, )))
model.add(layers.BatchNormalization())
model.add(layers.Activation("relu"))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(1024))
model.add(layers.BatchNormalization())
model.add(layers.Activation("relu"))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(512))
model.add(layers.BatchNormalization())
model.add(layers.Activation("relu"))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(10, activation = "softmax"))

model.compile(optimizer = 'Adam',
              loss = "sparse_categorical_crossentropy",
              metrics = "accuracy")

# model.save('cifar10_model_init')
model.summary()

```

>CIFAR10 데이터에 대한 CNN 사용과 결과를 비교하기 위해 기존의 모델 구성을 대부분 유지했고, model.save()를 주석 처리했다. 

```
# CNN

import keras
import tensorflow as tf
from tensorflow.keras import layers, models

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), padding='same', input_shape=(32, 32, 3 )))
model.add(layers.BatchNormalization())
model.add(layers.Activation("relu"))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))

model.add(layers.Conv2D(32, (3, 3), padding='same'))
model.add(layers.BatchNormalization())
model.add(layers.Activation("relu"))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))

model.add(layers.Conv2D(32, (3, 3), padding='same'))
model.add(layers.BatchNormalization())
model.add(layers.Activation("relu"))

model.add(layers.Flatten())
model.add(layers.Dense(128))

model.add(layers.BatchNormalization())
model.add(layers.Activation("relu"))
model.add(layers.Dense(64))

model.add(layers.BatchNormalization())
model.add(layers.Activation("relu"))

model.add(layers.Dropout(0.5))
model.add(layers.Dense(10, activation="softmax"))

model.compile(optimizer = 'Adam',
              loss = "sparse_categorical_crossentropy",
              metrics = ["accuracy"])

# model.save('cifar10_cnn_model_init')
model.summary()
```

>Dence Layer를 사용한 모델 구성에 비해 전체적인 모델 구성이 다소 복잡해 보일 수 있지만, 이전 모델과 달라진 점은 Dense() 사이에 BatchNormalization()을 촘촘히 추가하였고, model.save()를 주석 처리했다. 시각화하여 그래프로 확인하였을 때 기존의 모델에 비해 학습이 안정적으로 이뤄진 것을 확인할 수 있으며, Dence Layer를 사용하여 모델을 구성한 경우보다 최종 결과값이 상승(0.5281 -> 0.7358)하였다.

### Retrospect

>각 데이터 유형에 따라 전처리를 진행하고 모델을 디자인하여 학습하는 과정이 어려웠습니다. 벅차다는 느낌이었어요. 하지만 이미지 데이터와 텍스트 데이터 즉, 데이터 유형에 따라 어떤 모델화가 필요한지 실습할 수 있었으며, 안정적이고 효율적인 학습 진행을 위해 다각도로 모델 최적화를 시도해볼 수 있었던 유익한 프로젝트였습니다.