'''
class Desktop:
    def __init__(self, cpu, disk, power):
        self.cpu = cpu
        self.disk = disk
        self.power = power
    def start(self):
        print("您的電腦已開啟")
class Notebook:
    def __init__(self, cpu, disk, display, battery):
        self.cpu = cpu
        self.disk = disk
        self.display = display
        self.battery = battery
    def start(self):
        print("您的電腦已開啟")
class Phone:
    def __init__(self, cpu, disk, display, battery, camera ):
        self.cpu = cpu
        self.disk = disk
        self.display = display
        self.battery = battery
        self.camera = camera
    def start(self):
        print("您的手機已開啟")
# 指定物件所屬類別
MacbookPro = Notebook('M1','256GB',13,'23000mAh')
iMac = Desktop('i7 10700','1TB','110V')
iPhone12 = Phone('A14','256GB',6.1,'2000mAh',3)
# 執行物件方法

MacbookPro.start()
iMac.start()
iPhone12.start()
'''

class Device:
    def __init__(self,name):
        self.name=name
    def start(self):
        print(f'您的{self.name}已經開啟')
class Desktop(Device):
    def __init__ (self,name,cpu,disk,power):
        self.name=name
        self.cpu = cpu
        self.disk = disk
        self.power=power
    def start(self):
        super().start() #執行父類別的功能
        print('系統已啟動windows 10')
        print('------------------------')
class Notebook(Device):
    def __init__ (self, name,cpu,disk,display, battery):
        self.name=name
        self.cpu = cpu
        self.disk = disk
        self.display = display
        self.battery = battery
    def start(self):
        super().start()
        print('系統已啟動macOS Big sur')
        print('------------------------')
class Phone(Device):
    def __init__ (self, name,cpu,disk,display, battery, camera):
        self.name=name
        self.cpu = cpu
        self.disk = disk
        self.display = display
        self.battery = battery
        self.camera = camera
    def start(self):
        super().start()
        print('系統已啟動ios 14')
        print('------------------------')
# 指定物件所屬類別
A = Notebook('MacbookPro','M1','256GB',13,'23000mAh')
B = Desktop('Xeno','i7 10700','1TB','110V')
C= Phone('iPhone12','A14','256GB',6.1,'2000mAh',3)
# 執行物件方法

A.start()
B.start()
C.start()