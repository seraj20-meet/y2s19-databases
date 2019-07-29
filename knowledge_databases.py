from knowledge_model import Base, Food, Pilots

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(name,year,age,airplane):
	pilots = Pilots(
	pilot_name=name,
	experience=year,
	age=age,
	airplane=airplane)
	session.add(pilots)
	session.commit()

add_article("max","good",55,"boeing 473")
 


def query_all_articles():
	airways=session.query(
		Pilots).all()
	return airways


def query_article_by_topic():
	pass

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass

print(query_all_articles())
