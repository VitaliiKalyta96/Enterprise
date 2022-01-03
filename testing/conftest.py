import pytest
from models import Plant, Employee, MenuItem, Salon
from app import app, db


@pytest.fixture
def client():
    app.test = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flask:flask@db:3306/flask'
    client = app.test_client()
    with app.app_context():
        db.create_all()
        db.session.commit()
    yield client


@pytest.fixture()
def plant_data():
    yield {
        'location': 'Ternopil',
        'name': 'Jacktom'
    }


@pytest.fixture()
def plant_update():
    yield {
        'location': 'Chernivtsi',
        'name': 'Jaison'
    }


@pytest.fixture()
def employee_data():
    yield {
        'email': 'jack@gmail.com',
        'name': 'Jack',
        'department_type': 'technic'
    } 


@pytest.fixture()
def employee_update():
    yield {
        'email': 'alex@gmail.com',
        'name': 'Alex',
        'department_type': 'technic2'
    }


@pytest.fixture()
def menuitem_data():
    yield {
        'name': 'Plant_Employee_Salon',
        'link': 'menu'
    }


@pytest.fixture()
def menuitem_update():
    yield {
        'name': 'Plant_Employee_Salon_2',
        'link': 'menu_2'
    }


@pytest.fixture()
def salon_data():
    yield {
        'name': 'Roy',
        'city': 'Lviv',
        'address': 'Washington street 20'
    }


@pytest.fixture()
def salon_update():
    yield {
        'name': 'Jack',
        'city': 'Ternopil',
        'address': 'Avenue street 25'
    }
