import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledefinition import *
 
engine = create_engine('sqlite:///credentials.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User("Admin","Pass")
session.add(user)

user = User("Guest","guest")
session.add(user)

user = User("Mag","1234")
session.add(user)

# commiting records to database
session.commit()
session.commit()
