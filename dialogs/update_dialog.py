from dialogs.edit_dialog_code import EditDialog

class UpdateDialog(EditDialog):
    def __init__(self, companies, init_data, *args, **kwargs) -> None:
        super().__init__(companies, *args, **kwargs)

        self.ui.btnAdd.setText('Изменить')
        self.ui.cmbCompany.setEnabled(False)

        company_name = companies[init_data.company_id].name
        self.ui.cmbCompany.setCurrentText(company_name)

        #конвертация значений из базы данных в текст для успешного их редактирования 
        self.ui.txtRating.setText(str(init_data.rating))
        self.ui.txtClient.setText(str(init_data.clients))
        self.ui.txtProfit.setText(str(init_data.profit))
        self.ui.txtAge.setText(str(init_data.age))
        self.ui.txtCover.setText(str(init_data.cover))
