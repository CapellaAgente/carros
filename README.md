# Gestão de Carros

### Sobre
O projeto consiste em uma aplicação web para uma loja de carros/concessionária, que visa no cadastramento de carros que estarão à venda, edição e remoção dos mesmos, bem como cadastro e login de usuários ao site.
Projeto feito no curso [Django Master](https://pycodebr.com.br/) do Felipe Azambuja/[PycodeBR](https://github.com/pycodebr)

### Instalação

Para baixar a aplicação, execute o comando abaixo em seu terminal:

```bash
git clone https://github.com/CapellaAgente/carros.git
```

Feito isso, crie um ambiente virtual Python no local da aplicação e ative-o:

##### Windows
```bash
py -m venv venv
.\venv\Scripts\activate
```
##### Linux
```bash
python3 -m venv venv
source venv/bin/activate
```
Agora instale as dependências requeridas com o comando:

```bash
pip install -r requirements.txt
```
Faça as migrações necessárias para o banco de dados:

```bash
py manage.py makemigrations
py manage.py migrate
```

Crie um super usuário para privilégios administrativos:

```bash
py manage.py createsuperuser
```
Informe um nome de usuário, email (opcional) e senha.

Finalmente, execute a aplicação com o comando:

```bash
py manage.py runserver
```

Irá aparecer uma mensagem com o endereço IP local para acesso:

```bash
#Página inicial
http://127.0.0.1:8000/cars

#Página administrativa
http://127.0.0.1:8000/admin
```

### Google Gemini

A aplicação utiliza o Google Gemini para criação de descrição dos carros.

Para conseguir habilitar o recurso, acesse o [Google AI Studio](https://aistudio.google.com/app/apikey?hl=pt-br) e crie uma chave API "Generative Language Client".

Copie e cole a chave indicado no arquivo em "google_api/client.py"

Na hora de cadastrar um carro, deixe a descrição em branco e a IA automaticamente criará uma para você!