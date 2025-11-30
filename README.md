# Implantar no vercel:
- cria conta no vercel;
- dar acesso do repositório no vercel para criar o projeto e importar os programas;
- criar todas as variáveis de ambiente necessárias: SECRET_KEY, POSTGRES_DATABASE, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_DB_PORT


## Dependências:
vercel.json:

```
{
  "builds": [
    {
      "src": "_core/wsgi.py",
      "use": "@vercel/python",
      "config": { "maxLambdaSize": "15mb", "runtime": "python3.9" }
    },
    {
        "src": "build.sh",
        "use": "@vercel/static-build",
        "config": { "distDir": "static_files" }
    }
  ],
  "routes": [
    {
      "src": "/static/(.*)",
      "dest": "/static/$1"
    },
    {
      "src": "/(.*)",
      "dest": "_core/wsgi.py"
    }
  ]
}

```

requirements.txt:

```
asgiref==3.7.2
Django==4.2.10
psycopg2-binary==2.9.9
sqlparse==0.4.4
typing_extensions==4.9.0

```

build.sh:

```
#!/bin/bash

echo "**********     início     **********"


echo "**********  pip install   **********"
python3 -m pip install -r requirements.txt

echo "********** makemigrations **********"
python3 manage.py makemigrations --noinput

echo "**********    migrate     **********"
python3 manage.py migrate --noinput

echo "********** collectstatic  **********"
python3 manage.py collectstatic --noinput


echo "**********      fim       **********"

```

trocar application para app em wsgi.py e em settings.py



# Pendências:
- criar manuteção de tabela filho
- nome do usuário em telas logada
- criar menu externo
- criar função messages (que aparece mensagens em qualquer página)
- melhorar acesso a variáveis de ambiente
- globalizar classe MyContext
