class Cargoplane:
    def takeoff(self):
        print("Plane is takeoff")
    def fly(self):
        print("Plane is flying")
    def land(self):
        print("Plane is landed")
    def carryg(self):
        print("Plane carry goods")
class Passengerplane:
    def takeoff(self):
        print("Plane is takeoff")
    def fly(self):
        print("Plane is flying")
    def land(self):
        print("Plane is landed")
    def carryp(self):
        print("Plane carry Passenger")
class Fightplane:
    def takeoff(self):
        print("Plane is takeoff")
    def fly(self):
        print("Plane is flying")
    def land(self):
        print("Plane is landed")
    def carryw(self):
        print("Plane carry weapons")
c=Cargoplane()
p=Passengerplane()
f=Fightplane()
c.takeoff()
c.fly()
c.land()
c.carryg()
p.takeoff()
p.fly()
p.land()
p.carryp()
f.takeoff()
f.fly()
f.land()
f.carryw()