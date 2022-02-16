'''create a class named car, with name,cost,engine_displacement,engine,braking_system,
transmission_type properties and print_specification method'''
class car: 
    def __init__(self,name,cost,engine_displacement,engine,braking_system,transmission_type):
        self.name = name
        self.cost = cost
        self.engine_disp = engine_displacement
        self.engine = engine
        self.breaking_sys = braking_system
        self.transmission = transmission_type
    def print_specification(self):
        print('Car Name:',self.name,'\nCost of car:',self.cost,'\nEngine Displacement of the car:',self.engine_disp,
        '\nEngine:',self.engine,'\nBraking system of car:',self.breaking_sys,'\nTransmission of car:',self.transmission)

# class sportcars is derived from car with additional properties of nitro and additional_feature
class sportcars(car):
    def __init__(self,name,cost,engine_displacement,engine,braking_system,transmission_type,nitro,additional_feature):
        car.__init__(self,name,cost,engine_displacement,engine,braking_system,transmission_type)
        # here we can also use
        # super().(cost,engine_displacement,engine,braking_system,transmission_type)
        self.nitro = nitro
        self.Another_features = additional_feature
    def print_specification1(self):
        print('Car Name:',self.name,'\nCost of car:',self.cost,'\nEngine Displacement of the car:',self.engine_disp,
        '\nEngine:',self.engine,'\nBraking system of car:',self.breaking_sys,'\nTransmission of car:',self.transmission,
        '\nNitro is present in car:',self.nitro,'\nAdditional Features:',self.Another_features)

# use the sportcars class to create an object
a = sportcars("BMW", 5500000, 10000, "Petrol", "ABS", "Manual","Yes","Parking sensors")

# execute print_specification1 method
a.print_specification1()