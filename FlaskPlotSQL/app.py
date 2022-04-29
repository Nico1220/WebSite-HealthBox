import matplotlib
from flask import Flask, render_template, request, redirect, session
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use('Agg')
from io import BytesIO
import base64

app = Flask(__name__)
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="testDB")
img = BytesIO()

@app.route('/diagram')
def plot():

    mycursor = mydb.cursor()
    # Fecthing Data From mysql to my python progame
    mycursor.execute("select s_time, s_temp, s_spO2, s_puls from testDB_table LIMIT 20")
    result = mycursor.fetchall

    Time = []
    Temperatur = []
    SpO2 = []
    Puls = []

    for i in mycursor:
        Time.append(i[0])
        Temperatur.append(i[1])
        SpO2.append(i[2])
        Puls.append(i[3])


    plt.plot(Time, Temperatur)
    plt.ylim(35, 45)
    plt.xlabel("Time")
    plt.ylabel("Temperature")
    plt.title("Temperatur")
    plt.savefig(img)
    plt.close()
    img.seek(0)
    plotTemp = base64.b64encode(img.getvalue()).decode('utf8')


    # Visulizing Data using Matplotlib
    plt.plot(Time, SpO2)
    plt.ylim(80, 110)
    plt.xlabel("Time")
    plt.ylabel("SpO2")
    plt.title("SpO2")
    plt.savefig(img)
    plt.close()
    img.seek(0)
    plotSpO2= base64.b64encode(img.getvalue()).decode('utf8')

    # Visulizing Data using Matplotlib
    plt.plot(Time, Puls)
    plt.ylim(45, 110)
    plt.xlabel("Time")
    plt.ylabel("Puls")
    plt.title("Puls")
    plt.savefig(img)
    plt.close()
    img.seek(0)
    plotPuls = base64.b64encode(img.getvalue()).decode('utf8')


    return render_template('plot.html' , plotTemp=plotTemp, plotSpO2=plotSpO2, plotPuls=plotPuls)

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/table', methods=['GET'])
def table():
    cursor = mydb.cursor()
    # Fecthing Data From mysql to my python progame
    cursor.execute("select s_time, s_temp, s_spO2, s_puls from testDB_table LIMIT 20")
    rows = cursor.fetchall()
    return render_template("table.html", rows=rows)


if __name__ == '__main__':
    app.run()

