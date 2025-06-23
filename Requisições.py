import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()
chave_api = os.getenv("CHAVE_API")
series_id = os.getenv("SERIES_ID")

def cambio():
    try:
        req = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
        req.raise_for_status()
        dados = req.json()
        if  "USDBRL" in dados and "bid" in dados["USDBRL"]:
            dolar_real = dados["USDBRL"]["bid"]
            conversao = float(dolar_real)
            print(F'Conversão: {conversao:.2f}')
            return conversao
        else:
            return None
    except (requests.exceptions.RequestException, ValueError, KeyError):
        return None
    
def ipca():
    try:
        data_inicial = (datetime.now() - timedelta(days=365)).strftime("%d/%m/%Y")
        data_final = datetime.now().strftime("%d/%m/%Y")
        req = requests.get(f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.10844/dados?formato=json&dataInicial={data_inicial}&dataFinal={data_final}")
        req.raise_for_status()
        dados = req.json()
        inflacao_acumulada = sum(float(item["valor"]) for item in dados if "valor" in item)
        print(f"Inflação acumulada nos últimos 12 meses: {inflacao_acumulada:.2f}%")
        return inflacao_acumulada
    except (requests.exceptions.RequestException, ValueError, KeyError):
        return None
    
def inflacao_eua():
    try:
        req = requests.get(f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={chave_api}&file_type=json&sort_order=desc&limit=1")
        req.raise_for_status()
        dados = req.json()
        if "observations" in dados and len(dados["observations"]) > 0:
            inflacao_nucleo = float(dados["observations"][0]["value"])
            print(f"Núcleo da inflação atual nos EUA: {inflacao_nucleo:.2f}%")
            return inflacao_nucleo
        else:
            print("Erro, dados não encontrados")
            return None
    except (requests.exceptions.RequestException, ValueError, KeyError):
        return None
