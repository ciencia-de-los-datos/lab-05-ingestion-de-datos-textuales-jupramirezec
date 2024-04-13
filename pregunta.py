"""
Laboratorio ingestion de datos textuales
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import os
import csv
import pandas as pd

def creaset():
    # Rutas de los directorios de las carpetas
    paths = ["/train/", "/test/"]
    # Nombres de los archivos de salida CSV para los datos
    output_files = ["train_dataset.csv", "test_dataset.csv"]
    # Categorías de sentimientos (negative, positive, neutral)
    categories = ["negative", "positive", "neutral"]
    
   
    # Itera sobre la enumeración de los nombres de archivos de salida
    for index, file_name in enumerate(output_files):
        # Abre el archivo CSV en modo de escritura y crea un escritor CSV
        with open(file_name, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            # Escribe una fila de encabezado con los nombres de columna "phrase" y "sentiment"
            csv_writer.writerow(["phrase", "sentiment"])
        # Itera sobre cada categoría en las categorías de sentimientos
        for category in categories:
            # Construye la ruta completa al directorio de la categoría actual
            folder_path = "data" + paths[index] + category
            print("Processing files in:", folder_path)  # Depuración
            # Abre el archivo CSV en modo de adjuntar para agregar datos adicionales
            with open(output_files[index], "a", newline="") as csv_file:
                csv_writer = csv.writer(csv_file)
                # Itera sobre cada archivo en el directorio de la categoría actual
                for file in os.listdir(folder_path):
                    # Verifica si el archivo tiene la extensión .txt
                    if file.endswith(".txt"):
                        # Construye la ruta completa al archivo de texto actual
                        file_path = os.path.join(folder_path, file)
                        try:
                            # Abre el archivo de texto y lee su contenido
                            with open(file_path, "r") as text_file:
                                content = text_file.read()
                                # Escribe una nueva fila en el archivo CSV con el contenido del archivo de texto y la categoría actual
                                csv_writer.writerow([content, category])
                        except Exception as e:
                            print("Error reading file:", file_path)
                            print(e)

creaset()
