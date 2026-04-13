class plane:
    def takeoff(self):
        print("Plane is takeoff")
    def fly(self):
        print("Plane is flying")
    def land(self):
        print("Plane is landed")
class Cargo(plane):
    def carryg(self):
        print("Plane carry goods")
class Passenger(plane):
    def carryp(self):
        print("Plane carry passengers")
class Fighter(plane):
    def carryw(self):
        print("Plane carry Weapons")
c=Cargo()
p=Passenger()
f=Fighter()
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