import os
from collections import defaultdict

dataset_path = "dataset"

def verificar_dataset(path):
    conteo = defaultdict(int)

    for file in os.listdir(path):
        if file.lower().endswith((".jpg", ".png")):
            partes = file.split(".")
            if len(partes) >= 3 and partes[1].isdigit():
                user_id = int(partes[1])
                conteo[user_id] += 1
            else:
                print(f"[WARN] Archivo ignorado: {file} (formato inválido)")

    if conteo:
        print("\n📊 Resumen del dataset:")
        for user_id, cantidad in conteo.items():
            print(f"Usuario {user_id}: {cantidad} imágenes")
    else:
        print("[ERROR] No se encontraron imágenes válidas en dataset/")

if __name__ == "__main__":
    if not os.path.exists(dataset_path):
        print(f"[ERROR] No se encontró la carpeta {dataset_path}.")
    else:
        verificar_dataset(dataset_path)