import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    #task_1
    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items
    
    #task_2
    def add_item_to_cheque(self, name):
        if len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in self.__item_price.keys():
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(name)
            self.__number_items+=1
    
    #task_3
    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(name)
            self.__number_items-=1

    #task_4
    def check_amount(self):
        total =[]
        for n in self.__name_items:
            total.append(self.__item_price[n])
        if len(total) > 10:
            return print(sum(total)*0.9)
        else:
            return print(sum(total))
    
    #task_5
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for n in self.__name_items:
            if self.__tax_rate[n] == 20:
                twenty_percent_tax.append(n)
                total.append(self.__item_price[n])
        if len(self.__name_items) > 10:
            return sum(total)*0.2*0.9
        else:
            return sum(total)*0.2
    
    #task_6
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for n in self.__name_items:
            if self.__tax_rate[n] == 10:
                ten_percent_tax.append(n)
                total.append(self.__item_price[n])
        if len(self.__name_items) > 10:
            return sum(total)*0.1*0.9
        else:
            return sum(total)*0.1
    
    #task_7
    def total_tax(self):
        return self.twenty_percent_tax_calculation()+self.ten_percent_tax_calculation()

    #task_8
    @staticmethod
    def get_telephone_number(telephone_number):
        try:
            int(telephone_number)
        except ValueError:
            raise ValueError('Необходимо ввести цифры')
        if len(str(telephone_number)) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')          
        else:
            return print(f'+7{telephone_number}')

test_collection = OnlineSalesRegisterCollector()
#task_2
#test_collection.add_item_to_cheque('чипсы')
test_collection.add_item_to_cheque('кола')
test_collection.add_item_to_cheque('кола')
test_collection.add_item_to_cheque('кефир')
test_collection.add_item_to_cheque('кола')
test_collection.add_item_to_cheque('кола')
test_collection.add_item_to_cheque('кефир')
test_collection.add_item_to_cheque('кефир')
test_collection.add_item_to_cheque('кола')
test_collection.add_item_to_cheque('кефир')
test_collection.add_item_to_cheque('кола')
test_collection.add_item_to_cheque('кефир')
#task_3
test_collection.delete_item_from_check('кола')
#task_1
print(test_collection.name_items)
print(test_collection.number_items)
#task_4
test_collection.check_amount()
#task_5
print(test_collection.twenty_percent_tax_calculation())
#task_6
print(test_collection.ten_percent_tax_calculation())
#task_7
print(test_collection.total_tax())
#task_8
test_collection.get_telephone_number("8005553535")
test_collection.get_telephone_number(8005553535)