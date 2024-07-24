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
Substitua ???? pelos valores apropriados:

LOGIN: Seu login para o serviço de DNS.
PASSWORD: Sua senha para o serviço de DNS.
HOSTNAME: O nome do host para o qual o IP deve ser atualizado.
SLEEP_TIME: O intervalo em segundos entre atualizações de IP (por exemplo, 600 para 10 minutos).

Depois de modificar, o bloco deve ficar assim:
```bash
# Define variáveis de ambiente padrão (podem ser sobrescritas ao executar o container)
ENV LOGIN=seu_login
ENV PASSWORD=sua_senha
ENV HOSTNAME=seu_hostname
ENV SLEEP_TIME=600
```

### 2. Construir a Imagem Docker
Navegue até o diretório onde o Dockerfile e o main.py estão localizados. Em seguida, construa a imagem Docker com o comando:
```bash
sudo docker build -t update-no-ip .
```

### 3. Executar o Container Docker
Depois de construir a imagem, você pode executar o container. Use o comando abaixo, substituindo as variáveis de ambiente se necessário. Caso tenha configurado o Dockerfile com os valores padrões, você pode usar este comando diretamente:
```bash
sudo docker run -d \
  --name update-no-ip-container \
  -e LOGIN=seu_login \
  -e PASSWORD=sua_senha \
  -e HOSTNAME=seu_hostname \
  -e SLEEP_TIME=600 \
  update-no-ip

```
Se você já configurou as variáveis diretamente no Dockerfile, pode usar o comando sem definir as variáveis de ambiente:
```bash
sudo docker run -d --name update-no-ip-container update-no-ip
```

### 4. Verificar os Logs do Container
Para verificar se o container está funcionando corretamente e para visualizar os logs, use:
```bash
sudo docker logs update-no-ip-container
```











