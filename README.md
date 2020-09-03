# Capstone-Project-Full-Stack-Dev
My Fifth project at Misk-Udactiy - Full-Stack Developer Nanodegree Program.
It's cover all these point below:
- Coding in Python 3
- Relational Database Architecture
- Modeling Data Objects with SQLAlchemy
- Internet Protocols and Communication
- Developing a Flask API
- Authentication and Access
- Authentication with Auth0
- Authentication in Flask
- Role-Based Access Control (RBAC)
- Testing Flask Applications
- Deploying Applications

## Project Description
**Casting Agency Specifications**
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

### Roles
This app has 3 roles with different permissions:
- Casting Assistant
    - Can view actors and movies
- Casting Director
    - All permissions a Casting Assistant has and…
    - Add or delete an actor from the database
    - Modify actors or movies
- Executive Producer
    - All permissions a Casting Director has and…
    - Add or delete a movie from the database

## Demo URL 
This app deploy on [herokuapp](www.herokuapp.com)
https://capstone-proj-full-stack-dev.herokuapp.com/

## Getting Started
### Installing Dependencies
**Python 3.7**

## To install and run app localy

- pip Dependencies 
```
pip3 install -r requirements.txt
```
This will install all of the required packages we selected within the requirements.txt file.

- Database Setup
```
sudo -u postgres -i
createdb capstone
```
Then run this command at the project directory
```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```
- Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
5. Create new API permissions:
    - `get:actors`
    - `get:movies`
    - `post:actor`
    - `post:movie`
    - `patch:actors`
    - `patch:movies`
    - `delete:movies`
6. Create new roles for:
    - Casting Assistant
        - can  `get:actors` and `get:movies`    
    - Casting Director
        - can `get:actors`, `get:movies`, `post:actor`, `patch:actors` and `patch:movies`    
    - Executive Producer
        - can `get:actors`, `get:movies`, `post:actor`, `patch:actors`, `patch:movies`,`post:movie` and `delete:movies`
7. Test your endpoints with [Postman](https://getpostman.com). 
    - Register 3 users - assign them to each role
    - Sign into each account and make note of the JWT.
    - Import the postman collection `capstone-proj-full-stack-dev.postman_collection.json`
    - Right-clicking the collection folder for Casting Assistant, Casting Director and Executive Producer, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
    - Run the collection and correct any errors.

- Running the server
```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
- Run test unit file
```
sudo -u postgres -i
createdb capstone_test
```
Then run this command at the project directory
```
python3 test_app.py
```
## To run app on online sever
- run test unit file
```
heroku run python test_app.py --app capstone-proj-full-stack-dev
```
- Test JWT Token 
```
find tokens for every role at setup.sh file
or 
import `capstone-proj-full-stack-dev.postman_collection.json` file to postman app
```

## Endpoints
### GET '/actors'
- To get all actors
```
{
    "actors": [
        {
            "age": 60,
            "gender": "male",
            "id": 1,
            "name": "Tom Hanks"
        },
        {
            "age": 22,
            "gender": "male",
            "id": 2,
            "name": "actor 2"
        }
    ],
    "success": true
}
```
### GET '/movies'
- To get all moives
```
{
    "movies": [
        {
            "id": 1,
            "release_date": "Tue, 22 Jan 2019 00:00:00 GMT",
            "title": "Toy Story 4"
        },
        {
            "id": 2,
            "release_date": "Sun, 01 Jan 1995 00:00:00 GMT",
            "title": "Toy Story"
        }
    ],
    "success": true
}

```
### POST '/actor'
- To add a new actor data
```
{
    "actor": {
        "age": 61,
        "gender": "male",
        "id": 14,
        "name": "Tom Hanks"
    },
    "success": true
}
```
### POST '/movie'
- To add a new movie data
```
{
    "title" : "Toy story 4",
    "release_date":"2019-1-22"
}
```
### PATCH '/actors/1'
- To add a update actor data
```
{
    "actor": {
        "age": 60,
        "gender": "male",
        "id": 1,
        "name": "Tom Hanks"
    },
    "success": true
}
```

### DELETE '/movies/1'
- To add a delet movie
```
{
    "movie_id": 1,
    "success": true
}
```

