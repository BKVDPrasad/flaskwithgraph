from flask import Flask, render_template

app = Flask(__name__)
from matplotlib import pyplot as plt
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import dash_bootstrap_components as dbc
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import dash
# import dash_bootstrap_components as dbc
# import dash_core_components as dcc
# import dash_html_components as html
import sqlite3
# from dash.dependencies import Input, Output, State
import paho.mqtt.client as mqtt
import time
import pandas as pd
import sqlite3
import os
import pathlib
import base64
from six.moves.urllib.parse import quote
from sqlalchemy import create_engine
from datetime import datetime, timedelta
import unicodedata
# import dash_daq as daq
# from flask_mqtt import Mqtt
# from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db_URI = os.environ.get('DATABASE_URL', 'sqlite:///test.db')
engine = create_engine(db_URI)


class User(db.Model):
    __tablename__ = 'datatable'

    id = db.Column(db.Integer, primary_key=True)
    stamp = db.Column(db.String(26))
    devId = db.Column(db.String(15))
    SPA = db.Column(db.String(10))
    TA = db.Column(db.String(10))

    def __repr__(self):
        return '<User %r %r  %r %r>' % (self.stamp, self.devId, self.SPA, self.TA)


class smb(db.Model):
    __tablename__ = 'smbtable'

    id = db.Column(db.Integer, primary_key=True)
    stamp = db.Column(db.String(26))
    devId = db.Column(db.String(15))
    str1 = db.Column(db.String(10))
    str2 = db.Column(db.String(10))
    str3 = db.Column(db.String(10))
    str4 = db.Column(db.String(10))
    str5 = db.Column(db.String(10))
    str6 = db.Column(db.String(10))
    str7 = db.Column(db.String(10))
    str8 = db.Column(db.String(10))
    str9 = db.Column(db.String(10))
    str10 = db.Column(db.String(10))
    str11 = db.Column(db.String(10))
    str12 = db.Column(db.String(10))
    str13 = db.Column(db.String(10))
    vol1 = db.Column(db.String(10))
    vol2 = db.Column(db.String(10))
    vol3 = db.Column(db.String(10))
    vol4 = db.Column(db.String(10))
    vol5 = db.Column(db.String(10))
    vol6 = db.Column(db.String(10))
    vol7 = db.Column(db.String(10))
    vol8 = db.Column(db.String(10))
    vol9 = db.Column(db.String(10))
    vol10 = db.Column(db.String(10))
    vol11 = db.Column(db.String(10))
    vol12 = db.Column(db.String(10))
    vol13 = db.Column(db.String(10))
    temp = db.Column(db.String(10))
    stravg = db.Column(db.Float)
    volavg = db.Column(db.Float)
    poweravg = db.Column(db.Float)

    def __repr__(self):
        return '<User %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r %r>' % (
        self.stamp, self.devId, self.str1, self.str2, self.str3, self.str4, self.str5, self.str6, self.str7, self.str8,
        self.str9,
        self.str10, self.str11, self.str12, self.str13, self.vol1, self.vol2, self.vol3, self.vol4, self.vol5,
        self.vol6, self.vol7, self.vol8, self.vol9, self.vol10, self.vol11, self.vol12, self.vol13, self.temp,
        self.stravg, self.volavg, self.poweravg)


db.create_all()


def on_connect(client, userdata, flags, rc):
    print("Connected!", rc)
    if rc == 0:
        client.connected_flag = True  # set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed:", str(mid), str(granted_qos))


def on_unsubscribe(client, userdata, mid):
    print("Unsubscribed:", str(mid))


def on_publish(client, userdata, mid):
    print("Publish:", client)


def on_log(client, userdata, level, buf):
    print("log:", buf)


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")


messagelist = []
messagelist2 = []
smbdict = {}
teststr = ""
a = []
b = []
c = []
e = []
devicetime = []
d = {}






@app.route('/')
def home():
    res=smb.query.all()
    return render_template("smb.html", data=res)



@app.route('/lchart')
def lchart():
    #i = request.GET.get('un')
    data=smb.query.all()
    d1=data['poweravg']
    d2=data['volavg']
    # x = ['Telugu', 'Hindi', 'English','Maths','Science','Social']
    #  corresponding y axis values
    # y = [data.telugu, data.hindi, data.english,data.maths,data.science,data.social]
    x=['poweravg']
    y=[89]
    # plotting the points
    plt.plot(x, y)

    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')

    # giving a title to my graph
    plt.title('Student subject and marks')

    # function to show the plot
    #plt.show()

    img = plt.savefig(fname='static/line1.png')
    #img=plt.savefig(fname='app/static/line.png')
    return render_template('line.html')

@app.route('/show')
def show():
    return render_template('tracker.html')






@app.route('/line')
def line():

    res = User.query.all()
    print('res')
    i=res[0]
    print('hi')
    print(i)
    print(type(i))

    l1=[]
    l2=[]
    for x in res:
        print(x.stamp)
        d=x.stamp
        spa=x.SPA
        l1.append(d)
        l2.append(spa)

    single=res[0]
    labels = [
        '9:00', '9:15', '9:30', '9:45',
        '10:00', '10:15', '10:30', '10:45',
        '11:00', '11:16', '11:30', '12:00'
    ]

    values = [
        9167.67, 1190.89, 1079.75, 1349.19,
        2328.91, 2504.28, 2873.83, 4764.87,
        4349.29, 6458.30, 9907, 16297
    ]

    line_labels=l1
    line_values=l2
    return render_template('line_chart.html', title='TRACKER', max=100, labels=line_labels, values=line_values,data=res,data1=single)
    return None



def on_message(client, userdata, message):
    data = {}
    data1 = {}
    global d
    payload = str(message.payload.decode("utf-8"))  # +" "
    print("payload=", payload, len(payload))
    print("payload[:4]", payload[:4], len(payload))
    # messagelist=
    if payload[:4] == "Dev:":  # and len(payload)!=45:
        ind = payload.index(",Time")
        # ind=ind+25
        print("index devid=", ind)
        print("payload[ind+25:]", payload[ind + 25:], len(payload))
        teststr = payload[:ind] + payload[ind + 25:]
        messagelist.append(payload)
        if len(messagelist) > 4:
            messagelist.remove(messagelist[0])
        print("smbmessagelist=", messagelist)
        data = dict(x.split(":") for x in teststr.split(","))
        data['Time'] = payload[ind + 21:ind + 25] + "-" + payload[ind + 18:ind + 20] + "-" + payload[
                                                                                             ind + 15:ind + 17] + "T" + payload[
                                                                                                                        ind + 6:ind + 14] + ".000000"
        print("smb data=", data)
    print("pay data1=", payload[:6])

    if payload[:6] == "DevId:":
        print("hi data1")
        data1 = dict(x.split(":") for x in payload.split(","))
        messagelist2.append(payload)
        if len(messagelist2) > 4:
            messagelist2.remove(messagelist2[0])
        print("messagelist2=", messagelist2)
    print("data=", data1)
    print("smb data=", data)
    print("len dataa=", len(data))
    if (len(data1) == 3):
        print("len", len(data1))
        admin = User(stamp=str(datetime.now() + timedelta(minutes=330)), devId=data1['DevId'], SPA=data1['SPA'],
                     TA=data1['TA'])
        db.session.add(admin)
        db.session.commit()
        print("data saved to datatabe")

    elif len(smbdict) == 28:
        print("smb dict=", smbdict)
        stravg = 0
        stravg = float(smbdict['str1']) + float(smbdict['str2']) + float(smbdict['str3']) + float(
            smbdict['str4']) + float(smbdict['str5']) + float(smbdict['str6']) + float(smbdict['str7']) + float(
            smbdict['str8']) + float(smbdict['str9']) + float(smbdict['str10']) + float(smbdict['str11']) + float(
            smbdict['str12']) + float(smbdict['str13'])
        stravg = float(stravg / 13)
        smbdict['stravg'] = stravg
        print("smb dict=", smbdict)
        volavg = 0
        volavg = float(smbdict['vol1']) + float(smbdict['vol2']) + float(smbdict['vol3']) + float(
            smbdict['vol4']) + float(smbdict['vol5']) + float(smbdict['vol6']) + float(smbdict['vol7']) + float(
            smbdict['vol8']) + float(smbdict['vol9']) + float(smbdict['vol10']) + float(smbdict['vol11']) + float(
            smbdict['vol12']) + float(smbdict['vol13'])
        volavg = float(volavg / 13)
        smbdict['volavg'] = volavg
        print("smb dict=", smbdict)
        poweravg = 0
        poweravg = float((volavg * stravg) / 1000)
        smbdict['poweravg'] = poweravg
        smbdict['temp'] = data['temp']
        print("smb dict=", smbdict)

        smbdata = smb(stamp=smbdict['Time'], devId=smbdict['Dev'], temp=smbdict['temp'], str1=smbdict['str1'],
                      vol1=smbdict['vol1'], str2=smbdict['str2'], vol2=smbdict['vol2'], str3=smbdict['str3'],
                      vol3=smbdict['vol3'], str4=smbdict['str4'], vol4=smbdict['vol4'], str5=smbdict['str5'],
                      vol5=smbdict['vol5'], str6=smbdict['str6'], vol6=smbdict['vol6'], str7=smbdict['str7'],
                      vol7=smbdict['vol7'],
                      str8=smbdict['str8'], vol8=smbdict['vol8'], str9=smbdict['str9'], vol9=smbdict['vol9'],
                      str10=smbdict['str10'], vol10=smbdict['vol10'], str11=smbdict['str11'], vol11=smbdict['vol11'],
                      str12=smbdict['str12'], vol12=smbdict['vol12'], str13=smbdict['str13'], vol13=smbdict['vol13'],
                      stravg=smbdict['stravg'], volavg=smbdict['volavg'], poweravg=smbdict['poweravg'])
        db.session.add(smbdata)
        db.session.commit()
        smbdict.clear()
        print("SMBdata saved to datatabe")

    elif len(data) == 4:
        if len(smbdict) == 0:
            smbdict.update(data)
        elif (('str2' not in smbdict) and ('str2' in data)):
            smbdict['str2'] = data['str2']
            smbdict['vol2'] = data['vol2']
        elif (('str3' not in smbdict) and ('str3' in data)):
            smbdict['str3'] = data['str3']
            smbdict['vol3'] = data['vol3']
        elif (('str4' not in smbdict) and ('str4' in data)):
            smbdict['str4'] = data['str4']
            smbdict['vol4'] = data['vol4']
        elif (('str5' not in smbdict) and ('str5' in data)):
            smbdict['str5'] = data['str5']
            smbdict['vol5'] = data['vol5']

        elif (('str6' not in smbdict) and ('str6' in data)):

            smbdict['str6'] = data['str6']
            smbdict['vol6'] = data['vol6']

        elif (('str7' not in smbdict) and ('str7' in data)):

            smbdict['str7'] = data['str7']
            smbdict['vol7'] = data['vol7']

        elif (('str8' not in smbdict) and ('str8' in data)):
            smbdict['str8'] = data['str8']
            smbdict['vol8'] = data['vol8']
        elif (('str9' not in smbdict) and ('str9' in data)):
            smbdict['str9'] = data['str9']
            smbdict['vol9'] = data['vol9']
        elif (('str10' not in smbdict) and ('str10' in data)):

            smbdict['str10'] = data['str10']
            smbdict['vol10'] = data['vol10']
        elif (('str11' not in smbdict) and ('str11' in data)):

            smbdict['str11'] = data['str11']
            smbdict['vol11'] = data['vol11']
        elif (('str12' not in smbdict) and ('str12' in data)):

            smbdict['str12'] = data['str12']
            smbdict['vol12'] = data['vol12']
        elif (('str13' not in smbdict) and ('str13' in data)):

            smbdict['str13'] = data['str13']
            smbdict['vol13'] = data['vol13']









client = mqtt.Client()
client.on_subscribe = on_subscribe
client.on_unsubscribe = on_unsubscribe
client.on_connect = on_connect
client.on_message = on_message
time.sleep(1)

subtop = "tracker/device/sub"
pubtop = "tracker/device/pub"
# client.username_pw_set("cbocdpsu", "3_UFu7oaad-8")
# client.connect('soldier.cloudmqtt.com', 14035, 60)
client.connect('ec2-54-185-112-88.us-west-2.compute.amazonaws.com')
client.loop_start()
client.subscribe(subtop)
client.loop()


if __name__ == '__main__':
    app.run()
