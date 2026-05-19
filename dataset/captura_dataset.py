import cv2
import os

def capturar_imagenes(user_id, num_fotos=20, carpeta="dataset"):
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    cam = cv2.VideoCapture(0)
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    print("📸 Capturando imágenes... Presiona 'q' para salir antes de terminar.")
    contador = 0

    while True:
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rostros = detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in rostros:
            contador += 1
            nombre_archivo = f"{user_id}_usuario{contador}.jpg"
            cv2.imwrite(os.path.join(carpeta, nombre_archivo), gray[y:y+h, x:x+w])
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, f"Imagen {contador}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2)

        cv2.imshow("Captura Dataset", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        if contador >= num_fotos:
            break

    cam.release()
    cv2.destroyAllWindows()
    print(f"✅ Captura finalizada. {contador} imágenes guardadas en {carpeta}/")

if __name__ == "__main__":
    usuario_id = input("Ingrese el ID del usuario (ejemplo: 1): ")
    capturar_imagenes(usuario_id)