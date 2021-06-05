import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_serializer import SerializerMixin

conn = sa.create_engine('sqlite:///flights.db')

Base = declarative_base()


class Flights(Base, SerializerMixin):
    __tablename__ = 'flights'
    serialize_only = ('number', 'departure_time', 'arrival_time')
    id = sa.Column('Id', sa.Integer, primary_key=True, nullable=False)
    origin = sa.Column('Origin', sa.CHAR(3), nullable=False)
    destination = sa.Column('Destination', sa.CHAR(3), nullable=False)
    departure_date = sa.Column('DepartureDate', sa.CHAR(8), nullable=False)
    departure_time = sa.Column('DepartureTime', sa.CHAR(4), nullable=False)
    arrival_date = sa.Column('ArrivalDate', sa.CHAR(8), nullable=False)
    arrival_time = sa.Column('ArrivalTime', sa.CHAR(4), nullable=False)
    number = sa.Column('Number', sa.VARCHAR(15), nullable=False)

    def __init__(self, id, origin, destination, departure_date, departure_time, arrival_date, arrival_time, number):
        self.id = id
        self.origin = origin
        self.destination = destination
        self.departure_date = departure_date
        self.departure_time = departure_time
        self.arrival_date = arrival_date
        self.arrival_time = arrival_time
        self.number = number


def save_list(list_to_save):
    Session = sessionmaker(bind=conn)
    session = Session()
    session.add_all(list_to_save)
    session.commit()


def get_fligths_by_id(id):
    Session = sessionmaker(bind=conn)
    session = Session()
    return session.query(Flights).filter(Flights.id == id).first()


Base.metadata.drop_all(bind=conn, tables=[Flights.__table__])
Base.metadata.create_all(conn)
