from bs4 import BeautifulSoup
import requests
import sys


matricula = sys.argv[1]
url = 'https://sede.dgt.gob.es/es/vehiculos/distintivo-ambiental/?accion=1&matriculahd=&matricula='+matricula+'&submit=Consultar'

r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, 'html.parser')
mensaje_resultado = soup.find('div', {'class': 'mensajeResultadoConImagen'})
etiqueta_ambiental = mensaje_resultado.find('strong').text.split('Etiqueta Ambiental ')
etiqueta = etiqueta_ambiental[1].rstrip('.')

print (etiqueta)
