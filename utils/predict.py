from keras.models import load_model
import numpy as np


def prepare_image(img):
    img_size = 224
    image = img.resize((img_size, img_size))
    image = np.array(image).reshape(1, 224, 224, 3)
    image = image.astype("float32") / 255
    return image


def predict(img):
    labels = {
        "bacterial_spot": "Mancha Bacteriana",
        "powdery_mildew": "Oídio",
        "healthy": "Saludable",
        "tomato_mosaic_virus": "Virus del Mosaico",
        "tomato_yellow_leaf_curl_virus": "Virus del Enrollamiento de la Hoja Amarilla",
        "target_spot": "Target Spot",
        "spider_mites": "Araña Roja / Dos Puntos",
        "septoria_leaf_spot": "Mancha Foliar por Septoria",
        "leaf_mold": "Molde de la Hoja",
        "late_blight": " Tizón Tardío",
        "early_blight": "Tizón Temprano",
    }

    model = load_model("network.model")
    data = prepare_image(img)
    prediction = model.predict([data])
    prediction = prediction[0].tolist()
    label = list(labels.keys())[prediction.index(max(prediction))]
    return labels[label]
