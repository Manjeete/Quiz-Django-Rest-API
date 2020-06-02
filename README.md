# Quiz-Django-Rest-API
This is an API for multiple-choice questions. Where You can GET, POST, PUT, PATCH, and DELETE your quiz and its question.


## Steps that You can do in this Rest API

- **User Register**
- **User Login**
- **Post You Quizs, Questions and, Answers**
- **Retrieve, Update, and Delete single Quiz**
- **User's own Quiz**

## User Register
User can register using the following Endpoint and own data

```python
Register Endpoint (Only Post Request)

https://quizrestapi.herokuapp.com/api/auth/register/
```
```python
data : {
    
	"username":"<username>",
	"email":"<user_email>",
	"password":"<password>",
	"password2":"<password>"
}

```
After sending POST request user will  receive the following response :
```python
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
```python
data : {
    
	"username":"<username>",
	"password":"<password>",
}
```