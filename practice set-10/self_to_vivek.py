import random

class Train:
    def __init__(vivek, trainNo):
        vivek.trainNo = trainNo

    def book(vivek,fro,to):
        print(f"Ticket is booked in trainNo : {vivek.trainNo} from {fro} to {to}")

    def getStatus(vivek):
        print(f"Train number {vivek.trainNo} is running on time")

    def getFare(vivek,fro,to):
        print(f"Ticket fare in trainNo : {vivek.trainNo} from {fro} to {to} {random.randint(222,55555)}")

t = Train(123456)
t.book("Rampur","Delhi")
t.getStatus()
t.getFare("Rampur","Delhi")