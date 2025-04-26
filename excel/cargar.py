import pandas as pd
import os
# obtener ruta del archivo 
ruta = os.path.dirname(__file__)
print(ruta)
df = pd.read_csv(os.path.join(ruta , 'Poblaci_n_atendida_en_el_Hospital_General_de_Medell_n_20250426.csv'), sep=',', low_memory=False)
print(df.head())