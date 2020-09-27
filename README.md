## connect 4 api

### Tech used
- Django
- django-rest-framework

### endpoints
- /api/moves [GET] - gives all moves for particular session
- /api/ [POST] - takes request for moves and restart game, give error of invalid moves


### features
- Parallel games are possible from different UI (postman, Chrome, IncognitoChrome, different, browser) because data is being saved in session variables.
- Reset game 

### local setup steps
- install all packages by - `pip install -r requirements.txt` on python > 3.7 
- then cd to project - `python manage.py runserver`