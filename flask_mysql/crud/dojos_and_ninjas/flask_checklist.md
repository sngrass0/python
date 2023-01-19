# Flask Full Stack App Checklist

- [x] make ERD
  
- [x] forward engineer
- [x] create a virtual environment
``` bash
pipenv install PyMySQL flask
```
- [x] activate VE
``` bash
pipenv shell
```
- [x] create a app directory [flask_app](./flask_app/__init__.py)
- [x] create [server.py](server.py)
  
- [x] create a templates directory with my html [files](./flask_app/templates/index.html)
- [x] to add styling add [static](./flask_app/static/css/style.css)
- [x] create [mysqlconnection.py](./flask_app/config/mysqlconnection.py)
- [x] create our model(s) [dojo.py](./flask_app/models/dojo.py)
- [x] create our model(s) [ninja.py](./flask_app/models/ninja.py)
- [x] create our controller(s) [dojos.py](./flask_app/controllers/dojos.py)
- [x] create our controller(s) [ninjas.py](./flask_app/controllers/ninjas.py)

## run server
``` bash
python3 server.py
```



