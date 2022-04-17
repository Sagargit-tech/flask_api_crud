import email
from app import app
import sqlite3 as sql

from model.user_model import user_model
from flask import Flask, request,render_template
@app.route("/user/getall")

def user_getall_controller():
    obj= user_model()
    
    return obj.user_getall_model()
    

@app.route("/user/addone", methods= ['POST','GET'])
def user_addone_controller():
    data=[]
    
    if request.method == 'POST':
        id = request.form['ID'] 
        nm=request.form['nm']
        data.append(nm)
        email = request.form['email']
        data.append(email)
        phone = request.form['phone']
        data.append(phone)
        role = request.form['role']
        data.append(role)
        password = request.form['pass']
        data.append(password)
    
        with sql.connect('flask_api.db') as con:
           cur=con.cursor()
           cur.execute('INSERT INTO users(id,name,email,phone,role,password) VALUES (?,?,?,?,?,?)',(id,nm,email,phone,role,password))
    
    return render_template("user.html")


@app.route("/user/update", methods= ['POST','GET'])
def user_update_controller():
    
    obj= user_model()
    return obj.user_update_model()

@app.route("/user/delete/<id>", methods=['DELETE'])
def user_delete_controller(id):
    obj = user_model()
    return obj.user_delete_model(id)

