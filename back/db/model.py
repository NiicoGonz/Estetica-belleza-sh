from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):
    __tablename__ = 'Employee'

    id_e = db.Column(db.String(20), primary_key=True, nullable=False)
    name_e = db.Column(db.String(50), nullable=False)
    lastname_e = db.Column(db.String(50), nullable=False)
    id_specialty = db.Column(db.String(5), db.ForeignKey('Specialty.id_sp'))
    id_schedule = db.Column(db.String(5), db.ForeignKey('Schedule.id_sc'))
    rating = db.Column(db.Float())
    photo = db.Column(db.LargeBinary)
    client_one = db.relationship('Client', backref='favorite', lazy='dynamic', foreign_keys='Client.favorite_one')
    client_two = db.relationship('Client', backref='favorite', lazy='dynamic', foreign_keys='Client.favorite_two')
    client_three = db.relationship('Client', backref='favorite', lazy='dynamic', foreign_keys='Client.favorite_three')
    appointment_e = db.relationship('Appointment', backref='employee', lazy='dynamic', foreign_keys='Appointment.id_employee')

    def __init(self, id_e, name_e, lastname_e, id_specialty, id_schedule,rating, photo):
        self.id_e = id_e
        self.name_e = name_e
        self.lastname_e = lastname_e
        self.id_specialty = id_specialty
        self.id_schedule = id_schedule
        self.rating = rating
        self.photo = photo

class Client(db.Model):
    __tablename__ = 'Client'

    id_c = db.Column(db.String(20), primary_key=True, nullable=False)
    name_c = db.Column(db.String(50), nullable=False)
    lastname_c = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    favorite_one = db.Column(db.String(20), db.ForeignKey('Employee.id_e')) 
    favorite_two = db.Column(db.String(20), db.ForeignKey('Employee.id_e'))
    favorite_three = db.Column(db.String(20), db.ForeignKey('Employee.id_e'))
    appointment_c = db.relationship('Appointment', backref='client', lazy='dynamic', foreign_keys='Appointment.id_client')

    def __init(self, id_c, name_c, lastname_c, email, password, favorite_one, favorite_two, favorite_three):
        self.id_c = id_c
        self.name_c = name_c
        self.lastname_c = lastname_c
        self.email = email
        self.password = password
        self.favorite_one = favorite_one
        self.favorite_two = favorite_two
        self.favorite_three = favorite_three

class Services(db.Model):
    __tablename__ = 'Services'

    id_s = db.Column(db.String(5), primary_key=True, nullable=False)
    name_s = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float())
    appointment_s = db.relationship('Appointment', backref='services', lazy='dynamic', foreign_keys='Appointment.id_services')

    def __init(self, id_s, name_s, price):
        self.id_s = id_s
        self.name_s = name_s
        self.price = price


class Appointment(db.Model):
    __tablename__ = 'Appointment'

    id_a = db.Column(db.String(5), primary_key=True, nullable=False)
    id_client = db.Column(db.String(20), db.ForeignKey('Client.id_c'))
    id_employee = db.Column(db.String(20), db.ForeignKey('Employee.id_e'))
    id_services = db.Column(db.String(5), db.ForeignKey('Services.id_s'))
    date_a = db.Column(db.DateTime, nullable=False)

    def __init(self, id_a, id_client, id_employee, id_services, date_a):
        self.id_a = id_a
        self.id_client = id_client
        self.id_employee = id_employee
        self.id_services = id_services
        self.date_a = date_a


class Specialty(db.Model):
    __tablename__ = 'Specialty'

    id_sp = db.Column(db.String(5), primary_key=True, nullable=False)
    name_sp = db.Column(db.String(100), nullable=False)
    employee_sp = db.relationship('Employee', backref='specialty', lazy='dynamic', foreign_keys='Employee.id_specialty')

    def __init(self, id_sp, name_sp):
        self.id_sp = id_sp
        self.name_sp = name_sp


class Schedule(db.Model):
    __tablename__ = 'Schedule'

    id_sc = db.Column(db.String(5), primary_key=True, nullable=False)
    entry_time = db.Column(db.Time)
    departure_time = db.Column(db.Time)
    employee_sc = db.relationship('Employee', backref='schedule', lazy='dynamic', foreign_keys='Employee.id_schedule')

    def __init(self, id_sc, entry_time, departure_time):
        self.id_sc = id_sc
        self.entry_time = entry_time
        self.departure_time = departure_time

