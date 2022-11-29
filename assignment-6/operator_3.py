class distance:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    
    def __gt__(self,obj):
        self.mag=self.a**2+self.b**2
        obj.mag=obj.a**2+obj.b**2
        return (self.mag>obj.mag)
    
d1=distance(14,20)
d2=distance(18,15)
print("Magnitude of d1 > d2 : ",end=" ")
print(d1>d2)