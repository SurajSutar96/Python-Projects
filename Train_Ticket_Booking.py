import random
class Train:
    
    def __init__(self,num):
        self.num=num
        
    def Reservation(self):
        self.result=[]
        self.identity=[]
        for i in range(0,self.num):
            print(f"Please enter the details for <<< {i} >>> no seat")
            self.a=input("Please Enter your full name:-")
            x=input("Enter your aadhar card numer:-")
            self.b=random.randint(1,100)
            self.result.append({self.b:self.a})
            self.identity.append({self.b:self.a})
            self.identity.append({"addhar no":x})
        print("Congratulations,Your reservation is Done, Your seat number with Name:-",self.result)
    def Local(self):
        n=100
        a=n-self.num
        if a>0:
            print(f'Congratulations, You are successfully book your {self.num} tickets \n And the total remaining seats are {a}')
        elif a<=0:
            print(f"Oops! Sorry you are late seats are full")
    def Identity(self):
        print(f"The identity of reserved person :- {self.identity}")
        
        
if __name__ == "__main__":
    obj=Train(int(input("Enter the Total number of tickets you want to book:- ")))
    a=int(input(" 1] Reservation \n 2] Local \n Enter the choice for ticket :-"))
    if a == 1:
        obj.Reservation()
        print("*"*88)
        obj.Identity()
    if a == 2:
        obj.Local()
    