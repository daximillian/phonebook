#!/usr/bin/python3
from database import DataBase
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    edit = request.values.get('edit')
    search = request.values.get('search')
    delete = request.values.get('delete')
    data = DataBase(table="USERS").get()
    if search:
        search_data = []
        for i in data:
            find = False
            for x in i:
                if search in str(x):
                    find = True
            if find:
                search_data.append(i)
        if len(search_data) != 0:
            data = search_data
        else:
            message = "Target not found !"
    if delete:
        DataBase(table="USERS", rows="id", values=f"'{delete}'").delete()
        return redirect('?url=show')
    if edit:
        data = DataBase(table="USERS", values=f"id='{edit}'").search()
    if request.method == "POST":
        if "addValues" in request.form:
            name = request.form['name']
            phone = request.form['phoneNumber']
            email = request.form['emailAddress']
            DataBase(table="USERS", rows="name, number, email",
                     values=f"'{name}', '{phone}', '{email}'").add()
            message = f"{name} data`s Successfully registered"
        if "editValues" in request.form:
            name = request.form['name']
            phone = request.form['phoneNumber']
            email = request.form['emailAddress']
            DataBase(table="USERS", rows="id, name, number, email",
                     values=f"'{edit}', '{name}', '{phone}', '{email}'").replace()
            message = f"{name} data`s successfully edited !"
    return render_template("index.html", data=data, message=message)
