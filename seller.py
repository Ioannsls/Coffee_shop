from DataBase import Data
from tkinter import *
from functools import partial
import threading
lock = threading.RLock()
global window

class seller_options:
    # def __init__(self, text):
    #     self.text = text

    def get_surname(self, txt):
        data = Data()
        surname = txt.get()
        with lock:
            start_date = data.select_time()
        data.begin_work(surname, start_date)

    def put_surname(self, txt):
        data = Data()
        surname = txt.get()
        with lock:
            end_date = data.select_time()
        data.end_work(surname, end_date)

    def get_product(self, product_txt, quantity_txt):
        data = Data()
        product = product_txt.get()
        quantity = quantity_txt.get()
        with lock:
            product_sel_id = data.select("id", "Products", "ProductName = '{}'".format(product))
            time = data.select_time()
            data.insert(product_sel_id, quantity, time)
        product_txt.destroy()
        quantity_txt.destroy()

    def choose_option(self, window):
        # window.destroy()
        lbl = Label(window, text="Выберете дальнейшее действие:", font=("Arial Bold", 14))
        lbl.grid(column=0, row=0)
        btn = Button(window, text="Начать смену", command=partial(self.seller_begin_work, window))
        btn.grid(column=0, row=1)
        btn2 = Button(window, text="Продать", command=partial(self.seller_sell, window))
        btn2.grid(column=0, row=2)
        btn3 = Button(window, text="Закончить смену", command=partial(self.seller_end_work, window))
        btn3.grid(column=0, row=3)


    def seller_begin_work(self, window):
        data = Data()
        lbl = Label(window, text="Введите фамилию", font=("Arial Bold", 14))
        lbl.grid(column=0, row=4)
        txt = Entry(window, width=10)
        txt.grid(column=1, row=4)
        btn = Button(window, text="Отправить", command=partial(self.get_surname, txt))
        btn.grid(column=2, row=4)
        lbl = Label(window, text="Выберете дальнейшее действие:", font=("Arial Bold", 14))
        lbl.grid(column=0, row=5)
        btn2 = Button(window, text="Продать", command=partial(self.seller_sell, window))
        btn2.grid(column=0, row=6)
        btn3 = Button(window, text="Закончить смену", command=partial(self.seller_end_work, window))
        btn3.grid(column=0, row=7)
        # match activities:
        #     case 'Продать':
        #         self.seller_sell()
        #     case 'Закончить смену':
        #         end = self.seller_end_work()

    def seller_sell(self, window):
        lbl = Label(window, text="Введите название продукта:", font=("Arial Bold", 14))
        lbl.grid(column=0, row=8)
        lbl = Label(window, text="Введите количество:", font=("Arial Bold", 14))
        lbl.grid(column=0, row=9)
        product = Entry(window, width=10)
        product.grid(column=1, row=8)
        quantity = Entry(window, width=10)
        quantity.grid(column=1, row=9)
        btn = Button(window, text="Отправить", command=partial(self.get_product, product, quantity))
        btn.grid(column=2, row=9)
        btn3 = Button(window, text="Продолжить", command=partial(self.seller_sell, window))
        btn3.grid(column=3, row=9)
        # print('Введите название продукта\n')
        # product = input()

        # print('Введите количество\n')
        # quantity = input()

        # print('Покупка успешно проведена\n')
        # print('Если хотите закончить введите END\n')
        # print('Если хотите продолжить введите C\n')
        # next = input()
        # match next:
        #     case 'C':
        #         self.seller_sell()
        #     case 'END':
        #         end = self.seller_end_work()

    def seller_end_work(self, window):
        global end
        lbl = Label(window, text="Введите фамилию", font=("Arial Bold", 14))
        lbl.grid(column=0, row=10)
        txt = Entry(window, width=10)
        txt.grid(column=1, row=10)
        btn = Button(window, text="Отправить", command=partial(self.put_surname, txt))
        btn.grid(column=2, row=10)
        end = 'end'
        return end
