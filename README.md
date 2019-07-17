# drf-boilerplate
Api from boilerplate using python

## Features/Uses

- Using Django rest framework;

- Celery

- Redis

- Authenticate Module `Token authentication`

- Pytest

- Extends UserView to Profile

- Postgress

## Subir projeto local

1 - `git clone`

2 - Entre na pasta da aplicação `cd drf-boilerplate`

3 - Certifique-se de suas credenciais da aws e postgresSql antes de tudo no `settings/base.py` e `settings/local.py`

3 - Crie sua venv `python3.5 -m venv venv`

4 - Active evn `source venv/bin/activate`

3 - Instale o requirements `pip install -r requirements/base.txt`

4 - Rode makemigrations `python3.5 src/makemigrations.py migrate --settings=settings.local`

4 - Rode migrate `python3.5 src/manage.py migrate --settings=settings.local`

4 - Rode a aplicação `python3.5 src/manage.py runserver --settings=settings.local`

5 - Abra outro terminal verifique se tem o `REDIS` com o comando `redis-server`

6 - Caso não tenha instalado `brew install redis` ou `sudo apt-get install redis`

7 - Novamente `redis-server`

8 - Abra outro terminal e execute o `Celery` com o comando `celery -A celery_worker worker --loglevel=info`

9 - OK, por enquanto API, Redis e Celery rodando :)


## Deploy automatizado
1 - De permissão de execução para o arquivo deploy.sh `chmod +x deploy.sh`

2 - Execute `./deploy.sh`



## Deploy de máquina nova AWS

1 - Cadastre-se na AWS e crie um instancia Ubuntu

2 - Gere as chaves ssh e conecte na máquina

3 - `sudo apt-get update`

4 - `sudo apt-get install python3-pip nginx supervisor git git-core libpq-dev python-dev`

5 - Clone o projeto `git clone`

6 - Entre na pasta da aplicação `cd drf-boilerplate`

7 - Crie sua venv `python3.5 -m venv venv`

8 - Active evn `source venv/bin/activate`

9 - Instale o requirements `pip install -r requirements/base.txt`

10 - Remove default do ngix pasta `sudo rm /etc/nginx/sites-enabled/default`

11 - Cria arquivo do projeto no ngimx `sudo nano /etc/nginx/sites-available/meusite`
Com o seguinte conteudo:

```
server {
 listen 80;
 access_log /home/usuario/logs/access.log;
 error_log /home/usuario/logs/error.log;

 server_name nome-site.com.br (ip máquiba da aws);

 location / {
 proxy_pass http://127.0.0.1:8000; 

 #As proximas linhas passam o IP real para o gunicorn nao achar que sao acessos locais
 proxy_pass_header Server;
 proxy_set_header X-Forwarded-Host $server_name;
 proxy_set_header X-Real-IP $remote_addr;
 proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
 proxy_set_header Host $http_host;


 }

 location /static {
   alias /home/usuario/caminho_projeto/static/;
 }
}
```

12 - Cria link simbolico `sudo ln -s /etc/nginx/sites-available/meusite /etc/nginx/sites-enabled/meusite`

13 - Restart `sudo service nginx restart`

14 - Verifique se tem o arquivo `gunicorn_conf` na pasta do projeto 

15 - Caso tenha verifique o conteudo e se não crie `sudo nano gunicorn_conf`

Conteudo

```
bind = "127.0.0.1:8001"
logfile = "/home/ubuntu/logs/gunicorn.log"
workers = 3
```

16 - Tudo OK, só rodar `gunicorn --bind 127.0.0.1:8000 --env DJANGO_SETTINGS_MODULE=settings.production wsgi` para subir :D

17 - Acesse `http://seuip/ e vera que deu certo :D


## Comandos uteis

1 - Matar apps em determinada port: `kill -9 $(lsof -i:8000 -t) 2> /dev/null`

2 - Ver o que ta rodando em determinada porta: `sudo fuser -k 8000/tcp`


## Obs

- Não se esqueça de fazer as alterações de apontamento no `settings/base.py` e/ou `settings/production.py`

