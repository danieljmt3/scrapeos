from bs4 import BeautifulSoup
import requests

sitioweb = 'https://www.google.com/'
respuesta = requests.get(sitioweb)
content = respuesta.text

soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())

#este codigo es para que me extraiga el html de la pagina que quiero comprobar, esto es para saber si el codigo esta funcionando de manera correcta
#si se prueba con la url de computrabajo, mostrara el error 403 (igual con los otros portales de empleo)