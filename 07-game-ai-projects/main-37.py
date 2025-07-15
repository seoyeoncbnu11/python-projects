import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
from glob import glob

model_path = "./converted_keras/keras_model.h5"
labels_path = "./converted_keras/labels.txt"
img_list = glob("./test/*.jpg")
img_list.extend(glob("./test/*.png"))

model = tf.keras.models.load_model(model_path)

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
for img_path in img_list:
    image = Image.open(img_path)
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)
    print(prediction)

    with open(labels_path, "rt", encoding="UTF8") as f:
        readLines = f.readlines()

    if prediction[0, 0] > prediction[0, 1]:
        print(readLines)
    else:
        print(readLines[1])
