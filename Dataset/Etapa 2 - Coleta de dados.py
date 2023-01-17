# Nesse notebook realizamos as requisições da API TMDB para buscar os filmes já produzidos.
# Ao final, exportamos o dataframe gerado em um arquivo CSV, para serem utilizados nas etapas seguintes.
#Manipulação de dados
import pandas as pd

#Requisição da API
import requests
from tmdbv3api import Movie, TMDb

#Tratamento do JSON
import json

tmdb = TMDb()
tmdb.api_key = 'd432f6c8a0f782815df6523ecd18dd9a'

df = pd.read_csv ("./Dataset/movies_metadata.csv")
