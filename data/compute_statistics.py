from statistics import mean
#Функция для вычисления статистики
def compute_statistics(rows, companies):
        #обозначение максимального и минимального значения из раздела со значениями клиентов
        max_row = max(rows, key=lambda row: float(row.clients))
        min_row = min(rows, key=lambda row: float(row.clients))
        avg_clients = int(mean([i.clients for i in rows]))
        #Присвоение имён к компаниям с меньшим/наибольшим количеством клиентов
        max_company_name = companies[max_row.company_id].name
        min_company_name = companies[min_row.company_id].name
        #Заготовленный текст с переменными, которые ссылаются на занчения из базы данных
        text = f"""
        Наибольший показатель числености клиентов составил 
        <br> <b style="color: #f542c8; font-size: 16px">{max_row.clients}</b> человека при доходе  <b style="color: #4290f5">{max_row.profit}</b> в компании <u><b>{max_company_name}</b></u>
        <hr>
        Наименьший показатель числености клиентов составил 
        <br> <b style="color: #f542c8; font-size: 16px">{min_row.clients}</b> человека при доходе <b style="color: #4290f5">{min_row.profit}</b> в компании <u><b>{min_company_name}</b></u>
        <hr>
        Среднее значение населения составило: <span style="color: #f542c8">{avg_clients} человека</span>
        """
        #Возвращаем заготовленный текст в главный код
        return text