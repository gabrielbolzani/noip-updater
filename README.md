
#Atualizador de IP Dinâmico com Docker
Introdução
Este projeto fornece um script Python para automatizar a atualização do seu IP dinâmico no serviço de DNS do NO-IP. O script é executado em um container Docker, facilitando a instalação e o gerenciamento.

Estrutura do Projeto
O projeto é composto por dois arquivos:

main.py: Script Python responsável por obter o IP público e atualizar o serviço de DNS.
Dockerfile: Arquivo que define a construção da imagem Docker para executar o script.
Configuração
O Dockerfile inclui variáveis de ambiente padrão para o script, mas você pode personalizá-las ao executar o container. As variáveis disponíveis são:

LOGIN: Seu login no serviço de DNS.
PASSWORD: Sua senha no serviço de DNS.
HOSTNAME: O nome do host para o qual o IP deve ser atualizado.
SLEEP_TIME: Intervalo em segundos entre as atualizações de IP (padrão: 600 segundos, ou 10 minutos).
Instruções
1. Configurando o Projeto
Clone o repositório e acesse o diretório do projeto:
Bash
git clone <URL_DO_SEU_REPOSITORIO>
cd <NOME_DO_DIRETORIO>
Use o código com cuidado.

Edite o Dockerfile com um editor de texto e localize o bloco de variáveis de ambiente:
Snippet de código
# Define variáveis de ambiente padrão (podem ser sobrescritas ao executar o container)
ENV LOGIN=????
ENV PASSWORD=????
ENV HOSTNAME=????
ENV SLEEP_TIME=????
Use o código com cuidado.

Substitua "???? " pelos seus valores:
LOGIN: Seu login no serviço de DNS.
PASSWORD: Sua senha no serviço de DNS.
HOSTNAME: O nome do host para o qual o IP deve ser atualizado.
SLEEP_TIME: Intervalo em segundos entre as atualizações de IP (por exemplo, 600 para 10 minutos).
Salve o Dockerfile com as alterações.
2. Construindo a Imagem Docker
Navegue até o diretório do projeto (onde o Dockerfile e o main.py estão localizados).

Construa a imagem Docker usando o seguinte comando:

Bash
sudo docker build -t update-no-ip .
Use o código com cuidado.

3. Executando o Container Docker
Após construir a imagem, execute o container com o seguinte comando:
Bash
sudo docker run -d \
  --name update-no-ip-container \
  -e LOGIN=seu_login \
  -e PASSWORD=sua_senha \
  -e HOSTNAME=seu_hostname \
  -e SLEEP_TIME=600 \
  update-no-ip
Use o código com cuidado.

Observação:

Se você já configurou as variáveis de ambiente no Dockerfile, pode omitir a definição delas no comando acima.
Substitua seu_login, sua_senha e seu_hostname pelos seus valores reais.
4. Verificando os Logs do Container
Para verificar se o container está funcionando e visualizar seus logs, use o comando:

Bash
sudo docker logs update-no-ip-container
Use o código com cuidado.

Considerações Finais
Este script Python em um container Docker oferece uma maneira simples e automatizada de manter seu IP dinâmico atualizado em um serviço de DNS. A configuração e o gerenciamento são facilitados pelo Docker, tornando-o ideal para diversos cenários.

Lembre-se de:

Ajustar as variáveis de ambiente no Dockerfile ou no comando de execução do container de acordo com suas necessidades.
Monitorar os logs do container para garantir que o script esteja funcionando corretamente.
