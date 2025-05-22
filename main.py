from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import TEXT, VARCHAR, LargeBinary, create_engine, Column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = FastAPI()

DATABASE_URL='postgresql://postgres:password123@localhost:5432/clef' 

engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(autocommit= False ,autoflush=False, bind= engine)


db = sessionLocal()

class UserCreate(BaseModel):
    name:str
    email:str
    password:str

#creating sqlalchemy declarative base instance
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(TEXT, primary_key=True)
    name = Column(VARCHAR(100))
    email = Column(VARCHAR(100))
    password = Column(LargeBinary) #CONVERT the text into something else




@app.post('/signup')
def signup_user(user: UserCreate):
    #extract the data thats coming from req
    print(user.name)
    print(user.email)
    print(user.password)
    #check if the user already exists in db
    #add the user in db
    pass
