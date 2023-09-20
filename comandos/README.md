
Iniciar o projeto Django
```
python -m venv venv -> criando ambiente virtual
. venv/bin/activate  ->ativando ambiente virtual no mac
./venv/Scripts/activate ->ativando ambiente virtual no wind
pip install django -> instalar django
django-admin startproject project .  ->criar projeto django
python manage.py runserver  -> rodar projeto django
python manage.py startapp contact
``` 

Migrando a base de dados do Django
```
python manage.py makemigrations
python manage.py migrate
```

Criando e modificando a senha de um super usuário Django
```
python manage.py createsuperuser
python manage.py changepassword USERNAME
```
usuario josenatal
senha padrao


```
# Importe o módulo
from contact.models import Contact
# Cria um contato (Lazy)
# Retorna o contato
contact = Contact(**fields)
contact.save()
# Cria um contato (Não lazy)
# Retorna o contato
contact = Contact.objects.create(**fields)
# Seleciona um contato com id 10
# Retorna o contato
contact = Contact.objects.get(pk=10)
# Edita um contato
# Retorna o contato
contact.field_name1 = 'Novo valor 1'
contact.field_name2 = 'Novo valor 2'
contact.save()
# Apaga um contato
# Depende da base de dados, geralmente retorna o número
# de valores manipulados na base de dados
contact.delete()
# Seleciona todos os contatos ordenando por id DESC
# Retorna QuerySet[]
contacts = Contact.objects.all().order_by('-id')
# Seleciona contatos usando filtros
# Retorna QuerySet[]
contacts = Contact.objects.filter(**filters).order_by('-id')
```


