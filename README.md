# 💈 Barbearia FitPower — Sistema de Agendamento e Lista de Espera

## 📌 Sobre o Projeto

O **Barbearia FitPower** é um sistema web desenvolvido com **Django + HTML + CSS (Bootstrap)** que permite:

* Exibir serviços (barbearia/academia)
* Criar uma **lista de espera online**
* Permitir que clientes entrem na fila
* Permitir que o administrador finalize atendimentos
* Exibir status em tempo real (com atualização automática)
* Integração direta com WhatsApp

---

## 🚀 Funcionalidades

### 👤 Cliente

* Visualizar serviços disponíveis
* Entrar na lista de espera
* Acompanhar status da fila
* Interface simples e responsiva

### 🔐 Administrador

* Login seguro
* Visualizar lista completa
* Finalizar atendimentos
* Atualizar status dos clientes

---

## 🧠 Tecnologias Utilizadas

* **Python 3**
* **Django 5**
* **HTML5**
* **CSS3**
* **Bootstrap 5**
* **Widget Tweaks (Django)**
* **SQLite (dev) / PostgreSQL (produção)**
* **Gunicorn (deploy)**

---

## 📁 Estrutura do Projeto

```
barbearia/
│
├── agenda/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── lista.html
│       └── login.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── img/
│
├── barbearia/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── Procfile
```

---

## ⚙️ Instalação Local

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/barbearia.git
cd barbearia
```

### 2. Crie o ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 🗄️ Banco de Dados

### Rodar migrações:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Criar superusuário:

```bash
python manage.py createsuperuser
```

---

## ▶️ Executar o Projeto

```bash
python manage.py runserver
```

Acesse:

```
http://127.0.0.1:8000/
```

---

## 🔐 Autenticação

* Login disponível em:

```
/login/
```

* Apenas usuários **admin (superuser)** podem:

  * Ver lista protegida
  * Finalizar clientes

---

## 📋 Funcionalidade da Lista

* Clientes entram na fila
* Status inicial: **Aguardando**
* Admin pode marcar como **Finalizado**
* Quando finalizado:

  * Nome aparece riscado
  * Status muda visualmente

---

## 🔄 Atualização Automática

A página da lista atualiza automaticamente a cada 10 segundos:

```javascript
setInterval(() => location.reload(), 10000);
```

---

## 📱 Integração com WhatsApp

Botão direto para contato:

```html
<a href="https://wa.me/5599999999999" target="_blank">
```

Com mensagem automática:

```
Olá! Gostaria de agendar um horário.
```

---

## 🌐 Deploy (Render)

### Arquivos necessários:

**requirements.txt**

```bash
pip freeze > requirements.txt
```

**Procfile**

```
web: gunicorn barbearia.wsgi:application
```

---

### Configurações importantes no `settings.py`:

```python
DEBUG = False

ALLOWED_HOSTS = ['.onrender.com']

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

---

### Banco PostgreSQL

Instalar:

```bash
pip install dj-database-url psycopg2-binary
```

Configurar:

```python
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite3')
}
```

---

## 🧪 Testes

* Testar login
* Testar criação de cliente
* Testar finalização
* Verificar atualização da lista

---

## 🎨 Interface

* Design responsivo
* Bootstrap 5
* Animações leves
* Navbar com login/logout
* Botões intuitivos

---

## 🔒 Segurança

* Rotas protegidas com `@login_required`
* Ações administrativas restritas a `is_superuser`
* CSRF habilitado

---

## 📌 Melhorias Futuras

* Atualização em tempo real com AJAX/WebSocket
* Notificação via WhatsApp automática
* Painel administrativo avançado (dashboard)
* Filtros por data/serviço
* Sistema de senhas (tipo painel de atendimento)

---

## 👨‍💻 Autor

Desenvolvido por **Cleyton Durans**

---

## 📄 Licença

Este projeto é de uso livre para fins de estudo e desenvolvimento.

---

## 💬 Observação Final

Este projeto foi pensado para ser:

✔ Simples de usar
✔ Fácil de adaptar
✔ Pronto para produção
✔ Escalável

---

🔥 Se quiser evoluir esse sistema (app mobile, API, dashboard profissional), é totalmente possível expandir a partir dessa base.
