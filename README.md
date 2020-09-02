# Capstone-Project-Full-Stack-Dev
My Fifth project at Misk-Udactiy - Full-Stack Developer Nanodegree Program

## Demo URL 
https://capstone-proj-full-stack-dev.herokuapp.com/

## Getting Started
**Python 3.7**

### To install and run app localy

- pip Dependencies 
```
pip3 install -r requirements.txt
```
This will install all of the required packages we selected within the requirements.txt file.

- Running the server
```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
- run test unit file
```
python3 test_app.py
```
### To run app on sever
- run test unit file
```
heroku run python test_app.py --app capstone-proj-full-stack-dev
```
- Test JWT Token 
```
find tokens for every role at setup.sh file
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
