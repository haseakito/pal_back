from pydantic import BaseModel

# User base schema
class UserBase(BaseModel):
    id: str
    username: str
    email: str
    profileImage: str


class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserUnique(UserBase):
    bio: str
    coverImage: str
    