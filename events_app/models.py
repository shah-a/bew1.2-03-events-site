"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref
from enum import Enum

class EVENT_TYPE(Enum):
    RELAX = 1
    PARTY = 2
    STUDY = 3
    NETWORKING = 4

class Guest(db.Model):
    """Guest model."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    phone = db.Column(db.String(20))
    events = db.relationship('Event', secondary='guest_event', back_populates='guests')

class Event(db.Model):
    """Event model."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(80))
    date_and_time = db.Column(db.Date)
    event_type = db.Column(db.Enum(EVENT_TYPE))
    guests = db.relationship('Guest', secondary='guest_event', back_populates='events')

guest_event_table = db.Table('guest_event',
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
)
