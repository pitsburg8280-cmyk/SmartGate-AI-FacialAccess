import cv2
import sqlite3
import os
import time
import json
import logging
import numpy as np
from datetime import datetime

# Configuración de logging
logging.basicConfig(filename="smart_gate.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

class SmartGate:
    """Sistema de control de acceso biométrico con IA y persistencia de datos."""

    def __init__(self, config_file="config.json"):
        try:
            with open(config_file) as f:
                config = json.load(f)
        except Exception as e:
            logging.error(f"Error al cargar configuración: {e}")
            config = {
                "db_name": "smart_gate.db",
                "confidence_threshold": 70,
                "cooldown_seconds": 60,
                "cascade_path": "haarcascade_frontalface_default.xml"
            }

        self.db_name = config["db_name"]
        self.confidence_threshold = config["confidence_threshold"]
        self.cooldown_seconds = config["cooldown_seconds"]
        self.cascade_path = config["cascade_path"]

        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            self._crear_tablas()
            logging.info("Conexión a la base de datos establecida.")
        except sqlite3.Error as e:
            logging.error(f"Error al conectar con la base de datos: {e}")

        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + self.cascade_path)
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        if os.path.exists("trainer.yml"):
            self.recognizer.read("trainer.yml")
            logging.info("Modelo LBPH cargado correctamente.")
        else:
            logging.warning("No se encontró trainer.yml, el sistema funcionará en modo detección.")

        self.last_access_time = {}
        self.salir = False  # bandera para botón de salida

    def _crear_tablas(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nombre TEXT NOT NULL,
                                rostro_id INTEGER UNIQUE NOT NULL)""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS registros_acceso (
                                id_log INTEGER PRIMARY KEY AUTOINCREMENT,
                                usuario_id INTEGER,
                                fecha_hora DATETIME,
                                estado TEXT,
                                FOREIGN KEY(usuario_id) REFERENCES usuarios(id))""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS intrusos (
                                id_intruso INTEGER PRIMARY KEY AUTOINCREMENT,
                                foto_path TEXT,
                                fecha_hora DATETIME)""")
        self.conn.commit()

    def registrar_acceso(self, usuario_id, estado):
        ahora = datetime.now()
        self.cursor.execute(
            "INSERT INTO registros_acceso (usuario_id, fecha_hora, estado) VALUES (?, ?, ?)",
            (usuario_id, ahora, estado)
        )
        self.conn.commit()

    def registrar_intruso(self, foto_path):
        ahora = datetime.now()
        self.cursor.execute(
            "INSERT INTO intrusos (foto_path, fecha_hora) VALUES (?, ?)",
            (foto_path, ahora)
        )
        self.conn.commit()

    def procesar_video(self):
        cap = cv2.VideoCapture(0)
        logging.info("Sistema Smart-Gate activo...")

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

            for (x, y, w, h) in faces:
                id_pred, confidence = self.recognizer.predict(gray[y:y+h, x:x+w])

                if confidence < self.confidence_threshold:
                    nombre_usuario = f"Usuario {id_pred}"
                    color = (0, 255, 0)
                    self._intentar_log(id_pred, "Autorizado")
                else:
                    nombre_usuario = "DESCONOCIDO"
                    color = (0, 0, 255)
                    self._protocolo_intruso(frame)

                cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
                cv2.putText(frame, f"{nombre_usuario} ({int(confidence)})", (x, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

            # Dibujar botón "Salir"
            cv2.rectangle(frame, (10, 10), (100, 50), (0, 0, 255), -1)
            cv2.putText(frame, "Salir", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)

            cv2.imshow("Smart-Gate: Control de Acceso", frame)

            # Detectar tecla 'q'
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

            # Detectar clic en el botón
            cv2.setMouseCallback("Smart-Gate: Control de Acceso", self.click_event)

            if self.salir:
                break

        cap.release()
        cv2.destroyAllWindows()
        logging.info("Cámara cerrada y recursos liberados.")

    def click_event(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            if 10 <= x <= 100 and 10 <= y <= 50:
                logging.info("Botón de salida activado.")
                self.salir = True

    def _intentar_log(self, user_id, estado):
        ahora = time.time()
        if user_id not in self.last_access_time or (ahora - self.last_access_time[user_id]) > self.cooldown_seconds:
            self.registrar_acceso(user_id, estado)
            self.last_access_time[user_id] = ahora

    def _protocolo_intruso(self, frame):
        ahora = datetime.now().strftime("%Y%m%d_%H%M%S")
        foto_name = f"intruso_{ahora}.jpg"
        if not os.path.exists("intrusos"): os.makedirs("intrusos")
        path = os.path.join("intrusos", foto_name)
        cv2.imwrite(path, frame)
        self.registrar_intruso(path)

def entrenar_modelo(dataset_path="dataset", trainer_path="trainer.yml"):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    faces, ids = [], []

    for root, dirs, files in os.walk(dataset_path):
        for file in files:
            if file.endswith("jpg"):
                path = os.path.join(root, file)
                img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                try:
                    id_usuario = int(file.split(".")[1])  # formato usuario.ID.n.jpg
                    faces.append(img)
                    ids.append(id_usuario)
                except Exception as e:
                    logging.warning(f"Archivo ignorado: {file} ({e})")

    if faces:
        recognizer.train(faces, np.array(ids))
        recognizer.write(trainer_path)
        print("✅ Modelo entrenado y guardado en trainer.yml")
    else:
        print("[ERROR] No se encontraron imágenes válidas para entrenamiento.")

# --- BLOQUE MAIN ---
if __name__ == "__main__":
    gate = SmartGate()
    gate.procesar_video()