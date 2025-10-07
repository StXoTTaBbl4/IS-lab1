# Secure API — учебный проект

## Описание
REST API на Flask для ЛР1 по предмету 'Информационная безопасность' с аутентификацией через JWT, хранением данных в SQLite, мерами защиты от OWASP Top 10 и интеграцией security-сканеров в CI.

## Эндпоинты
- `POST /auth/register` — регистрация (json: {"username":"...","password":"..."})
- `POST /auth/login` — получение JWT (json: {"username":"...","password":"..."})
- `GET /api/data` — защищённый эндпоинт, требует заголовок `Authorization: Bearer <token>`

## Запуск
```bash
python -m venv venv
source venv/bin/activate
venv\Scripts\activate
pip install -r req.txt
export FLASK_APP=app.py
export FLASK_ENV=development
export SECRET_KEY="change_me_harder"
flask run
```

curl -X POST http://127.0.0.1:5000/auth/register ^ -H "Content-Type: application/json" ^ -d "{\"username\":\"user1\",\"password\":\"secret\"}"

curl -X POST http://localhost:5000/auth/login ^ -H "Content-Type: application/json" -d "{\"username\":\"user1\",\"password\":\"secret\"}"

curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjEsInVzZXJuYW1lIjoidXNlcjEiLCJleHAiOjE3NTk4NTY0MjV9.iovstcdeCJY33snyN37EsNasLGFg8tLR_7to2tUaNgs" http://localhost:5000/api/data
