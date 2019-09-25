# Reproduce a Celery

## Use

Start redis

```
redis-server
```

Start Flask

```
python app.py
```

Running Worker

```
python run_worker.py
```

## Result

![](https://raw.githubusercontent.com/ayuLiao/images/master/20190925094458.png)

```
python run_worker.py
Unable to execute task.
Unable to execute task.
Unable to execute task.
task info: 3c7cd8ac-7482-467b-b17c-dba2649b70ee succesfully queued
task info: 3c7cd8ac-7482-467b-b17c-dba2649b70ee succesfully queued
task info: 3c7cd8ac-7482-467b-b17c-dba2649b70ee succesfully queued
task info: 3c7cd8ac-7482-467b-b17c-dba2649b70ee succesfully queued
```

```
python app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat

 * Debugger is active!
 * Debugger PIN: 145-285-706
127.0.0.1 - - [25/Sep/2019 11:14:07] "GET / HTTP/1.1" 200 -
task: 3c7cd8ac-7482-467b-b17c-dba2649b70ee succesfully queued
127.0.0.1 - - [25/Sep/2019 11:14:11] "POST /longtask HTTP/1.1" 202 -
<task.async_result.<locals>.Info object at 0x107f50780>
127.0.0.1 - - [25/Sep/2019 11:14:11] "GET /status/3c7cd8ac-7482-467b-b17c-dba2649b70ee HTTP/1.1" 200 -
<task.async_result.<locals>.Info object at 0x107f50a20>
127.0.0.1 - - [25/Sep/2019 11:14:13] "GET /status/3c7cd8ac-7482-467b-b17c-dba2649b70ee HTTP/1.1" 200 -
```




