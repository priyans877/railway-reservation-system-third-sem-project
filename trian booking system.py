from doctest import DocTestFailure


class  trian:

    def __init__(self,name,arrivel,destinattion,distance,time,fare,availableseat):
        self.name=name
        self.arrivel=arrivel
        self.destinattion=destinattion
        self.distance=distance
        self.time=time
        self.fare=fare
        self.availableseats=availableseat
        
        
    def getrj(self,detail):
        self.detail=detail
        print(f"In this train name {self.name} is departure from {self.arrivel} and reachs at the destination {self.destinattion} and cover  total distance {self.distance} in {self.time} and the total no of seat available in this train is {self.availableseats} and the fare for one person is {self.fare}\n\t************")

    def getdr(self,detail):
        self.detail=detail
        print(f"In this train name {self.name} is departure from {self.arrivel} and reachs at the destination {self.destinattion} and cover  total distance {self.distance} in {self.time} and the total no of seat available in this train is {self.availableseats} and the fare for one person is {self.fare}\n\t************")
           
    def getsp(self):
        print(f"In this train name {self.name} is departure from {self.arrivel} and reachs at the destination {self.destinattion} and cover  total distance {self.distance} in {self.time} and the total no of seat available in this train is {self.availableseats} and the fare ffor one person is {self.fare}\n\t************")

    def booking(self):
        if(self.availableseats>0):
            print(f"CONGARATS YOUR TICKET BOOKED IN TRAIN {self.name} AND YOUR SEAT NO IS {self.availableseats}")
            print(f"the remaining ticket is {self.availableseats-1}\n\t************")
            self.availableseats = self.availableseats - 1
        else:
            print("THEIR IS NO MORE AVAILABLE SEATS IN THIS TRAIN KINDLY CHAECK FOR OTHER OPTIONS OR GO FOR TATKAL")
    def cancleticket(self):
        print(f"YOUR TICKET IN TRIAN {self.name} IS SUCSESSFULLY CANCLED. AND THE REMAINING TICKET IS {self.availableseats+1}\n\t************")
        self.availableseats=self.availableseats+1

    def getstatus(self):
        print(f"   NOW THE REMAINING SEATS IN THIS TRAIN IS {self.availableseats}\n\t************")


rajdhani1=trian("RAJDHANI EXPRESS","NEW DELHI","ASANSOL","1345 KM","22 HOURS","3467 RS",360)
duranto=trian("DURANTO EXPRESS","NEW DELHI","CHENNAI","2400 KM","48 HOUR","4578 RS",467)
saptkr=trian("SAPT KRANTI","NEW DELHI","RAXAUL","875 KM","18 HOURS","454 RS",678)


hii=input("ener the trian name you want to search")
rajdhani1=hii
rajdhani1.getrj()
rajdhani1.booking()
rajdhani1.booking()
# rajdhani1.booking()
# rajdhani1.cancleticket()
rajdhani1.getstatus

duranto.getdr()
# duranto.booking()
# duranto.booking()
# duranto.booking()
# duranto.booking()
# duranto.getstatus()
# rajdhani1.booking()
# rajdhani1.getstatus()



# duranto.cancleticket()
# duranto.booking()
