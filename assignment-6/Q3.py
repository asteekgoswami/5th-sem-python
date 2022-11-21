# 3. Write a program to create a class Electricity_bill with data members bill_id, customer_name, meter_no, no_of_units, total_amount, previous_balance and member functions compute_bill(), which computes the monthly electricity bill based on the following criteria:
# Units Cost per unit (Rs.)
# 200 5/-
# 200-400 7/-
# 400-800 10/-
# 800-1600 13/-
# Above 1600 15/-
# If the previous bill is not paid then previous bill along with penalty.


class Electricity_bill:
    def __init__(self) -> None:
        self.bill_id=''
        self.customer_name=''
        self.meter_no=''
        self.num_of_unit=0
        self.total_amount=0
        self.prev_bal=0

    def compute_bill(self):
        if self.num_of_unit<200:
            self.total_amount=self.num_of_unit*5 + self.prev_bal

        elif self.num_of_unit>=200 and self.num_of_unit<400:
            self.total_amount=self.num_of_unit*7 + self.prev_bal

        elif self.num_of_unit>=400 and self.num_of_unit<800:
            self.total_amount=self.num_of_unit*10 + self.prev_bal

        elif self.num_of_unit>=800 and self.num_of_unit<1600:
            self.total_amount=self.num_of_unit*13 + self.prev_bal
        
        else:
            self.total_amount=self.num_of_unit*15 + self.prev_bal

    def getdata(self):
        print("-"*30)
        self.bill_id=input("Enter the bill id : ")
        self.customer_name=input("Enter the customer name : ")
        self.meter_no=input("Enter the meter number : ")
        self.num_of_unit=int(input("Enter the number of units : "))
        self.prev_bal=int(input("Enter the previous balance : "))
        paid=int(input("Previous balance is paid(1) or not paid (0) : "))
        if paid==1:
            self.prev_bal=0
        print("-"*30)

    def display(self):
        self.compute_bill()

        print("-"*30)
        print("Bill id : ",self.bill_id)
        print("Meter number : ",self.meter_no)
        print("Customer name : ",self.customer_name)
        print("Number of units : ",self.num_of_unit)
        print("Total amount : ",self.total_amount)
        print("-"*30)


ob=Electricity_bill()
ob.getdata()
ob.display()

        
        
    
