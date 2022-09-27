

class Person:

    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def print_person(self):
        print('Name',self.__name)
        print('Address',self.__address)
        print('Phone',self.__phone)


class Customer(Person):

    def __init__(self, name, address, phone, customer_num, mail_list):

        Person.__init__(self, name, address, phone)

        self.__customer_num = customer_num
        self.__mail_list = mail_list

    
    def print_person(self):
        Person.print_person(self)


        print('Customer Number:',self.__cust_number)
        if self.__on_list:
            print('On Mailing list: Yes')
        else:
            print('On Mailing List: No')

            




