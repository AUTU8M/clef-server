import bcrypt
from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import TEXT, VARCHAR, LargeBinary, create_engine, Column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import uuid

app = FastAPI()

#here im doing some testin

DATABASE_URL='postgresql://postgres:admin123@localhost:5432/clef' 

engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(autocommit= False ,autoflush=False, bind= engine)

 
db = sessionLocal()

class UserCreate(BaseModel):
    name:str
    email:str
    password:str



#this if for testing 

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
    #print(user.name)
    #print(user.email)
    #print(user.password)

    #check if the user already exists in db

    user_db = db.query(User).filter(User.email == user.email).first()

    if user_db:
        return ' User with the same email already exists!'

    hash_pw = bcrypt.hashpw(user.password.encode(),bcrypt.gensalt())
    user_db = User(id=str(uuid.uuid4()), email=user.email,password=user.password,name=user.name)
    

    
    #add the user in db
    db.add(user_db)
    db.commit()

    return user_db


Base.metadata.create_all(engine)
