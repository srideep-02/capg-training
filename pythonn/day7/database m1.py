class Customers:
    def _init_(self,c_id,first_name,last_name,phone,email,street,city,state,zip_code):
        
        self.c_id = c_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone =phone
        self.email=email
        self.street=street
        self.city=city
        self.state=state
        self.zip_code=zip_code
        
        
    def display(self):
        print(f" customer id is : {self.c_id} \n First name is : {self.first_name} \n Lasst name is : {self.last_name} \n Phone no is : {self.phone} \n Email is {self.email} \n Street is {self.street} \n City is {self.city} \n state is {self .state} \n Zip_code is {self.zip_code} ")
        
obj = Customers(101,"Harika","Sirigani",987654321,"abc@gmail.com","Ramalayam street","hyd","Ts",500075)
obj.display()
    
class Orders:
    def _init_(self,o_id,c_id,O_status,o_date,required_date,shipped_date,store_id,staff_id):
        self.o_id=o_id
        self.c_id=c_id
        self.o_status=O_status
        self.o_date=o_date
        self.required_date=required_date
        self.shipped_date=shipped_date
        self.store_id=store_id
        self.staff_id=staff_id
        
    def display1(self):
        print(f" order id:{self.o_id}\n customer_id: {self.c_id}\n order_status: {self.o_status} \n order_date:{self.o_date} \n required date:{self.required_date} \n shipped date:{self.shipped_date} \n store id:{self.store_id} \n staff id:{self.staff_id}") 
        
obj1 = Orders(202,101,"Received","29-01-2025","2-2-2025","4-02-2025",44567,102030)
obj1.display1() 
        
'''class Order_Item:
    
    
    def _init_(self,o_id,item_id,product_id,quantity,list_price,discount):
        #self.append[self,o_id,item_id,product_id,quantity,list_price,discount]
        self.o_id=o_id
        self.item_id=item_id
        self.product_id = product_id
        self.quantity = quantity
        self.list_price = list_price
        self.discount = discount
       
        
    def display(self,*args):
        print(f" Item id is : {self.item_id} \n Product id is : {self.product_id}  \n quantity is : {self.quantity} \n list price is : {self.list_price} \n discount is : {self.discount}")
        
obj2 = Order_Item(202,303,404,10,500,100)

obj2.display()'''
        
class Order_Item:
    
    def display3(self,*args):
        Label = ["o_id","item_id","product_id","quantity","list_price","discount"]
        for Label,value in zip(Label, args):
            print(f"{Label} is {value}")
        
        
        return args

obj2 = Order_Item()
obj2.display3(202, 303, 10, 500, 100)