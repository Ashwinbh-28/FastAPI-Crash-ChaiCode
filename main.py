'''
basics hTTP methods:
    GET → Read

    POST → Create

    PUT → Replace/Update

    PATCH → Partial Update

    DELETE → Remove
'''

from fastapi import FastAPI

# create a fastapi app
app = FastAPI()

# create a route
@app.get('/')
def root():
    return {"message": "Hello there! FastAPI"}

# create a get for query parameters
@app.get('/query')
def query(name: str):
    return {"message": f"Hello {name}"}

