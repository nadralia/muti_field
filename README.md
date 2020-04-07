# tims
Tims is a Django application that implements the logic to support
subscription-based Software-as-a-Service businesses for tours and itinerary management system.

Major Features:

- populate the features here

Development
===========

After cloning the repository, create a virtualenv environment and install
the prerequisites:

### Installation
<pre><code>
    $ Virtualenv venv
    $ source venv/Scripts/activate
    $ source .env
    $ pip install -r requirements.txt
</code></pre>

## API Endpoints
| Methods | EndPoint                                | Functionality                                    |Access
| ------- | --------------------------------------- | -------------------------------------------------|------
| POST    | /api/v1/accounts/                       | Create Company Account and Manager user          | public



## Endpoint Examples

### Create company account (Request)

```source-json
{
   "company": {
       "name":"KainGroup",
       "address":"p.o.box 2345 , kampala uganda"
    },
    "user":{
    	 "username":"nadralia",
    	 "password":"*******"
    }
}
```
### Response 

```source-json
{
    "company": {
        "id": "05fa1417-bbf2-4ac3-ad40-12a9879e4e46",
        "name": "KainGroup",
        "address": "p.o.box 2345 , kampala uganda"
    },
    "user": {
        "url": "http://127.0.0.1:8000/api/v1/accounts/users/4f6535ee-3653-44a7-b6de-f0708cec617b",
        "id": "4f6535ee-3653-44a7-b6de-f0708cec617b",
        "username": "nadralia"
    }
}
```

### User Login (Request)

```source-json
{
	"user": {
		"email":"nadralia@gmail.com",
		"password":"nadra2922"
	}
}
```
### Response 

```source-json
{
    "data": {
        "email": "nadralia@gmail.com",
        "username": "nadralia@gmail.com",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJuYWRyYWxpYUBnbWFpbC5jb20iLCJpYXQiOjE1ODQ0MzkxOTksImV4cCI6MTU4NDQ0OTk5OX0.VvQtqET1ZqGLU3Qz47l_6VNQxKntYk6-MQo6aQE36XM"
    }
}
```

### Create Inquiry (Request)

```source-json
{
	"inquiry": {
		"description": "I want to tour the major parts of uganda"
	},
	"client":{
		"name":"adralia nelson"
	}
}
```
### Response 

```source-json
{
    "id": 3,
    "inquirystatus": 0,
    "description": "I want to tour the major parts of uganda"
}
```

### Create itinerary

```source-json
{
	"itinerary":{
		"inquiry_id":1,
	    "client_id":4,
		"itineraryname":"tour eastern uganda",
		"numberadults":5,
		"numberchildren":2,
		"arrival":"",
		"guide":"",
		"driver":"",
		"day": [
	        {
	            "type": 1,
	            "activity": [
	            	{
	            		"title":"",
	            		"description":""
	            	},
	                 {
	            		"title":"",
	            		"description":""
	            	}
	            ]
	        },
	        {
	            "type": 1,
	            "activity": [
	            	{
	            		"title":"",
	            		"description":""
	            	},
	                 {
	            		"title":"",
	            		"description":""
	            	}
	            ]
	        }
        ]
          
		
	}
		
}
```
### Response 

```source-json
{

}
```


### Technologies used to build the application
- `Python3` - A programming language that lets us work more quickly.
- `Django REST framework` -  is a powerful and flexible toolkit for building Web APIs.
- `Virtualenv` - A tool to create an isolated virtual environment.
- `Git` - Version Control System for tracking your changes.
