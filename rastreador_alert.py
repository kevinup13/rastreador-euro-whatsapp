import os

import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

def buscar_cotacao_euro():
    url = "https://economia.awesomeapi.com.br/json/last/EUR-BRL"
    resposta = requests.get(url)

    try:
        resposta.raise_for_status()   
    except requests.exceptions.HTTPError as err:
        print(err)
        return None
    
    cotacao = float(resposta.json()["EURBRL"]["bid"])

    if cotacao < 5.90:
        texto_alerta = f"ALERTA: O Euro baixou! Preço atual: R$ {cotacao:.2f}. Hora de comprar!"
        print("Condição atingida! Disparando requisiçao para a API da Twilio...")
        
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        client = Client(account_sid, auth_token)

        mensagem = client.messages.create(
            from_='whatsapp:+14155238886',
            body=texto_alerta,
            to='whatsapp:+559281274551'
        )
        print(f"Alerta enviado silenciosamente! ID da mensagem: {mensagem.sid}")

    else:
        print(f"Cotação do euro: {cotacao}")
        print("O preço do euro está alto, Esperar baixar o preço!")
    

if __name__ == "__main__":
    buscar_cotacao_euro()