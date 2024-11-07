from geopy.geocoders import Nominatim
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv('EMAIL')

def lerExecel():
    excel = pd.read_excel(io='./enderecos.xlsx', index_col=0)
    excel['LATITUDE'] = excel['LATITUDE'].astype(object)
    excel['LONGITUDE'] = excel['LONGITUDE'].astype(object)
    LINHA = 0
    
    for row in excel.itertuples(index=True, name=None):

        LINHA += 1
        endereco = f"{row[3]}, {row[5]} {row[6]},SP"
        print(endereco)

        latlong = getLatLon(endereco)
        excel.at[LINHA,'LATITUDE'] = latlong[0]
        excel.at[LINHA,'LONGITUDE'] = latlong[1]
        
    excel.to_excel("enderecos_CORRIGIDOS.xlsx")   

def getLatLon(adress):
    
    geolocator = Nominatim(user_agent=EMAIL)
    localizacao = geolocator.geocode(adress)
    
    return [localizacao.latitude, localizacao.longitude]
