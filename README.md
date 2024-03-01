# ci-cd-learning

## How to run the application:

First, clone the repository

```
git clone https://github.com/asifrahaman13/ci-cd-learning.git
```
Next, open the terminal and enter into the backend folder. 

```
cd backend/
```
Next, create a virtual environment. 

```
virualenv venv
```

Activate the  virtual environment. The following code works for UNIX based system( Linux and Max OS)

```
source venv/bin/activate
```

Install all the dependencies.

```
pip install -r requirements.txt
```

Change the name of .env.example to .env and enter the env variables.

Next, run the backend server.

```
uvicorn main:app --reload
```
Now in another terminal open the front end.
