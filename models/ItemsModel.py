from PySide6 import QtCore
#класс для вывовад всех данных о компаний в виде таблицы
class ItemsModel(QtCore.QAbstractTableModel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        #библиотека для данных о компаний и словарик для хранения имён компаний
        self.items = []
        self.companies = {}

    def setItems(self,items):
        #бегин и ресет для коррекотного вывода данных
        self.beginResetModel()
        self.items = items
        self.endResetModel()

    def setCompany(self,companies):
        self.beginResetModel()
        self.companies = companies
        self.endResetModel()
    #количество рядов определяется по длине массива айтемс или количеству компаний для вывода
    def rowCount(self, *args, **kwargs) -> int:
        return len(self.items)
    #количество столбцов всегда будет 7, тк как у нас 7 столбцов...
    def columnCount(self, *args, **kwargs) -> int:
        return 7
    #функция для загрузки данных в таблицу
    def data(self, index: QtCore.QModelIndex, role: QtCore.Qt.ItemDataRole):
        if not index.isValid():
            return
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            company_info = self.items[index.row()]
            col = index.column()
            #по индексу определяется в какой столбец выводить данные
            if col == 0:
                return f'{company_info.id}'
            elif col == 1:
                company_name = self.companies[company_info.company_id].name
                return company_name
            elif col == 2:
                return f'{company_info.rating}'
            elif col == 3:
                return f'{company_info.clients}'
            elif col == 4:
                return f'{company_info.profit}'
            elif col == 5:
                return f'{company_info.age}'
            elif col == 6:
                return f'{company_info.cover}'
        elif role == QtCore.Qt.ItemDataRole.UserRole:
            return self.items[index.row()]
    #функция для именования заголовоков столбцов
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: QtCore.Qt.ItemDataRole):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                return {
                    #имена столбцов для вывода
                    0: "id",
                    1: "Компания",
                    2: "Рейтинг",
                    3: "Клиенты",
                    4: "Доход",
                    5: "Возраст"
                }.get(section)
