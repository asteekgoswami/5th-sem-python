# Write a program to illustrate the concept of overloading of arithmetic '+' operator
class complex:
    def __init__(self,real,img) -> None:
        self.real=real
        self.img=img
    
    def __add__(self,obj):
        real=self.real+obj.real
        img=self.img+obj.img
        return (complex(real,img))
    
    def display(self):
        print(self.real,"+ i",self.img)
    

c1=complex(2,2)
c2=complex(3,3)
c1.display()
c2.display()
c3=c1+c2
print("Sum is : ",end="")
c3.display()