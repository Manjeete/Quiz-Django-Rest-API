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
    
	"username":"user",
	"email":"email@gmail.com",
	"password":"user",
	"password2":"user"
}

```