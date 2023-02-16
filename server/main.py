''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Necessary Imports
from fastapi import FastAPI, Request              # The main FastAPI import and Request object
from fastapi.responses import HTMLResponse        # Used for returning HTML responses (JSON is default)
from fastapi.templating import Jinja2Templates    # Used for generating HTML from templatized files
from fastapi.staticfiles import StaticFiles       # Used for making static resources available to server
import uvicorn                                    # Used for running the app directly through Python
import mysql.connector as mysql                   # Used for interacting with the MySQL database
import os                                         # Used for interacting with the system environment
from dotenv import load_dotenv                    # Used to read the credentials

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Configuration
load_dotenv('../credentials.env')                 # Read in the environment variables for MySQL
db_host = os.environ['MYSQL_HOST']
db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']

app = FastAPI()                                   # Specify the "app" that will run the routing
views = Jinja2Templates(directory='views')        # Specify where the HTML files are located
static_files = StaticFiles(directory='public')    # Specify where the static files are located
app.mount('/public', static_files, name='public') # Mount the static files directory to /public

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Define helper functions for CRUD operations

# CREATE SQL query
def db_create_user(first_name:str, last_name:str) -> int:
  '''
  1. Open a connection to the database
  2. INSERT a new user into the table
  3. Close the connection to the database
  4. Return the new user's ID (this is stored in the cursor's 'lastrowid' attribute after execution)
  '''
  return 0

# SELECT SQL query
def db_select_users(user_id:int=None) -> list:
  '''
  1. Open a connection to the database
  2. If the user_id is specified as an argument, perform a SELECT for just that user record
  3. If there is no user_id specified, then perform a SELECT for all users
  4. Close the connection to the database
  5. Return the retrieved record(s)
  '''
  return []

# UPDATE SQL query
def db_update_user(user_id:int, first_name:str, last_name:str) -> bool:
  '''
  1. Open a connection to the database
  2. UPDATE the user in the database
  3. Close the connection to the database
  4. Return True if a row in the database was successfully updated and False otherwise (you can
     check how many records were affected by looking at the cursor's 'rowcount' attribute)
  '''
  return False

# DELETE SQL query
def db_delete_user(user_id:int) -> bool:
  '''
  1. Open a connection to the database
  2. DELETE the user in the database
  3. Close the connection to the database
  4. Return True if a row in the database was successfully deleted and False otherwise (you can
     check how many records were affected by looking at the cursor's 'rowcount' attribute)
  '''
  return False

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Home route to load the main page in a templatized fashion

# GET /
@app.get('/', response_class=HTMLResponse)
def get_home(request:Request) -> HTMLResponse:
  return views.TemplateResponse('index.html', {'request':request, 'users':db_select_users()})

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# RESTful User Routes

# GET /users
# Used to query a collection of all users
@app.get('/users')
def get_users() -> dict:
  '''
  1. Query the database for all users
  2. Format the results as a list of dictionaries (JSON objects!) where the dictionary keys are:
    'id', 'first_name', and 'last_name'
  3. Return this collection as a JSON object, where the key is 'users' and the value is the list
  '''
  return {'users': []}

# GET /users/{user_id}
# Used to query a single user
@app.get('/users/{user_id}')
def get_user(user_id:int) -> dict:
  '''
  1. Query the database for the user with a database ID of 'user_id'
  2. If the user does not exist, return an empty object
  3. Otherwise, format the result as JSON where the keys are: 'id', 'first_name', and 'last_name'
  4. Return this object
  '''
  return {}

# POST /users
# Used to create a new user
@app.post("/users")
async def post_user(request:Request) -> dict:
  '''
  1. Retrieve the data asynchronously from the 'request' object
  2. Extract the first and last name from the POST body
  3. Create a new user in the database
  4. Return the user record back to the client as JSON
  '''
  return {}

# PUT /users/{user_id}
@app.put('/users/{user_id}')
async def put_user(user_id:int, request:Request) -> dict:
  '''
  1. Retrieve the data asynchronously from the 'request' object
  2. Attempt to update the user first and last name in the database
  3. Return the update status under the 'success' key
  '''
  return {'success': False}

# DELETE /users/{user_id}
@app.delete('/users/{user_id}')
def delete_user(user_id:int) -> dict:
  '''
  1. Attempt to delete the user from the database
  2. Return the delete status under the 'success' key
  '''
  return {'success': False}

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# If running the server directly from Python as a module
if __name__ == "__main__":
  uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)