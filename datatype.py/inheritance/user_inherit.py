class User():
    def __init__(self,name,email,phone,user,password,is_locked):
        self.name = name
        self.email = email
        self.phone = phone
        self.user = user
        self.password = password
        self.is_locked=is_locked
    def call_name(self):
        print("name is",self.name)

    def print_info(self):
        print("name is",self.name)
        print("email is",self.email)
        print("phone number is",self.phone)
        print("user type is:",self.user)
    def login_system(self):
        if self.is_locked:
            return("user is locked ,contact admin")
        for i in range(0,3):
            password=input(f"Enter password {i}")
            if password==self.password:
                print("logged in successfully")
                return
        self.is_locked=True
        print("max attempts exceeded,account locked")
class Employee(User):
    def __init__(self,name,email,phone,user,password,is_locked,salary):
        super().__init__(name=name,email=email,phone=phone
                         ,password=password,user=user,is_locked=is_locked)
        self.salary=salary

class Customer(User):
    def __init__(self,name,email,phone,user,password,is_locked):
        super().__init__(name=name,email=email,phone=phone
                         ,password=password,user=user,is_locked=is_locked)
        
Employed=Employee(name="Vasha",password="121",email="Vasha@vasha.com"
              ,user="Employee",salary="30000",phone="1234",is_locked=False)

Cust=Customer(name="Vasha",password="121",email="Vasha@vasha.com"
              ,user="Customer",phone="1234",is_locked=False )

Employed.call_name() 

Cust.call_name()
Employed.print_info()
Cust.print_info()
Employed.login_system()


            
            