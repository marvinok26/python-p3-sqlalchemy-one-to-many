#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

if __name__ == '__main__':
    engine = create_engine('sqlite:///one_to_many.db')
    Base.metadata.create_all(engine)  # Create tables based on models
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb; ipdb.set_trace()
