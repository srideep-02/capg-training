class customers:
    def __init__(cust,cust_id,password,first_name,last_name,phone,email,city,state,zip_code):
        cust.cust_id=cust_id
        cust.password=password
        cust.first_name=first_name
        cust.last_name=last_name
        cust.phone=phone
        cust.email=email
        cust.city=city
        cust.state=state
        cust.zip_code=zip_code
        
    def display(cust):
        print(f"Customer id{cust.cust_id} ,2{cust.password},3{cust.first_name},4{cust.last_name},5{cust.phone},6{cust.email},7{cust.city},8{cust.state},9{cust.zip_code}")
# obj=customers(1,2222,"srideep","akula",987654321,"qwerty@123","ssssss","tttttt",12345)
# obj.display()
class orders():
    def __init__(ord,order_id,customer_id,order_status,ordered_date,required_date,shipped_date,store_id,staff_id):
        ord.customer_id=customer_id
        ord.order_id=order_id
        ord.order_status=order_status
        ord.ordered_date=ordered_date
        ord.required_date=required_date
        ord.shipped_date=shipped_date
        ord.store_id=store_id
        ord.staff_id=staff_id
        
    def display(ord):
        print(f"ordered id {ord.order_id},2{ord.customer_id},3{ord.order_status},4{ord.ordered_date},5{ord.shipped_date},6{ord.store_id},7{ord.staff_id}")
obj1=orders(2,1,"out for delivery","21-25-2005","27-25-2005","29-25-2005",22,44)
obj1.display()
