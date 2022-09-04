import random
import datetime
class latur():
    def __init__(self,name,age,stream,mobile_no):
        self.a=name
        self.b=age
        self.c=stream
        self.d=mobile_no
    def science(self):
        a=datetime.datetime.today()
        g=a.strftime('%d-%B-%Y/%I:%M%p')
        b=random.randint(1,100)
        with open("science_student.txt",'w')as f:
            f.write(f'\nRoll no:-{b}\nName:-{self.a}\nAge:{self.b}\nAddress:-{self.c}\nMobile_no:-{self.d}\nAdmission on:-{g}\n\n')
        print("Yuor addmission is confirm in science stram on:-",g)
    def commerce(self):
        a=datetime.datetime.today()
        g=a.strftime('%d-%B-%Y/%I:%M%p')
        b=random.randint(1,100)
        with open("commerce_student.txt",'w')as f:
            f.write(f'\nRoll no:-{b}\nName:-{self.a}\nAge:{self.b}\nStream:-{self.c}\nMobile_no:-{self.d}\n\n')
        print("Yuor addmission is confirm in commerce stream on:-",g)
    def list1(self,n1):
        if n1 == 1:
            with open('science_student.txt','r')as f:
                res=f.read()
                print(res)
        elif n1== 2:
             with open('commerce_student.txt','r')as f:
                res=f.read()
                print(res)
        
if __name__=="__main__":
    a=input("Enter your name:-")
    b=input("Enter your age:-")
    c=input("Enter your full address:-")
    d=input("Enter your 10 digit mobile number :-")
    obj=latur(a,b,c,d)
    n=int(input("Enter your choice for admission:-\n1]Science\n2]commerce"))
    if n == 1:
        obj.science()
    elif n == 2:
        obj.commerce()
    lst=input("Do you want to see list[y/n]:--")
    if lst == 'y':
        obj.list1(int(input("Enter the choice:-\n1]science\n2]commerce:---")))
    elif lst == 'n':
        pass