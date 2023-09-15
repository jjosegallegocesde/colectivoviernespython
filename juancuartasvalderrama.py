print("Hello world")

import PyPDF2

def contar_palabras_en_pdf(pdf_path):
    # Abre el archivo PDF en modo lectura binaria
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        # Inicializa una variable para contar las palabras
        palabra_count = 0
        
        # Recorre todas las páginas del PDF
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            # Extrae el texto de la página
            page_text = page.extract_text()
            
            # Divide el texto en palabras
            palabras = page_text.split()
            
            # Actualiza el contador de palabras
            palabra_count += len(palabras)
    
    return palabra_count

# Ruta del archivo PDF que quieres analizar
archivo_pdf = 'C:/Users/memo9/Downloads/Sociales..pdf'

# Llama a la función para contar las palabras
total_palabras = contar_palabras_en_pdf(archivo_pdf)

# Imprime el resultado
print(f'Total de palabras en el PDF: {total_palabras}')
