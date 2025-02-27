# Web Application Exercise

## Team Members

Brian Zou https://github.com/brianzou03

Jasmine Fan https://github.com/jasmine7310

Johnny Ding https://github.com/yd2960

Ray Ochotta https://github.com/SnowyOchole

## Product vision statement

We want to create an application that shortens urls for ease of access and readability.

## User stories

1. As a user, I want to be able to log in so that I can keep track of my past URLs.
2. As a user, I want to be able to log out so that I can keep my account safe.
3. As a user, I want to be able to easily copy and paste my shortened URL so that I can paste it easily  in the search bar.
4. As a user, I want to be able to view all my urls in a table so that I can keep track of them.
5. As a user, I want to be able to delete one of my urls so that I can manage them.
6. As a user, I want to be able to edit my url so that I can make changes.
7. As a user, I want to be able to change my password so that I can better protect my account.
8. As a user, I want to be able to create an account to access the website.
9. As a user, I want to be able to view urls in alphabetical order in the table.
10. As a user, I would like to temporary disable one of my links so that I can control access easily.


## Initial setup
1. Virtual environment setup
```
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies
```
pip install flask pymongo flask-login python-dotenv bcrypt
```

3. Freeze requirements
```
pip freeze > requirements.txt
```

4. MongoDB setup
```
brew tap mongodb/brew
brew install mongodb-community@6.0
brew services start mongodb-community@6.0
```

5. Launch MongoDB
```
mongosh
use url_shortener
db.createCollection("users")
db.createCollection("urls")
```

6. Update your .env
```
MONGO_URI=mongodb://localhost:27017/url_shortener
```


## How to run
```
cd url_shortener_app
python3 app.py
```

### Page is located at http://127.0.0.1:8000


## Task boards

>[Task Board Link](https://github.com/orgs/software-students-spring2025/projects/7)

## Sitemap

![Sitemap](images/webslingers_Sitemap.drawio.png)


## Wireframe
![Wireframe](images/webslingersWireframe.png)

## Clickable Prototype
>[Clickable Protoype Link](https://www.figma.com/proto/3TcJrdvhNp3ve0cc9o9UdQ/web-slingers-Wireframe?node-id=1-2&p=f&t=6lmYLB6YDQNYvoWx-1&scaling=scale-down&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=1%3A2)