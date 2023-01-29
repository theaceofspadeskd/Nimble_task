```
Треба спроєктувати та написати відмовостійкий та масштабований REST-сервіс для зберігання бінарних даних
в будь-якому хмарному сервісі (S3, Azure Blob Storage, Dropbox і тд). Доступ до даних здійснюється по ключу (key-value)

Вимоги до сервісу:
Операції put, get через REST
Синхронний запис (дані доступні через get одразу після завершення put)
Можна використовувати будь-який фреймворк, окрім Django

Намагайся використати технології якими володієш і які були б доречними на твою думку (celery, docker, redis, nginx, etc).
Мінімальне робоче рішення - це погане рішення. Також приємно було би бачити тести і документацію.
```


Run in Docker:

 Build and run container
```
docker-compose up --build
```

To run:

1. Clone repo
```
git clone https://github.com/theaceofspadeskd/Nimble_task.git
```
2. install requirements
```
pip install -r requirements.txt
```
3. Run server
```
python proj/app.py
```
4. Run tests:
```
python proj/test.py
```

App routes:

1. Method PUT - put_data

```
 http://127.0.0.1:5000/api/v1/add-data/<key>/<value>

```
   nginx in docker:
```
 http://localhost/api/v1/add-data/<key>/<value>
```

2. Method GET - get_data
```
 http://127.0.0.1:5000/api/v1/<key>
```
   nginx in docker:
```
 http://localhost/api/v1/<key>
```
  
