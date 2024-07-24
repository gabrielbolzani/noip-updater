# Use uma imagem base oficial do Python
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o script principal para o diretório de trabalho
COPY main.py .

# Instala a dependência diretamente no Dockerfile
RUN pip install --no-cache-dir requests

# Define a variável de ambiente para garantir que as mensagens de log sejam mostradas no console
ENV PYTHONUNBUFFERED=1

# Define variáveis de ambiente padrão (podem ser sobrescritas ao executar o container)
ENV LOGIN=????????
ENV PASSWORD=????????
ENV HOSTNAME=????????
ENV SLEEP_TIME=600

# Comando para rodar o script
CMD ["python", "main.py"]
