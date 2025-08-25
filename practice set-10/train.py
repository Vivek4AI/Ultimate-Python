import random

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self,fro,to):
        print(f"Ticket is booked in trainNo : {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train number {self.trainNo} is running on time")

    def getFare(self,fro,to):
        print(f"Ticket fare in trainNo : {self.trainNo} from {fro} to {to} {random.randint(222,55555)}")

t = Train(123456)
t.book("Rampur","Delhi")
t.getStatus()
t.getFare("Rampur","Delhi")