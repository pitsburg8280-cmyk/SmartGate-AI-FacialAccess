import cv2
import os

dataset_path = "dataset"
output_path = "dataset_enhanced"

def mejorar_imagenes(path, out_path):
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    for file in os.listdir(path):
        if file.lower().endswith((".jpg", ".png")):
            img_path = os.path.join(path, file)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

            if img is None:
                print(f"[WARN] Imagen corrupta ignorada: {file}")
                continue

            # 🔧 Mejoras aplicadas
            # 1. Reducción de ruido
            img = cv2.GaussianBlur(img, (3,3), 0)
            # 2. Normalización de contraste
            img = cv2.equalizeHist(img)
            # 3. Escalado uniforme (opcional)
            img = cv2.resize(img, (200,200))

            # Guardar imagen mejorada
            out_file = os.path.join(out_path, file)
            cv2.imwrite(out_file, img)
            print(f"[INFO] Imagen mejorada guardada: {out_file}")

    print("\n✅ Mejora de imágenes completada.")

if __name__ == "__main__":
    mejorar_imagenes(dataset_path, output_path)