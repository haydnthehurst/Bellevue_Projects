
class Vehicle:

#constructor
    def __init__(self,make,model,color,fuelType,options):
        self.make=make
        self.model=model
        self.color=color
        self.fuelType=fuelType
        self.options=options

#get methods
    def getMake(self):
        return self.make
    def getModel(self):
        return self.model
    def getColor(self):
        return self.color
    def getFuelType(self):
        return self.fuelType
    def getOptions(self):
        return self.options

#car child class
class Car(Vehicle):

#another constructor
    def __init__(self,make,model,color,fuelType,options,engineSize,numDoors):
        Vehicle.__init__(self,make,model,color,fuelType,options)#calling super class constructor
        self.engineSize=engineSize
        self.numDoors=numDoors

#more get methods
    def getEngineSize(self):
        return self.engineSize
    def numDoors(self):
        return self.numDoors

#PRINT
    def printDetails(self):
        print("Car Make : ",self.make)
        print("Car model : ",self.model)
        print("Car Color : ",self.color)
        print("Car Fuel Type : ",self.fuelType)
        print("car Options : ",self.options)
        print("Car Engine Size : ",self.engineSize)
        print("Car Number of Doors :",self.numDoors)

#truck child class
class Pickup(Vehicle):

#yet another constructor
    def __init__(self,make,model,color,fuelType,options,cabStyle,bedLength):
        Vehicle.__init__(self,make,model,color,fuelType,options)#calling super class constructor
        self.cabStyle=cabStyle
        self.bedLength=bedLength

#yet another get method
    def getCabStyle(self):
        return self.cabStyle
    def getBedLength(self):
        return self.bedLength

#MORE PRINT
    def printDetails(self):
        print("Pickup Make : ",self.make)
        print("Pickup model : ",self.model)
        print("Pickup Color : ",self.color)
        print("Pickup Fuel Type : ",self.fuelType)
        print("Pickup Options : ",self.options)
        print("Pickup Cab Style : ",self.cabStyle)
        print("Pickup Bed Length :",self.bedLength)
  
garage=[]#this is a vehicle list fellas

while(True):#Johnny 5 loop

    option = int(input("Enter \n1 for Car \n2 for Pickup \n3 for exit \n")) #the option providing the illusion of choice lol

    if(option==1):#this is for car
        make=input("Enter Car Make : ")
        model=input("Enter Car Model : ")
        color=input("Enter Car Color : ")
        fuelType=input("Enter Car Fuel type : ")
        options=input("Enter Car option seprated by space : ")
        engineSize=int(input("Enter Car Engine Size : "))
        numDoors=int(input("Enter Car Number of Doors : "))
        p=Car(make,model,color,fuelType,options,engineSize,numDoors)#create car object
        garage.append(p)#add car to garage vehicle list

    elif(option==2):#this is for truck
        make=input("Enter Pickup Make : ")
        model=input("Enter Pickup Model : ")
        color=input("Enter Pickup Color : ")
        fuelType=input("Enter Pickup Fuel type : ")
        options=input("Enter Pickup option seprated by space : ")
        cabStyle=input("Enter Pickup Cab Style : ")
        bedLength=int(input("Enter Pickup bed length : "))
        t=Pickup(make,model,color,fuelType,options,cabStyle,bedLength)# create truck object
        garage.append(t)#add truck to garage vehicle list

    else:#this is for when you have enough cars
        break

#FINAL PRINT!!
print("Vehicles Details is :")
print("---------------------------")

for vehicle in garage:
    print(vehicle.printDetails())#call printDetails method