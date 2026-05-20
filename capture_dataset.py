import cv2
import os

# 📌 Carpeta donde se guardarán las imágenes
dataset_path = "dataset"

def capture_images(user_id, num_samples=30):
    # Crear carpeta dataset si no existe
    if not os.path.exists(dataset_path):
        os.makedirs(dataset_path)

    # Inicializar cámara
    cam = cv2.VideoCapture(0)
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    print(f"[INFO] Capturando imágenes para el usuario ID={user_id}...")
    count = 0

    while True:
        ret, img = cam.read()
        if not ret:
            print("[ERROR] No se pudo acceder a la cámara.")
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            count += 1
            # Guardar imagen en formato usuario.ID.n.jpg
            file_name = f"usuario.{user_id}.{count}.jpg"
            cv2.imwrite(os.path.join(dataset_path, file_name), gray[y:y+h, x:x+w])
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

            print(f"[INFO] Imagen {count} guardada: {file_name}")

        cv2.imshow("Captura de rostros", img)

        # Presiona 'q' para salir antes de completar
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Detener cuando se alcance el número de muestras
        if count >= num_samples:
            break

    print("[INFO] Captura finalizada.")
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Cambia el ID según la persona que estés registrando
    user_id = input("Ingrese el ID del usuario: ")
    capture_images(user_id)