## 딥러닝으로 시작하는 컴퓨터 비전_CR6 프로젝트: Computer Vision Project

| 평가문항  | 상세기준 | 
| :--- | :--- | 
| 1. VGG16 모델을 구현할 수 있는가? | 이미지로 제시된 VGG16 모델을 코드로 구현하였다. | 
| 2. 다양한 방법을 사용하여 성능을 향상시켰는가? | 다양한 방법을 사용하여 accuracy 53% 이상을 달성하였다. |   
| 3. 다양한 이미지와 모델을 사용하여 Object Detection을 수행하였는가? | 제시된 이미지 외의 다른 이미지에 Object Detection을 수행하였고, 1가지 이상의 사전 학습된 모델을 사용하여 결과를 비교하였다. | 

### Image Classification task

```
# 문제 1-2. 데이터 generator 생성

image_gen_train = ImageDataGenerator(rescale=1./255,
                                     rotation_range=20,
                                     width_shift_range=0.2,
                                     height_shift_range=0.2,
                                     shear_range = 0.2,
                                     zoom_range=0.2,
                                     horizontal_flip=True,
                                     fill_mode = 'nearest')

input_layer = tf.keras.layers.Input(shape=(150, 150, 3))
x = tf.keras.layers.Conv2D(32, (3, 3), strides=1, activation='relu', padding='same')(input_layer)
x = tf.keras.layers.BatchNormalization()(x)
x = tf.keras.layers.MaxPool2D((2, 2))(x)

x = tf.keras.layers.Conv2D(64, (3, 3), strides=1, activation='relu', padding='same')(x)
x = tf.keras.layers.BatchNormalization()(x)
x = tf.keras.layers.MaxPool2D((2, 2))(x)

x = tf.keras.layers.Conv2D(128, (3, 3), strides=1, activation='relu', padding='same')(x)
x = tf.keras.layers.BatchNormalization()(x)
x = tf.keras.layers.MaxPool2D((2, 2))(x)

x = tf.keras.layers.GlobalAveragePooling2D()(x)

x = tf.keras.layers.Dropout(0.5)(x)
x = tf.keras.layers.Dense(512, activation='relu')(x)
out_layer = tf.keras.layers.Dense(1, activation='sigmoid')(x)

model = tf.keras.Model(inputs=[input_layer], outputs=[out_layer])
model.summary()

```

>ImageDataGenerator를 전체적으로 재설정하여 실험했습니다. 에폭은 5 -> 20 -> 60 -> 10 순으로 실험하였는데, 20일 경우에 성능이 그나마 가장 좋았습니다. 모델의 경우 단순화하여 디자인하였고, Flatten()을 GlobalAveragePooling2D()로 변경하였습니다. 모델 컴파일 과정에서 optimizer=RMSprop(learning_rate=1e-4)로 설정하여 실험하였으나, Adam(learning_rate=0.01)으로 설정했던 경우와 비교하면 성능의 차이가 미미했습니다. 그러나 실험 과정에서 ImageDataGenerator의 값들을 다양하게 변경하였기 때문에 단순히 옵티마이저가 변수였다고 단정하긴 어렵다고 생각합니다. 생각보다 굉장히 시간이 오래 걸렸던 테스크였지만, 모델 디자인의 중요성과 최적화에 대한 저만의 답을 찾기 위해서는 많은 연습이 필요하다고 느꼈습니다.

### Object Detection task

```
# 문제 2-2. 모델 불러오기

module_handle = "https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1"
detector = hub.load(module_handle).signatures['default'] # detector에 사용할 모듈 저장
```

>mobilenet_v2로 실험하였을 때, 앞서 inception_resnet_v2을 사용했을 때보다 시간이 매우 적게 소요되었습니다(Inference time:  1.4565761089324951). 시간이 적게 소요되어 효율적이라고 느꼈습니다. 다만, pre-trained 모듈을 조사하는 과정에서 궁금했던 부분은 특정 모듈을 import하는 과정에서 url에 google이 있는 모듈만 정상적으로 적용/테스트가 가능했습니다. 심지어 tfhub에서 "https://tfhub.dev/google"으로 검색을 하면 inception_resnet_v2와 mobilenet_v2만 조회되었습니다. 다른 하나는 위키피디아에서 제가 임의로 가져온 이미지 내에서 inception_resnet_v2 모듈로 테스트하면 컴퓨터를 레이블로 찾았지만, ssd/mobilenet_v2/1는 컴퓨터를 인지하지 못했고 정확도가 다고 낮은 것으로 나타났습니다. 어떤 차이가 있는지에 관해서 다양한 이미지를 활용하여 실험해볼 필요가 있다고 생각합니다. 또한 다른 다양한 모듈을 사용한 실험 결과가 궁금합니다.

### Retrospect

>Object Detection task를 직접 테스트해볼 수 있었던 재미있는 프로젝트였습니다. 바인딩 박스 관련 코드가 조금 이해하기 어려웠지만 전체적인 소감은 매우 유익한 퀘스트였습니다. 더 다양한 모듈을 사용하여 결과를 비교해보고 싶습니다. 프로젝트 제출 후, 이미지 분류 작업과 관련하여 성능 테스트를 다시 시도했습니다. 테스트 과정과 결과를 요약한 내용을 img_classification_recap.ipynb 으로 업데이트 했습니다.
