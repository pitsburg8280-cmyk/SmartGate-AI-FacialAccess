import cv2
import numpy as np
import os
from PIL import Image

dataset_path = "dataset"
trainer_path = "trainer.yml"

def get_images_and_labels(path):
    face_samples = []
    ids = []

    for file in os.listdir(path):
        if file.lower().endswith((".jpg", ".png")):
            img_path = os.path.join(path, file)
            pil_img = Image.open(img_path).convert('L')
            img_numpy = np.array(pil_img, 'uint8')

            # Extrae el ID del nombre (usuario.ID.n.jpg)
            try:
                id = int(file.split(".")[1])
                face_samples.append(img_numpy)
                ids.append(id)
            except Exception as e:
                print(f"[WARN] Archivo ignorado: {file} ({e})")

    return face_samples, ids

def train_model():
    print("[INFO] Iniciando entrenamiento del modelo LBPH...")
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    faces, ids = get_images_and_labels(dataset_path)
    if len(faces) == 0:
        print("[ERROR] No se encontraron imágenes válidas en dataset/")
        return

    recognizer.train(faces, np.array(ids))
    recognizer.write(trainer_path)
    print(f"[INFO] Entrenamiento completado. Modelo guardado en {trainer_path}")

if __name__ == "__main__":
    if not os.path.exists(dataset_path):
        print(f"[ERROR] No se encontró la carpeta {dataset_path}.")
    else:
        train_model()