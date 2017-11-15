from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import re
import base64

Base = declarative_base()

DB_info = {
    'database': 'testdb',
    'database_driver': 'mysql+mysqlconnector',
    'user': 'test',
    'passward': 'testpw',
    'ip': '127.0.0.1',
    'port': '3306',
}

class Coupon(Base):
    __tablename__ = 'Coupon'
    id = Column(Integer, primary_key=True)
    c_id = Column(String(200))
    c_code = Column(String(200))

def connectDB(database_info):

    engine = create_engine('{database_driver}://{user}:{passward}@{ip}:{port}/{database}'.format_map(database_info))
    DBSession = sessionmaker(engine)
    session = DBSession()
    return session

def parse_coupon(c_code):
    return base64.urlsafe_b64decode(c_code.encode('utf-8'))


def uploadDB():
    session = connectDB(DB_info)
    with open('coupon.txt', 'r') as file:
        for line in file:
            cid = re.findall(r'.*/.*:(.*)\'', str(parse_coupon(line)))
            ccode = line.split('=')[0]
            session.add(Coupon(c_id = cid.pop(), c_code=ccode))
        session.commit()
        session.close()


if __name__ == '__main__':
    uploadDB()