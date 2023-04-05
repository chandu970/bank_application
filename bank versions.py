class BankV1():
    BName='Jesus'
    ROI=0.07
    def __init__(self,Name,Mno,AccNo,Bal):
        self.Name  = Name
        self.Mno   = Mno
        self.AccNo = AccNo
        self.Bal   = Bal
    def Details(self):
        print(f'Name      : {self.Name}')
        print(f'Mobile No : {self.Mno}')
        print(f'Balance   : {self.Bal}')
class BankV2 (BankV1):
    def __init__(self,Name,Mno,AccNo,Bal,Mail,Aadhar):
        super().__init__(Name,Mno,AccNo,Bal)
        self.Mail   = Mail
        self.Aadhar = Aadhar
    def Details(self):
        super().Details()
        print(f'Mail Id   : {self.Mail}')
        print(f'Aadhar No :{self.Aadhar}')
class BankV3(BankV2):
    def __init__(self,Name,Mno,AccNo,Bal,Mail,Aadhar,Pan,Pin):
        super().__init__(Name,Mno,AccNo,Bal,Mail,Aadhar)
        self.Pan=Pan
        self.Pin=Pin
    def Details(self):
        super().Details()
        print(f'PanCard No: {self.Pan}')      

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
ob3=BankV3('chandu',6300509580,9705658505,50000,'jesus@gmail.com',12132425,'BINC294738',1312)
ob3.withdraw()
ob3.CheckBal()
ob3.Details()
