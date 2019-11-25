import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import design
import test

class DaBestApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()


class Login(QtWidgets.QDialog, design.Ui_Dialog):
    def __init__(self):
        super().__init__()


class UI:
    def main(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.dialog = Login()
        self.dialog.setupUi(self.dialog)
        self.dialog.buttonBox.accepted.connect(self.on_ok_button)
        self.dialog.show()
        self.app.exec_()

    def on_ok_button(self):
        '''self.host = self.dialog.host_tb.toPlainText()
        self.db_name = self.dialog.db_name_tb.toPlainText()
        self.login = self.dialog.login_tb.toPlainText()
        self.password = self.dialog.password_tb.toPlainText()'''
        self.host = "localhost"
        self.db_name = "hospital_test"
        self.login = "postgres"
        self.password = "90trks125"
        self.connection = test.connect(self.host, self.db_name, self.login, self.password)
        self.window = DaBestApp()
        self.window.setupUi(self.window)
        self.window.query1_button.clicked.connect(self.query1)
        self.window.query2_button.clicked.connect(self.query2)
        self.window.query3_button.clicked.connect(self.query3)
        self.window.query4_button.clicked.connect(self.query4)
        self.window.query5_button.clicked.connect(self.query5)
        self.window.clear_button.clicked.connect(self.clear_view)
        self.window.show()
        self.dialog.close()

    def query1(self):
        input_dialog = QtWidgets.QInputDialog()
        patient_id, ok_pressed = input_dialog.getInt(input_dialog, "Get patient id", "ID:", 0, 0, 100000, 1)
        if (ok_pressed):
            doctor_names = test.query_1(patient_id, self.connection)
            names = QtGui.QStandardItemModel()
            item = QtGui.QStandardItem("the number of possible doctors: " + str(len(doctor_names)))
            names.appendRow(item)
            for name in doctor_names:
                item = QtGui.QStandardItem(str(name[0]))
                names.appendRow(item)
            self.window.listView.setModel(names)

    def query2(self):
        pass

    def query3(self):
        patients = test.query_3(self.connection)
        model = QtGui.QStandardItemModel()
        item = QtGui.QStandardItem("the number of patients: " + str(len(patients)))
        model.appendRow(item)
        for patient in patients:
            item = QtGui.QStandardItem(str(patient[0]) + ": " + str(patient[1]))
            model.appendRow(item)
        self.window.listView.setModel(model)

    def query4(self):
        income = test.query_4(self.connection)
        model = QtGui.QStandardItemModel()
        item = QtGui.QStandardItem("predicted income is: " + str(income[0][0]))
        model.appendRow(item)
        self.window.listView.setModel(model)

    def query5(self):
        doctors = test.query_5(self.connection)
        model = QtGui.QStandardItemModel()
        item = QtGui.QStandardItem("the number of great doctors: " + str(len(doctors)))
        model.appendRow(item)
        for doctor in doctors:
            item = QtGui.QStandardItem(str(doctor[0]) + ": " + str(doctor[1]))
            model.appendRow(item)
        self.window.listView.setModel(model)


    def clear_view(self):
        self.window.listView.setModel(QtGui.QStandardItemModel())

if __name__ == "__main__":
    ui = UI()
    ui.main()