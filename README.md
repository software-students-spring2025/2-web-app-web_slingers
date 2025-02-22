# Web Application Exercise

A little exercise to build a web application following an agile development process. See the [instructions](instructions.md) for more detail.

## Product vision statement

See instructions. Delete this line and place the Product Vision Statement here.

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

[User Stories link]()

## Initial setup

See instructions. Delete this line and place instructions to download, configure, and run the software here.

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

### Page is located at http://127.0.0.1:5000


## Task boards

See instructions. Delete this line and place a link to the task boards here.

[Task Board](https://github.com/orgs/software-students-spring2025/projects/7)