import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3

# URL de la página a scrapear
url = 'https://quotes.toscrape.com/'

# Hacer la solicitud HTTP
response = requests.get(url)

# Crear el objeto BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar todas las citas en la página
quotes_data = []
for quote in soup.find_all('div', class_='quote'):
    quote_text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    tags = [tag.text for tag in quote.find_all('a', class_='tag')]
    title = quote.find('span', class_='text').get('title', '')  # Si existe un título
    
    # Guardar los datos en el diccionario
    quotes_data.append({
        'quote': quote_text,
        'author': author,
        'tags': ', '.join(tags),
        'title': title
    })

# Crear un DataFrame de Pandas con los datos
df = pd.DataFrame(quotes_data)

# Limpieza de los datos (si es necesario)
df['quote'] = df['quote'].str.strip()
df['author'] = df['author'].str.strip()
df['tags'] = df['tags'].str.strip()
df['title'] = df['title'].str.strip()

# Guardar los datos limpios en un archivo CSV
df.to_csv('citas_limpias.csv', index=False)

# Conexión a la base de datos SQLite (base de datos "datos")
conn = sqlite3.connect('datos.sqlite')
cursor = conn.cursor()

# Crear una tabla para almacenar las citas si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS datos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quote TEXT,
    author TEXT,
    tags TEXT,
    title TEXT
)
''')

# Insertar los datos del DataFrame en la base de datos
for index, row in df.iterrows():
    cursor.execute('''
    INSERT INTO datos (quote, author, tags, title)
    VALUES (?, ?, ?, ?)
    ''', (row['quote'], row['author'], row['tags'], row['title']))

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Scraping completado y datos guardados en datos.sqlite y citas_limpias.csv")