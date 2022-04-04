"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80))
    phone = db.Column(db.String(20))
    events_attending = db.relationship('Event', secondary='guest_event')

# STRETCH CHALLENGE: Add a field `event_type` as an Enum column that denotes the
# type of event (Party, Study, Networking, etc)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    date_and_time = db.Column(db.DateTime)
    guests = db.relationship('Guest', secondary='guest_event')

guest_event_table = db.Table('guest_event', 
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id')),
)


