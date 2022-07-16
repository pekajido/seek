from flask import Flask, render_template, url_for, request, redirect
import csv
import sqlite3

app= Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def project(page_name):
    return render_template(page_name)

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		name= data["name"]
		email= data["email"]
		number= data["number"]
		message= data["message"]
		file= database.write(f'{name},{email}, {number}, {message}\n')


def write_to_csv(data):
	with open('database.csv', mode='a',newline='') as database2:
		name= data['name']
		email= data["email"]
		number= data["number"]
		message= data["message"]
		csv_writer= csv.writer(database2, delimiter=',', quotechar= '"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([name,email,number, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method== 'POST':
    	data= request.form.to_dict()
    	write_to_csv(data)
    	return redirect('/Thankyou.html')
    else:
    	return 'somthing went wrong, Try agin!'
