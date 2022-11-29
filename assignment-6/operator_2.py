class Number:
    def __init__(self,num) -> None:
        self.num=num
    
    def __and__(self,obj):
        num=self.num & obj.num
        return Number(num)
    
    def display(self):
        print(self.num)

    
n1=Number(4)
n2=Number(25)
n3=n1&n2
print("Bitwise & of 4 and 25 are : ",end=" ")
n3.display()