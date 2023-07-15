from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_guest_registration(object):
    def setupUi(self, guest_registration):
        guest_registration.setObjectName("guest_registration")
        guest_registration.resize(795, 369)
        guest_registration.setFixedSize(795, 369)  # Set fixed window size
        guest_registration.setWindowFlags(
            guest_registration.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint & ~QtCore.Qt.WindowMinimizeButtonHint
        )  # Disable maximize and minimize buttons

        # Set dark color palette
        self.setDarkPalette()

        self.centralwidget = QtWidgets.QWidget(guest_registration)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 30, 751, 301))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.identitasLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.identitasLabel.setObjectName("identitasLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.identitasLabel)
        self.identitasComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.identitasComboBox.setObjectName("identitasComboBox")
        self.identitasComboBox.addItem("")
        self.identitasComboBox.addItem("")
        self.identitasComboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.identitasComboBox)
        self.noIdentitasLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.noIdentitasLabel.setObjectName("noIdentitasLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.noIdentitasLabel)
        self.noIdentitasLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.noIdentitasLineEdit.setObjectName("noIdentitasLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.noIdentitasLineEdit)
        self.namaGuestLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.namaGuestLabel.setObjectName("namaGuestLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.namaGuestLabel)
        self.namaGuestLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.namaGuestLineEdit.setObjectName("namaGuestLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.namaGuestLineEdit)
        self.typeRoomLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.typeRoomLabel.setObjectName("typeRoomLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.typeRoomLabel)
        self.typeRoomComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.typeRoomComboBox.setObjectName("typeRoomComboBox")
        self.typeRoomComboBox.addItem("")
        self.typeRoomComboBox.addItem("")
        self.typeRoomComboBox.addItem("")
        self.typeRoomComboBox.addItem("")
        self.typeRoomComboBox.addItem("")
        self.typeRoomComboBox.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.typeRoomComboBox)
        self.alamatLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.alamatLabel.setObjectName("alamatLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.alamatLabel)
        self.alamatLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.alamatLineEdit.setObjectName("alamatLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.alamatLineEdit)
        self.kelurahanLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.kelurahanLabel.setObjectName("kelurahanLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.kelurahanLabel)
        self.kelurahanLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.kelurahanLineEdit.setObjectName("kelurahanLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.kelurahanLineEdit)
        self.kecamataLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.kecamataLabel.setObjectName("kecamataLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.kecamataLabel)
        self.kecamataLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.kecamataLineEdit.setObjectName("kecamataLineEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.kecamataLineEdit)
        self.kotaKabupatenLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.kotaKabupatenLineEdit.setObjectName("kotaKabupatenLineEdit")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.kotaKabupatenLineEdit)
        self.checkBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.checkBox)
        self.provinsiLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.provinsiLineEdit.setObjectName("provinsiLineEdit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.provinsiLineEdit)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.kotaKabupatenLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.kotaKabupatenLabel.setObjectName("kotaKabupatenLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.kotaKabupatenLabel)
        self.provinsiLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.provinsiLabel.setObjectName("provinsiLabel")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.provinsiLabel)
        guest_registration.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(guest_registration)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 795, 21))
        self.menubar.setObjectName("menubar")
        self.menuPurchase_Order = QtWidgets.QMenu(self.menubar)
        self.menuPurchase_Order.setObjectName("menuPurchase_Order")
        guest_registration.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(guest_registration)
        self.statusbar.setObjectName("statusbar")
        guest_registration.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuPurchase_Order.menuAction())

        self.retranslateUi(guest_registration)
        QtCore.QMetaObject.connectSlotsByName(guest_registration)

        self.pushButton.clicked.connect(self.showRegistrationDialog)

    def retranslateUi(self, guest_registration):
        _translate = QtCore.QCoreApplication.translate
        guest_registration.setWindowTitle(_translate("guest_registration", "MainWindow"))
        self.identitasLabel.setText(_translate("guest_registration", "Identitas"))
        self.identitasComboBox.setItemText(0, _translate("guest_registration", "KTP"))
        self.identitasComboBox.setItemText(1, _translate("guest_registration", "SIM"))
        self.identitasComboBox.setItemText(2, _translate("guest_registration", "Passport"))
        self.noIdentitasLabel.setText(_translate("guest_registration", "No Identitas"))
        self.namaGuestLabel.setText(_translate("guest_registration", "Nama Guest"))
        self.typeRoomLabel.setText(_translate("guest_registration", "Type Room"))
        self.typeRoomComboBox.setItemText(0, _translate("guest_registration", "Superior Single"))
        self.typeRoomComboBox.setItemText(1, _translate("guest_registration", "Superior Double"))
        self.typeRoomComboBox.setItemText(2, _translate("guest_registration", "Deluxe Single"))
        self.typeRoomComboBox.setItemText(3, _translate("guest_registration", "Deluxe Double"))
        self.typeRoomComboBox.setItemText(4, _translate("guest_registration", "Suite"))
        self.typeRoomComboBox.setItemText(5, _translate("guest_registration", "Junior Suite"))
        self.alamatLabel.setText(_translate("guest_registration", "Jalan"))
        self.kelurahanLabel.setText(_translate("guest_registration", "Kelurahan"))
        self.kecamataLabel.setText(_translate("guest_registration", "Kecamatan"))
        self.checkBox.setText(_translate("guest_registration", "Smoking?"))
        self.pushButton.setText(_translate("guest_registration", "Registrasi"))
        self.kotaKabupatenLabel.setText(_translate("guest_registration", "Kota/Kabupaten"))
        self.provinsiLabel.setText(_translate("guest_registration", "Provinsi"))

    def showRegistrationDialog(self):
        identitas = self.identitasComboBox.currentText()
        no_identitas = self.noIdentitasLineEdit.text()
        nama_guest = self.namaGuestLineEdit.text()
        type_room = self.typeRoomComboBox.currentText()
        alamat = self.alamatLineEdit.text()
        kelurahan = self.kelurahanLineEdit.text()
        kecamatan = self.kecamataLineEdit.text()
        kota_kabupaten = self.kotaKabupatenLineEdit.text()
        provinsi = self.provinsiLineEdit.text()

        if not identitas or not no_identitas or not nama_guest or not type_room or not alamat \
                or not kelurahan or not kecamatan or not kota_kabupaten or not provinsi:
            error_dialog = QMessageBox()
            error_dialog.setWindowTitle("Error")
            error_dialog.setText("Please fill in all the fields.")
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.addButton(QMessageBox.Ok)
            error_dialog.exec_()
        else:
            is_smoking = self.checkBox.isChecked()
            smoking_status = "Yes" if is_smoking else "No"

            message = f"Registration Details:\n\n" \
                      f"Identitas: {identitas}\n" \
                      f"No Identitas: {no_identitas}\n" \
                      f"Nama Guest: {nama_guest}\n" \
                      f"Type Room: {type_room}\n" \
                      f"Alamat: {alamat}\n" \
                      f"Kelurahan: {kelurahan}\n" \
                      f"Kecamatan: {kecamatan}\n" \
                      f"Kota/Kabupaten: {kota_kabupaten}\n" \
                      f"Provinsi: {provinsi}"

            confirm_dialog = QMessageBox()
            confirm_dialog.setWindowTitle("Confirmation")
            confirm_dialog.setText(message)
            confirm_dialog.setIcon(QMessageBox.Question)
            confirm_dialog.addButton(QMessageBox.Yes)
            confirm_dialog.addButton(QMessageBox.No)
            confirm_dialog.setDefaultButton(QMessageBox.No)
            response = confirm_dialog.exec_()

            if response == QMessageBox.Yes:
                success_dialog = QMessageBox()
                success_dialog.setWindowTitle("Registration Successful")
                success_dialog.setText("Registrasi Sukses")
                success_dialog.setIcon(QMessageBox.Information)
                success_dialog.addButton(QMessageBox.Ok)
                success_dialog.exec_()
                self.resetForm()
            else:
                pass  # Do nothing or perform any desired action

    def resetForm(self):
        self.identitasComboBox.setCurrentIndex(0)
        self.noIdentitasLineEdit.clear()
        self.namaGuestLineEdit.clear()
        self.typeRoomComboBox.setCurrentIndex(0)
        self.alamatLineEdit.clear()
        self.kelurahanLineEdit.clear()
        self.kecamataLineEdit.clear()
        self.kotaKabupatenLineEdit.clear()
        self.provinsiLineEdit.clear()

    def setDarkPalette(self):
        app.setStyle("Fusion")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.Base, QtGui.QColor(25, 25, 25))
        palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
        palette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
        palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
        palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
        app.setPalette(palette)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    guest_registration = QtWidgets.QMainWindow()
    ui = Ui_guest_registration()
    ui.setupUi(guest_registration)
    guest_registration.show()
    sys.exit(app.exec_())

