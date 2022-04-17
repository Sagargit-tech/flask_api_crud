import sqlite3 as sql
import json

from flask import Flask, request, render_template
class user_model():
    def __init__(self) :
        with sql.connect('flask_api.db') as con:
            self.cur=con.cursor()
    

    def user_getall_model(self):
        self.cur.execute("Select * FROM users")
        result=self.cur.fetchall()
        print (result)
        return json.dumps(result)

    def user_addone_model(self,data):
        print (data)
        # self.cur.executecur.execute('INSERT INTO students(name,addr,city,pin) VALUES (?,?,?,?)',(date[0],addr,city,pin))
        return "This is user add one model"
    
    def user_update_model(self):
        if request.method == "POST":
           i=int(request.form['ID'])
           print(type(i))
        #    my_data2 = users.query.get(request.form.get('id'))
           self.cur.execute("SELECT * FROM users WHERE id = 1 ")
           name = request.form['nm']
           print(name)
           email = request.form['email']
           phone = request.form['phone']
           role = request.form['role']
           password = request.form['pass']
           self.cur.execute('UPDATE users SET name="ravi" , email=email, phone=phone, role=role, password=password WHERE id ="1"')
        return render_template("update.html")

    def user_delete_model(self,id):
        self.cur.execute(f"DELETE FROM users WHERE id ={id}")
        if self.cur.rowcount>0:
            return "User Deleted Successfully"
        else:
            return "Nothing to Delete"