import uuid
import bcrypt
from fastapi import  HTTPException
from database import get_db
from models.user import User
from pydantic_schemas.user_create import UserCreate
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
router = APIRouter()


@router.post('/signup')

def signup_user(user: UserCreate, db: Session = Depends(get_db)):
    #extract the data thats coming from req
    #print(user.name)
    #print(user.email)
    #print(user.password)

    #check if the user already exists in db

    user_db = db.query(User).filter(User.email == user.email).first()

    if user_db:
        raise HTTPException(400, ' User with the same email already exists!')
        

    hash_pw = bcrypt.hashpw(user.password.encode(),bcrypt.gensalt())
    user_db = User(id=str(uuid.uuid4()), email=user.email,password=hash_pw,name=user.name)

    
    #add the user in db
    db.add(user_db)
    db.commit()
    db.refresh(user_db)

    return user_db
