# env
OS: ubuntu 17.04
python: 2.7.13
celery: 4.1.0
redis-server: 3.2.1

# packages need to install
1. sudo pip install celery
2. sudo pip install redis
3. sudo apt install redis-server

# command
1. start celery
celery -A celery_pro worker --app=celery_pro.celery_test:app --loglevel=debug
```shell
-- celery_pro is the directory
-- celery_test is the script to define some celery parameter
-- app is Celery() instance
```
2. start schedule celery task

-- start celery server
```shell
celery -A celery_pro worker --app=celery_pro.celery_test:app --loglevel=debug
```
-- start celery client
```shell
celery -A celery_pro.periodic_tasks beat --loglevel=debug
```

# demo 
![celery schedule demo]()

# ref
http://www.cnblogs.com/luhuajun/p/7488363.html


