from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

#Base = declarative_base()

#class Knowledge(Base):
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article


Base = declarative_base()


class Food(Base):
   __tablename__ = 'food'
   food_name = Column(String, primary_key=True)
   color = Column(String)
   calories = Column(Integer)
   taste = Column(String)
   def __repr__ (self):
   	return("food Name: {}\n"
               "food color : {} \n"
               "caloriess: {} \n" 
               "taste :{}").format(
                    self.food_name, self.color, self.calories, self.taste) 
pizza=Food(food_name="pizza", color="orange",calories=500,taste="niiice")
print(pizza)

class Pilots(Base):
   __tablename__ = 'pilots'
   pilot_name = Column(String, primary_key=True)
   airplane = Column(String)
   age = Column(Integer)
   experience = Column(String)
   def __repr__ (self):
   	return("pilot Name: {}\n"
   		"airplane : {}\n"
   		"age: {} \n" 
   		"experience :{}").format(self.pilot_name, self.airplane, self.age, self.experience)

john=Pilots(pilot_name ="john", airplane = "boeing 777", age=55 , experience= "general")
print(john)


  