import csv
import os
import zipfile

def crear_set_entrenamiento_testeo():
    # Descomprimir el archivo 'data.zip'
    with zipfile.ZipFile('data.zip', 'r') as zip_ref:
        zip_ref.extractall()

    # Definir las rutas de los directorios de entrenamiento y prueba
    train_dir = './train/'
    test_dir = './test/'
    output_dir = './'

    # Lista de categorías
    categories = ["negative", "positive", "neutral"]

    # Función auxiliar para escribir en el archivo CSV
    def write_to_csv(file_path, content, category):
        with open(file_path, "a", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([content, category])

    # Iterar sobre los directorios de entrenamiento y prueba
    for directory in [train_dir, test_dir]:
        output_file = "train_dataset.csv" if directory == train_dir else "test_dataset.csv"
        output_file = os.path.join(output_dir, output_file)

        # Escribir encabezados en el archivo CSV
        with open(output_file, "w", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["phrase", "sentiment"])

        # Iterar sobre las categorías y los archivos de texto
        for category in categories:
            folder_path = os.path.join(directory, category)
            for file_name in os.listdir(folder_path):
                if file_name.endswith(".txt"):
                    file_path = os.path.join(folder_path, file_name)
                    with open(file_path, "r", encoding="utf-8") as text_file:
                        content = text_file.read()
                        write_to_csv(output_file, content, category)

# Llamar al método para crear los conjuntos de entrenamiento y prueba
crear_set_entrenamiento_testeo()
