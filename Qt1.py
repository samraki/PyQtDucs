from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

now = QDate.currentDate()
print(now)
print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))
print("---")
datetime = QDateTime.currentDateTime()
print(datetime)
print(datetime.toString())
print("---")
time = QTime.currentTime()
print(time.toString(Qt.ISODate))
print(time.toString(Qt.DefaultLocaleLongDate))

