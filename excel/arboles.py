import pandas as pd 
class Hospital:
    def __init__(self, nombre: str, nit: int, sede: str, municipio: str):
        self.nombre = nombre
        self.nit = nit
        self.sede = sede
        self.municipio = municipio


    def __str__(self):
        return f"Hospital: {self.nombre}, NIT: {self.nit}, Latitud: {self.sede}, Longitud: {self.municipio}"
    
    
    class Nodo:
        def __init__(self, hospital):
            self.hospital = hospital
            self.izquierda = None
            self.derecha = None
import os
#cargar el archivo csv
ruta = os.path.dirname(__file__)
print(ruta)
hospitales = pd.read_csv(os.path.join(ruta , 'Directorio_E.S.E._Hospitales_de_Antioquia_con_coordenadas_20250426.csv'), sep=',', low_memory=False)
# Elimina espacios adicionales en los nombres de las columnas
hospitales.columns = hospitales.columns.str.strip()

hospitales.rename(columns={
    'Razón Social Organización': 'nombre',
    'Número NIT': 'nit',
    'Nombre Sede': 'sede',
    'Nombre Municipio': 'municipio'  # Asegura que el nombre sea correcto
}, inplace=True)
hospitales['nit'] = hospitales['nit'].str.replace(',', '',)
hospitales['nit'] = hospitales['nit'].astype(int)







print(hospitales.head())
print(hospitales.columns)
print(hospitales['nit'])

for index, row in hospitales.iterrows():
   hospital = Hospital(
      nombre=row['nombre'],
      nit=row['nit'],
      sede=row['sede'],
      municipio=row['municipio']  # Corrige el acceso a la columna
   )
   print(hospital)
