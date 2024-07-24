import requests
import time
import logging
import os

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Leitura das variáveis de ambiente
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
HOSTNAME = os.getenv('HOSTNAME')
SLEEP_TIME = int(os.getenv('SLEEP_TIME', 600))  # Tempo de sleep em segundos (10 minutos)


def get_public_ip():
    """
    Obtém o IP público atual usando o serviço ipify.
    """
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()  # Levanta exceção para erros HTTP
        ip_info = response.json()
        return ip_info['ip']
    except requests.RequestException as e:
        logging.error(f"Erro ao obter o IP: {e}")
        return None


def update_no_ip(ip):
    """
    Atualiza o IP dinâmico no No-IP usando a URL fornecida.
    """
    try:
        url = f'http://{LOGIN}:{PASSWORD}@dynupdate.no-ip.com/nic/update?hostname={HOSTNAME}&myip={ip}'
        response = requests.get(url)
        response.raise_for_status()  # Levanta exceção para erros HTTP
        logging.info(f"Resposta do No-IP: {response.text}")
    except requests.RequestException as e:
        logging.error(f"Erro ao atualizar o No-IP: {e}")


if __name__ == "__main__":
    while True:
        public_ip = get_public_ip()
        if public_ip:
            logging.info(f"Seu IP público é: {public_ip}")
            update_no_ip(public_ip)
        else:
            logging.error("Não foi possível obter o IP público.")

        # Loga a mensagem e espera o tempo configurado antes de repetir
        logging.info("Dormindo por %d minutos", SLEEP_TIME / 60)
        time.sleep(SLEEP_TIME)
