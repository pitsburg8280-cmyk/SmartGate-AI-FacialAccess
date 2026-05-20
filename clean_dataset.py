import os
import cv2
import hashlib

dataset_path = "dataset"

def hash_file(path):
    """Genera un hash MD5 del archivo para detectar duplicados"""
    hasher = hashlib.md5()
    with open(path, "rb") as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def limpiar_dataset(path):
    if not os.path.exists(path):
        print(f"[ERROR] No se encontró la carpeta {path}.")
        return

    hashes = set()
    eliminados = 0
    procesados = 0

    for file in os.listdir(path):
        if file.lower().endswith((".jpg", ".png")):
            file_path = os.path.join(path, file)
            try:
                # Verificar si la imagen se puede abrir
                img = cv2.imread(file_path)
                if img is None:
                    print(f"[WARN] Imagen corrupta eliminada: {file}")
                    os.remove(file_path)
                    eliminados += 1
                    continue

                # Verificar duplicados por hash
                file_hash = hash_file(file_path)
                if file_hash in hashes:
                    print(f"[WARN] Imagen duplicada eliminada: {file}")
                    os.remove(file_path)
                    eliminados += 1
                else:
                    hashes.add(file_hash)
                    procesados += 1

            except Exception as e:
                print(f"[ERROR] No se pudo procesar {file}: {e}")
                os.remove(file_path)
                eliminados += 1

    print(f"\n✅ Limpieza completada.")
    print(f"Imágenes válidas: {procesados}")
    print(f"Imágenes eliminadas: {eliminados}")

if __name__ == "__main__":
    limpiar_dataset(dataset_path)