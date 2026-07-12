import os
import time

import pywhatkit as kit
import requests
from dotenv import load_dotenv

load_dotenv()

def buscar_cotacao_euro():
    url = "https://economia.awesomeapi.com.br/json/last/EUR-BRL"

    print("Conectando com o servidor de cotações...")
    resposta = requests.get(url)

    try:
        resposta.raise_for_status()   
    except requests.exceptions.HTTPError as err:
        print(err)
        return None
    
    cotacao = float(resposta.json()["EURBRL"]["bid"])

    if cotacao < 5.90:
        texto_alerta = f"ALERTA: O Euro baixou! Preço atual: R$ {cotacao:.2f}. Hora de comprar!"
        print("Condição atingida! Preparando envio de WhatsApp...")
        numero_destino = os.getenv('MEU_CELULAR')
        kit.sendwhatmsg_instantly(numero_destino, texto_alerta, wait_time=60, tab_close=True)
        print("Alerta enviado com sucesso!")
    else:
        print(f"Cotação do euro: {cotacao}")
        print("O preço do euro está alto, Esperar baixar o preço!")
    

if __name__ == "__main__":
    buscar_cotacao_euro()
