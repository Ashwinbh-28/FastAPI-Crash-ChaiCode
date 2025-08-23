from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# create a user model
class User(BaseModel):
    id: int
    name: str
    is_employed: bool

input_data = {
    "id": 1,
    "name": "John Doe",
    "is_employed": True
}
user = User(**input_data)
print(user)
