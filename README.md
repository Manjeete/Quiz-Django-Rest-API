# Quiz-Django-Rest-API
This is an API for multiple-choice questions. Where You can GET, POST, PUT, PATCH, and DELETE your quiz and its question.


## Steps that You can do in this Rest API

- **User Register**
- **User Login**
- **Getting List Data**
- **Post You Quizs, Questions and, Answers**
- **Retrieve, Update, and Delete single Quiz**
- **User's own Quiz**

## User Register
User can register using the following Endpoint and own data

```python
Register Endpoint (Only Post Request)

https://quizrestapi.herokuapp.com/api/auth/register/
```
```javascript
data : {
    
	"username":"<username>",
	"email":"<user_email>",
	"password":"<password>",
	"password2":"<password>"
}

```
After sending POST request user will  receive the following response :
```javascript
{
    "username": "<username>",
    "email": "<user_email>",
    "token": "<user_token>",
    "expires": "2020-06-09T11:41:41.268925Z",
    "message": "Thank You for registering. Please verifying your email before continuing !"
}

```
Here the user is receiving a token that will use when they try to post data.

## User Login
If the user is already registered  and has a username and password then can log in using the following endpoint and data:

```python
Login Endpoint (Only Post Request)

https://quizrestapi.herokuapp.com/api/auth/
```
```javascript
data : {
    
	"username":"<username>",
	"password":"<password>",
}
```
```javascript
Response:
{
    "token": "<user_token>",
    "user":"<user_name",
    "expires": "2020-06-09T11:41:41.268925Z"
}

```
Getting token after login and register is used to post the data. This token is going to pass in **headers** for **authorization** purposes.

## Getting List Data
To retrieve a list of data, It is not necessary to login or register. Login is required to changes the data.
```python
GET Request
List Retrieve Endpoint

https://quizrestapi.herokuapp.com/api/mcq/

```
```javascript
Response:
[
    {
        "id": 1,
        "user": 2,
        "name": "GK",
        "questions_count": 10,
        "created": "2020-06-02T14:11:28.467741Z",
        "description": "A quiz is a form of game or mind sport, attempt to answer questions correctly. It is a game to test ... Views. Read · Edit · View history ...",
        "questions": [
            {
                "id": 1,
                "label": "Where is 'India Gate' ?",
                "order": 1,
                "answers": [
                    {
                        "id": 1,
                        "text": "Banglore",
                        "is_correct": false
                    },
                    {
                        "id": 2,
                        "text": "Punjab",
                        "is_correct": false
                    },
                    {
                        "id": 3,
                        "text": "Mumbai",
                        "is_correct": false
                    },
                    {
                        "id": 4,
                        "text": "Delhi",
                        "is_correct": true
                    }
                ]
            }
        ]
    }
]

```
### Details of fields

**```id```**
Id of the quiz that is automatic created when data is posted


**```user```**
*```Type - ForeignKey```*
Id of the user who creates the quiz


**```name```**
*```Type - CharField```*
Name of quiz


**```questions_count```**
*```Type - IntegerField```*
How many questions this quiz will  contain


**```created```**
*```Type - DateTimeField```*
When the quiz has been created.


**```description```**
*```Type - TextField```*
Detail about quiz


**```label```**
*```Type - CharField```*
What is the question

**```order```**
*```Type - IntergerField```*
Order of question


**```text```**
*```Type - CharField```*
Answer Choices


**```is_correct```**
*```Type - bool```*
This answer is correct or not