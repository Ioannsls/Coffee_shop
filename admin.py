from DataBase import Data
import threading
lock = threading.RLock()

class admin_options:
    def choose_option(self):
        print('Выберете дальнейшее действие:\n 1. Работники\n 2. Продажи\n 3. Склад\n 4. Закончить работу\n')
        for i in range(1, 4):
            activities = input()
            match activities:
                case 'Работники':
                    self.workers()
                    break
                case 'Продажи':
                    self.purchases()
                    break
                case 'Склад':
                    self.quantity()
                    break
                case 'Закончить работу':
                    self.admin_end_works()
                    break
                case _:
                    print('Неверное действие. Попробуйте ещё раз')

    def workers(self):
        data = Data()
        print('Выберете дальнейшее действие:\n 1. Посмотреть\n 2. Добавить работника\n 3. Удалить работника\n')
        for i in range(1, 4):
            activities = input()
            match activities:
                case 'Посмотреть':
                    print(data.select_workers(),'\n')
                    break
                case 'Добавить работника':
                    self.insert_worker()
                    break
                case 'Удалить работника':
                    self.delete_worker()
                    break
                case _:
                    print('Неверное действие. Попробуйте ещё раз')
        self.choose_option()


    def insert_worker(self):
        data = Data()
        print('Введите имя\n')
        name = input()
        print('Введите фамилию\n')
        surname = input()
        print('Введите отчество\n')
        middlename = input()
        with lock:
            data.insert_worker_seller(name, surname, middlename)
            result = data.select_worker_id(name, surname, middlename)
        print('Регион\n')
        state = input()
        print('Город\n')
        city = input()
        print('Улицу\n')
        street = input()
        print('Номер дома\n')
        house = input()
        with lock:
            data.insert_worker_adress(result, state, city, street, house)
        self.choose_option()

    def delete_worker(self):
        data = Data()
        print('Введите имя\n')
        name = input()
        print('Введите фамилию\n')
        surname = input()
        print('Введите отчество\n')
        middlename = input()
        with lock:
            data.delete_worker_sellers(name, surname, middlename)
            result = data.select_worker_id(name, surname, middlename)
            data.delete_worker_adress(result)
        print('Удалено успешно')
        self.choose_option()


    def purchases(self):
        global worker_sel_id, product_sel_id
        data = Data()

        print('Выберете фильтр. Если вы не хотите фильтровать по соответствующему полю, напишите 0 а если хотите - запишите значение\n')
        print('Кассир -- \n')
        worker = input()
        if worker != '0':
            worker_sel_id = data.select('id', 'Sellers', "sellers.surname = '{}'".format(worker))
        print('Продукт -- \n')
        product = input()
        if product != '0':
            product_sel_id = data.select('id', 'Products', "ProductName = '{}'".format(product))
        print('Начальная дата --\n')
        start_date = input()

        if start_date == '0':
            if worker != '0' and product == '0':
                with lock:
                    print(data.select_purch('*', 'Purchases',
                                            'PearsonID = {}'.format(
                                                worker_sel_id)))
            if worker == '0' and product != '0':
                with lock:
                    print(data.select_purch('*', 'Purchases',
                                            'ProductID = {}'.format(
                                                product_sel_id)))
            if worker != '0' and product != '0':
                with lock:
                    print(data.select_purch('*', 'Purchases',
                                            'PearsonID = {} AND ProductID = {}'.format(
                                                worker_sel_id, product_sel_id)))
        else:
            print('Конечная дата* --\n')
            end_date = input()

            if worker != '0' and product == '0':
                with lock:
                    print(data.select_purch('*', 'Purchases',
                                            'PearsonID = {} AND date BETWEEN "{}" AND "{}"'.format(worker_sel_id,start_date, end_date)))
            if worker == '0' and product != '0':
                with lock:
                    print(data.select_purch('*', 'Purchases',
                                            'ProductID = {} AND date BETWEEN "{}" AND "{}"'.format(product_sel_id,start_date, end_date)))
            if worker != '0' and product != '0':
                with lock:
                    print(data.select_purch('*', 'Purchases',
                                            'PearsonID = {} AND ProductID = {} AND date BETWEEN "{}" AND "{}"'.format(
                                                worker_sel_id, product_sel_id, start_date, end_date)))
        self.choose_option()



    def quantity(self):
        data = Data()
        print('Выберете дальнейшее действие:\n 1. Посмотреть всё\n 2. Посмотреть по товарам\n')
        for i in range(1, 3):
            activities = input()
            match activities:
                case 'Посмотреть всё':
                    with lock:
                        print(data.select_quantity())
                    break
                case 'Посмотреть по товарам':
                    print('Введите название продукта\n')
                    product = input()
                    with lock:
                        data.select_quantity_prod(product)
                    break
                case _:
                    print('Неверное действие. Попробуйте ещё раз')
        self.choose_option()

    def admin_end_works(self):
        print('Работа успешно завершена')
        return
