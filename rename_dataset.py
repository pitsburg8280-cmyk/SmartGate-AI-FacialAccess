import os

dataset_path = "dataset"

def renombrar_dataset(path, user_id=1):
    files = [f for f in os.listdir(path) if f.lower().endswith((".jpg", ".png"))]
    count = 0

    for file in files:
        count += 1
        # Nuevo nombre con formato correcto
        nuevo_nombre = f"usuario.{user_id}.{count}.jpg"
        origen = os.path.join(path, file)
        destino = os.path.join(path, nuevo_nombre)
        os.rename(origen, destino)
        print(f"[INFO] {file} → {nuevo_nombre}")

    print(f"\n✅ Renombrados {count} archivos para usuario ID={user_id}")

if __name__ == "__main__":
    if not os.path.exists(dataset_path):
        print(f"[ERROR] No se encontró la carpeta {dataset_path}.")
    else:
        user_id = input("Ingrese el ID del usuario: ")
        renombrar_dataset(dataset_path, user_id)