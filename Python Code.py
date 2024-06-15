import sys
import os
import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6 import QtCharts
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QMainWindow
from data.compute_statistics import compute_statistics
from data.delete_stats_info import delete_stats_info
from data.fetch_company_info import fetch_company_info
from data.fetch_stats_info import fetch_stats_info
from data.insert_stats_info import insert_stats_info
from data.update_stats_info import update_stats_info
from models.ItemsModel import ItemsModel
from dialogs.edit_dialog_code import EditDialog
from mainwindow import Ui_MainWindow
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from statistics import *

from dialogs.update_dialog import UpdateDialog

dirname = os.path.dirname(PySide6.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


class MainWindow(QMainWindow):
    #Функция инициализации программы
    def __init__(self):
        super(MainWindow, self).__init__()
        #Инициализация интерфейса
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.engine = create_engine("sqlite+pysqlite:///mydatabase.db", echo=True)
        self.model = ItemsModel()

        self.ui.tblItems.setModel(self.model)
        #визуальная функция для статичной таблицы
        self.ui.tblItems.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        #Для подгрузки статистики в нашу программу
        self.load_companies()
        self.load_stats()

        #реагирование функций, если на кнопки нажимают
        self.ui.cmbCompanies.currentIndexChanged.connect(self.load_stats)
        self.ui.btnAdd.clicked.connect(self.on_btnAdd_click)
        self.ui.btnRemove.clicked.connect(self.on_btnRemove_click)
        self.ui.btnEdit.clicked.connect(self.on_btnEdit_click)
    #функция вызова статистики
    def show_statistics(self):
        text = compute_statistics(self.rows, self.companies)
        #в папке data происходят главыне вычисления, пока здесь функция вызывается и потом выводится
        self.ui.lbStatistics.setText(text)
    #фукнция для кнопки изменения
    def on_btnEdit_click(self):
        item = self.ui.tblItems.currentIndex()
        init_data = item.data(QtCore.Qt.ItemDataRole.UserRole)

        dialog = UpdateDialog(self.companies, init_data)
        #определяет успешно было завершенно диалоговое окно или нет(результат 1 или 0)
        r = dialog.exec()
        
        #если 0( диалоговое окно закрыли или нажали кнопку отмена, то ничего не делаем)
        if r == 0:
            return
        #В противном же случае мы вызываем функцию замены старых данных на новых в нашей БД
        data = dialog.get_data()
        #Инициация Сессии при загрузке функции
        with Session(self.engine) as s:

            update_stats_info(s,data, init_data)
        #после выполнения функции замены данных вызываем подругзку статистики, чтобы сразу же увидеть результат
        self.load_stats()
    #функция загрузки статистики выводит данные из базы данных в нашу таблицу для просмотра пользователя
    def load_stats(self):
        #Данный блок проверяет нужно ли вывести статистику на определнную компанию, в случае
        #если никакая компания не задана, то выводит сразу все
        companies_data =  self.ui.cmbCompanies.currentData()
        if companies_data :
            company_id =  self.ui.cmbCompanies.currentData().id
        else:
            company_id = 0
        #Массив строчек, в который заносятся данные о компании
        self.rows = []
        with Session(self.engine) as s:
            rows = fetch_stats_info(s,company_id)

            for r in rows:
                self.rows.append(r)
        #загруженная информация в строчки используется для правильного вывода потом её в таблицу
        self.model.setItems(self.rows)
        #используем информацию о компании для вывода статистики
        self.show_statistics()
        self.draw_line_chart()
        self.draw_pie_chart()
        self.draw_bar_chart()
    #кнопка удаления данных
    def on_btnRemove_click(self):
        item = self.ui.tblItems.currentIndex()
        data = item.data(QtCore.Qt.ItemDataRole.UserRole)
        #Окно с подверждением действия
        r = QMessageBox.question(self, "Подтверждение", "Точно ли хотите удалить запись?")
        #если ответ положительный, то данные удаляются, иначе отмена
        if r == QMessageBox.StandardButton.No:
            return

        with Session(self.engine) as s:
            delete_stats_info(s, data)

        self.load_stats()
    #Кнопка добавления новых значений в базу данных
    def on_btnAdd_click(self):
        item = self.ui.tblItems.currentIndex()
        init_data = item.data(QtCore.Qt.ItemDataRole.UserRole)
        #выход из диалогового окна отменяет загрузку данных в дб
        dialog = EditDialog(self.companies, init_data)
        r = dialog.exec()
        if r == 0:
            return
        #иначе загружаем их
        data = dialog.get_data()
        with Session(self.engine) as s:
            insert_stats_info(s, data)

        self.load_stats()

    #функция подгрузки имён компаний
    def load_companies(self):
        #словарик для хранения имён компаний
        self.companies = {}

        with Session(self.engine) as s:
            rows = fetch_company_info(s)

            for r in rows:
                self.companies[r.id] = r
        self.ui.cmbCompanies.addItem("-")

        for r in self.companies.values():
            self.ui.cmbCompanies.addItem(r.name, r)

        self.model.setCompany(self.companies)
        
    def draw_line_chart(self):
        # заводим словарик под группировку по регионам
        self.data_by_companies = {}
        
        # группируем по регионам
        for row in self.rows:
            items = self.data_by_companies.setdefault(row.company_id, [])
            items.append(row)
        
        # создаем объект графика
        chart = QtCharts.QChart()
        
        # для каждого региона
        for company_id, company_data in self.data_by_companies.items():
            # вытаскиваем имя региона
            company_name = self.companies[company_id].name
            
            # создаем последовательность точек для вывода 
            series = QtCharts.QLineSeries()
            # даем ей название
            series.setName(company_name)
            # включаем отображение точек
            series.setPointsVisible(True)
            series.setMarkerSize(4)
            
            # заполняем последовательность точек
            for row in company_data:
                series.append(row.clients, row.profit)
            
            # добавляем последовательность точек на график
            chart.addSeries(series)
        
        # активируем отображение осей
        chart.createDefaultAxes()
        chart.axisX().setTitleText("Клиенты")
        chart.axisX().setLabelFormat("%i")
        chart.axisX().setMax(chart.axisX().max() + 1)
        chart.axisX().setMin(chart.axisX().min() - 1)
        
        chart.axisY().setLabelFormat("%i")
        chart.axisY().setTitleText("Профит")
        chart.axisY().setMax(chart.axisY().max() + 50)
        chart.axisY().setMin(chart.axisY().min() - 1)
        
        # подключаем график к форме
        self.ui.QChartView1.setChart(chart)

    #Круговая диаграмма
    def draw_pie_chart(self):
        #Создаём словарик
        self.data_by_companies = {}
        #Группируем данные по айди компаний
        for row in self.rows:
            items = self.data_by_companies.setdefault(row.company_id, [])
            items.append(row)
        series = QtCharts.QPieSeries()
        #вывод диаграммы со значениями
        for company_id, company_data in self.data_by_companies.items():
            company_name = self.companies[company_id].name
            avg = int(mean([i.clients for i in company_data]))
            series.append(f"{company_name}", avg)
        #Подписи осей
        series.setLabelsVisible()
        #создание секторов
        chart = QtCharts.QChart()
        #Добавляем серию нашему графику
        chart.addSeries(series)
        #вывод графика на окно Чартвью2
        self.ui.QChartView2.setChart(chart)

    #Горизонтальная столбиковая диаграммы, гистрограммы
    def draw_bar_chart(self):
        #словарик
        self.data_by_companies = {}

        people = set()
        #группируем данные по компаниям и клиентам
        for row in self.rows:
            items = self.data_by_companies.setdefault(row.company_id, {})
            items[row.clients] = row.profit
            people.add(row.clients)

        people = sorted(people)

        series = QtCharts.QHorizontalStackedBarSeries()
        #вывод диаграммы со значениями
        for company_id, company_data in self.data_by_companies.items():
            company_name = self.companies[company_id].name
            bar_set = QtCharts.QBarSet(company_name)
            for clients in people:
                value = int(company_data.get(clients, 0))
                bar_set.append(value)
            #установка цвета столбиков
            bar_set.setLabelColor("#0d0082")
            series.append(bar_set)
        
        series.setLabelsVisible()
        series.setLabelsPrecision(20)

        chart = QtCharts.QChart()
        #анимация для появления
        chart.setAnimationOptions(QtCharts.QChart.AnimationOption.SeriesAnimations)
        chart.addSeries(series)
        #Создание осей
        chart.createDefaultAxes()       
        axis = QtCharts.QBarCategoryAxis()
        axis.append([str(i) for i in people])
        chart.setAxisY(axis)
        series.attachAxis(axis)

        self.ui.QChartView3.setChart(chart)


#Определяет блок кода, который запускается при компилировании
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())