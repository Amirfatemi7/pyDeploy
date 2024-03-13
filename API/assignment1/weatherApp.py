from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap
import json
import requests

def search():
   
    a = my_window.lineEdit_1.text()
    print(a)
    resp = requests.get("https://goweather.herokuapp.com/weather/" + a)
    print(resp)
    if resp.status_code == 200:
        res = resp.json()
        print(res["temperature"])
        print(res["wind"])

        if res["description"] == "Partly cloudy":
            pixmap = QPixmap(' /img/pCloud.png')
            my_window.label.setPixmap(pixmap)
        if res["description"] == "Clear":
            pixmap = QPixmap(' /img/sun.png')
            my_window.label.setPixmap(pixmap)
        if res["description"] == "Light drizzle":
            pixmap = QPixmap(' /img/cloud.png')
            my_window.label.setPixmap(pixmap)
        if res["description"] == "Light rain":
            pixmap = QPixmap(' /img/rain.png')
            my_window.label.setPixmap(pixmap)

        
        my_window.lable_temp.setText(res["temperature"])
        my_window.lable_wind.setText(res["wind"])
        # print(res["forecast"][0]["temperature"])
        my_window.lable_temp_2.setText(res["forecast"][0]["temperature"])
        my_window.lable_wind_2.setText(res["forecast"][0]["wind"])
        my_window.lable_temp_4.setText(res["forecast"][1]["temperature"])
        my_window.lable_wind_4.setText(res["forecast"][1]["wind"])
        my_window.lable_temp_5.setText(res["forecast"][2]["temperature"])
        my_window.lable_wind_5.setText(res["forecast"][2]["wind"])
    else:
        msg_box = QMessageBox(text = " not working. error code: "+str(resp.status_code))
        msg_box.exec()

my_app = QApplication([])

loader = QUiLoader()

my_window = loader.load(" /weatherApp.ui")
my_window.show()


my_window.btn_search.clicked.connect(search)


my_app.exec()
