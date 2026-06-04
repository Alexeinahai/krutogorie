# ОАО «Крутогорье-Петковичи» — Сайт

FastAPI + Jinja2. Заявки отправляются на почту через SMTP.

## Структура проекта

```
krutogorie/
├── main.py              # Точка входа, FastAPI app
├── config.py            # ⚙️  ВСЕ НАСТРОЙКИ ЗДЕСЬ
├── email_utils.py       # Отправка почты
├── auth_utils.py        # Утилиты авторизации
├── requirements.txt
├── routers/
│   ├── pages.py         # Все страницы (контент вакансий, новостей — тут)
│   ├── auth.py          # Вход / выход
│   └── contact.py       # Обработка форм
├── templates/
│   ├── base.html        # Базовый шаблон (навбар, футер)
│   ├── index.html       # Главная
│   ├── about.html       # О предприятии
│   ├── products.html    # Продукция
│   ├── vacancies.html   # Вакансии
│   ├── news.html        # Новости
│   ├── contacts.html    # Контакты + карта
│   ├── login.html       # Вход в кабинет
│   └── admin.html       # Личный кабинет
└── static/
    └── css/style.css    # Стили
```

## Установка и запуск

```bash
# 1. Клонируй / распакуй проект
cd krutogorie

# 2. Создай виртуальное окружение
python -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\Scripts\activate         # Windows

# 3. Установи зависимости
pip install -r requirements.txt

# 4. Заполни config.py:
#    - SMTP_USER, SMTP_PASS, EMAIL_TO
#    - ADMIN_PASSWORD
#    - SITE_PHONE, SITE_EMAIL

# 5. Запуск
python main.py
# Сайт: http://localhost:8000
# Кабинет: http://localhost:8000/admin  (логин: admin)
```

## Настройка почты

### Gmail
1. Google Аккаунт → Безопасность → Двухэтапная аутентификация (включить)
2. Безопасность → Пароли приложений → Создать пароль для «Почта»
3. Вставить пароль в `SMTP_PASS` в `config.py`

### Mail.ru / Яндекс
- Аналогично — создать пароль приложения в настройках почты
- Изменить `SMTP_HOST` и `SMTP_PORT` соответственно:
  - Mail.ru:  `smtp.mail.ru`, порт `587`
  - Яндекс:   `smtp.yandex.ru`, порт `587`
  - tut.by:   `smtp.tut.by`, порт `465` (SSL)

## Добавление вакансий / новостей

Открой `routers/pages.py` — там списки `jobs` и `articles`.  
Просто добавь новый элемент по образцу.

## Деплой на сервер (пример с Nginx)

```bash
# 1. Установи gunicorn
pip install gunicorn

# 2. Запуск через gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

# 3. Nginx конфиг (/etc/nginx/sites-available/krutogorie):
# server {
#     listen 80;
#     server_name krytogorye-petkovichi.by;
#     location / {
#         proxy_pass http://127.0.0.1:8000;
#         proxy_set_header Host $host;
#         proxy_set_header X-Real-IP $remote_addr;
#     }
# }
```
