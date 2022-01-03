from app import app, db
from flask import render_template, request, redirect, url_for, session
from utils.helpers import encrypt_string
from models import Plant, Employee, Salon


@app.route('/')
def main():
    plants = Plant.query.all()
    employees = Employee.query.all()
    salons = Salon.query.all()
    return render_template('index.html', plants=plants, employees=employees, salons=salons, session=session)


@app.route('/plant/<int:id>')
def plant(id):
    plant = Plant.query.get(id)
    employees = Employee.query.all()
    return render_template('edit-plant.html', plant=plant, employees=employees, session=session)


@app.route('/login')
def login():
    return render_template('login.html', session=session)


@app.route('/auth', methods=['POST'])
def auth():
    form = request.form
    user = Employee.query.filter(Employee.email == form['login']).filter(
        Employee.password == encrypt_string(form['password'])).first()
    if user is not None:
        session['user'] = user.serialize
    return redirect("http://localhost:9092/")


@app.route('/logout')
def logout():
    session.pop('user')
    return render_template('logout.html')

    # return redirect(url_for('main'))

    # return jsonify({'message': 'You successfully logged out'})
    # return redirect("http://localhost:9092/")

    # login()
    # return redirect(url_for("main"))


@app.route('/plant/<int:id>/edit')
def plant_edit_page(id):
    if session.get('user') is None:
        return redirect("http://localhost:9092/")
    plant = Plant.query.get(id)
    employees = Employee.query.all()
    return render_template('edit-plant.html', plant=plant, employees=employees, salon=salon, session=session)


@app.route('/plant/<int:id>/update', methods=['POST'])
def plant_update(id):
    if session.get('user') is None:
        return redirect("http://localhost:9092/")
    plant = Plant.query.get(id)
    form_data = request.form
    plant.name = form_data.get('name')
    plant.location = form_data.get('location')
    plant.director_id = form_data.get('director_id')
    db.session.add(plant)
    db.session.commit()
    return redirect(url_for('plant', id=id))


@app.route('/employee/<int:id>')
def employee(id):
    employee = Employee.query.get(id)
    return render_template('employee.html', employee=employee, session=session)


@app.route('/employee/<int:id>/edit')
def employee_edit_page(id):
    employee = Employee.query.get(id)
    plants = Plant.query.all()
    salons = Salon.query.all()
    return render_template('edit-employee.html', plants=plants, employee=employee, salons=salons, session=session)


@app.route('/employee/<int:id>/update', methods=['POST'])
def employee_update(id):
    employee = Employee.query.get(id)
    form_data = request.form
    employee.email = form_data.get('email')
    employee.name = form_data.get('name')
    employee.department_type = form_data.get('department_type')
    employee.department_id = form_data.get('department_id')
    db.session.add(employee)
    db.session.commit()
    return redirect(url_for('employee', id=id))


@app.route('/salon/<int:id>')
def salon(id):
    salon = Salon.query.get(id)
    employees = Employee.query.all()
    return render_template('edit-salon.html', employees=employees, salon=salon, session=session)


@app.route('/salon/<int:id>/edit')
def salon_edit_page(id):
    if session.get('user') is None:
        return redirect("http://localhost:9092/")
    salon = Salon.query.get(id)
    employees = Employee.query.all()
    return render_template('edit-salon.html', plant=plant, employees=employees, salon=salon, session=session)


@app.route('/salon/<int:id>/update', methods=['POST'])
def salon_update(id):
    if session.get('user') is None:
        return redirect("http://localhost:9092/")
    salon = Salon.query.get(id)
    form_data = request.form
    salon.name = form_data.get('name')
    salon.address = form_data.get('address')
    db.session.add(salon)
    db.session.commit()
    return redirect(url_for('salon', id=id))