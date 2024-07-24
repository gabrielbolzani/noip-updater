# Atualizador de IP Dinâmico com Docker

Este projeto contém um script Python que atualiza automaticamente o IP dinâmico no DNS do No-IP. O script é executado em um container Docker.

## Estrutura do Projeto

- `main.py`: Script Python que obtém o IP público e atualiza o serviço de DNS.
- `Dockerfile`: Arquivo para construir a imagem Docker.

## Configuração

O `Dockerfile` já inclui variáveis de ambiente padrão, mas você pode sobrescrevê-las ao executar o container. 

As variáveis de ambiente usadas no projeto são:

- `LOGIN`: Seu login para o serviço de DNS.
- `PASSWORD`: Sua senha para o serviço de DNS.
- `HOSTNAME`: O nome do host para o qual o IP deve ser atualizado.
- `SLEEP_TIME`: O intervalo em segundos entre atualizações de IP (padrão: 600 segundos = 10 minutos).

## Instruções

### 1. Configurar o Projeto

Clone o repositório e navegue até o diretório do projeto:

```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd <NOME_DO_DIRETORIO>
```

Abra o arquivo Dockerfile em um editor de texto e localize as seguintes linhas:
```bash
# Define variáveis de ambiente padrão (podem ser sobrescritas ao executar o container)
ENV LOGIN=????
ENV PASSWORD=????
ENV HOSTNAME=????
ENV SLEEP_TIME=????
```
