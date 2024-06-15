from PySide6.QtWidgets import QDialog
from dialogs.edit_dialog import Ui_Dialog
from PySide6.QtWidgets import QMessageBox
#класс для кнопки по изменению данных
class EditDialog(QDialog):
    def __init__(self, companies, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        #определяют если диалоговое окно было отменено или успешно завершенно
        self.ui.btnAdd.clicked.connect(self.accept)
        self.ui.btnCancel.clicked.connect(self.reject)

        #окошечко для выбора компании у которой хотим отредактировать данные
        for r in companies.values():
            self.ui.cmbCompany.addItem(r.name,r)
        #возвращает данные выбранной компании для редактирования
    def get_data(self):
        #Проверка входит ли у нас в данные тока целые числа или нет
        if (self.ui.txtRating.text().isdigit() and self.ui.txtClient.text().isdigit() and self.ui.txtProfit.text().isdigit() and self.ui.txtAge.text().isdigit()) == False:
            return QMessageBox.warning(self, "Внимание", "В программу нельзя добавлять не целые значения!")
            
        return {
            "company_id":self.ui.cmbCompany.currentData().id,
            "rating":self.ui.txtRating.text(),
            "clients":self.ui.txtClient.text(),
            "profit":self.ui.txtProfit.text(),
            "age":self.ui.txtAge.text(),
            "cover":self.ui.txtCover.text()
        }

