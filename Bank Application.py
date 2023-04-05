class Bank:
    BName='Jesus'
    ROI=0.07
    
    def __init__(self,Name,Mno,AccNo,Bal,Pin):
        self.Name = Name
        self.Mno  = Mno
        self.AccNo= AccNo
        self.Bal  = Bal
        self.Pin  = Pin
    @classmethod
    def changeROI(cls,n):
        cls.ROI=n
    def withdraw(self):
        if self.Pin==self.GetPin():
            amt=int(input('Enter ammount: '))
            if self.Bal>=amt:
                self.Bal-=amt
                print('Amount Debited Successfully!!!')
            else:
                print('insufficient Balance')
        else:
            print('Incorrect Pin')
    def CheckBal(self):
        if self.Pin==self.GetPin():
            print(f'{self.Name} Current Balance is {self.Bal}')
        else:
            print('incorrect Pin')
    @staticmethod
    def GetPin():
        return int(input('Enter Pin: '))
ob1=Bank('David',5854792164,9705658503,80000,1311)
ob2=Bank('Ganesh',6848595052,9705658504,60000,1314)
ob3=Bank('chandu',6300509580,9705658505,50000,1312)
ob1.withdraw()
ob1.CheckBal()
