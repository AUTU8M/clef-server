
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL='postgresql://postgres:admin123@localhost:5432/clef' 

engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(autocommit= False ,autoflush=False, bind= engine)

 
db = sessionLocal()