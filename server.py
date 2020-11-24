#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)


class Employees(Resource):
    def get(self):
        conn = db_connect.connect()  # connect to database
        # This line performs query and returns json result
        query = conn.execute("select * from employees")
        # Fetches first column that is Employee ID
        return {'employees': [i for i in query.cursor.fetchall()]}

    def post(self):
        conn = db_connect.connect()
        print(request.json)
        LastName = request.json['LastName']
        FirstName = request.json['FirstName']
        Title = request.json['Title']
        ReportsTo = request.json['ReportsTo']
        BirthDate = request.json['BirthDate']
        HireDate = request.json['HireDate']
        Address = request.json['Address']
        City = request.json['City']
        State = request.json['State']
        Country = request.json['Country']
        PostalCode = request.json['PostalCode']
        Phone = request.json['Phone']
        Fax = request.json['Fax']
        Email = request.json['Email']
        query = conn.execute("insert into employees values(null,'{0}','{1}','{2}','{3}', \
                             '{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}', \
                             '{13}')".format(LastName, FirstName, Title,
                                             ReportsTo, BirthDate, HireDate, Address,
                                             City, State, Country, PostalCode, Phone, Fax,
                                             Email))
        return {'status': 'success'}

    def delete(self):
        conn = db_connect.connect()
        print(request.json)
        query = conn.execute(
            """delete from employees where LastName='%s'""" % request.json['LastName'])
        return{'status': 'success'}


api.add_resource(Employees, '/employees')  # Route_1


if __name__ == '__main__':
    app.run()
