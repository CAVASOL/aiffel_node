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
model.add(layers.Input(shape=(train_data.shape[1], )))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.BatchNormalization())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.BatchNormalization())
model.add(layers.Dense(1))

# 회귀(예측)을 위한 모델이므로 loss를 mse, metrics를 mae로 사용합니다.
model.compile(optimizer='adam',
              loss='mse',
              metrics=['mae'])

model.save('boston_housing_model_init')
model.summary()
```

**Reuters**

```
from tensorflow.keras import models, layers

model = models.Sequential()
model.add(layers.Dense(128, input_shape=(10000, ), name='input'))
model.add(layers.BatchNormalization())
model.add(layers.Activation('relu'))
model.add(layers.Dense(128, name='hidden'))
model.add(layers.BatchNormalization())
model.add(layers.Activation('relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(46, activation='softmax', name='output'))

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.save('reuters_model_init')
model.summary()
```

**CIFAR10**

```
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
model.add(layers.Dense(10, activation = "softmax"))

model.compile(optimizer = 'Adam',
              loss = "sparse_categorical_crossentropy",
              metrics = "accuracy")

model.save('cifar10_model_init')
model.summary()
```

### Retrospect

>각 데이터 유형에 따라 전처리를 진행하고 모델을 디자인하여 학습하는 과정이 어려웠습니다. 벅차다는 느낌이었어요. 모델 성능을 올리기 위해 Dense와 Activation 사이에 BatchNormalization()을 삽입하였고, Dropout(0.5)을 설정하였으며, 모델 학습 과정에서 check_point_cb와 early_stopping_cb을 설정한 후 삽입하였습니다. 전반적으로 최종 결과가 만족스럽지 못 하여 안타깝습니다. 각 모델에 대해 좀 더 깊이 고민하고 실험할 수 있었더라면 좋았을 거라는 아쉬움이 많이 남습니다.