# book_your_book

# book_your_book
#### INITIAL CONFIGURATIONS

```python
apt install python3.8-venv

python3 -m venv venv
source venv/bin/activate

pip3 install django pillow

django-admin startproject unity_books .
python3 manage.py runserver
```
The runserver command executes the function execute_from_command_line(sys.argv) present at manage.py
Browse
http://localhost:8000/

#### Settings
vamos fazer como ele esta fazendo e depois vou mudar 
para postgres, internacionalizar
https://testdriven.io/blog/multiple-languages-in-django/
language_code 'en-us'
timezone 'UTC'

sqlite 
pt-BR

## INICIANDO AS APLICACAOES
 Cadastrar livros
python3 manage.py startapp books




#### REQUIREMENTS
