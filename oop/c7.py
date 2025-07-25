# Inheritance Practice
# Siege weapons (battering rams, catapults, etc.) are special units in Age of Dragons. 
# Let's write the logic for how they move around the map.

# Challenge
# Complete the Siege, BatteringRam, and Catapult classes:

# Complete the Siege class:
# Complete the constructor. It accepts two parameters (in order) 
# and sets them as public instance variables with the same name: max_speed and efficiency
# Complete the get_trip_cost() method. It calculates the cost of a trip and returns it. 
# The formula for calculating the cost is: (distance / efficiency) * food_price. 
# It costs food to move siege weapons, those things are heavy!
# Leave the get_cargo_volume() method as empty. 
# Use the pass keyword. Child classes will override this method.

# Complete the BatteringRam class:
# Complete the constructor. It calls the parent constructor, 
# then sets the extra battering-ram-only instance variables as member variables.
# The get_trip_cost() method uses the parent method to calculate the cost of food for a trip, 
# plus the extra cost of carrying a load. 
# The formula for calculating the cost: get_trip_cost() + (load_weight * 0.01)
# The get_cargo_volume() method calculates and returns the cargo capacity in cubic meters. 
# To get the volume of the battering-ram's 'cargo' (bed_area), 
# multiply its area by its depth, which is always 2 meters.

# Complete the Catapult class:
# The constructor calls the parent constructor, 
# then sets the extra catapult-only instance variable as a member variable.
# Do not override the get_trip_cost() method. It's inherited from the parent class.
# The get_cargo_volume() method just returns the cargo capacity of the catapult. 
# This is already set by the constructor.

class Siege:
    def __init__(self, max_speed, efficiency):
        self.max_speed = max_speed
        self.efficiency = efficiency

    def get_trip_cost(self, distance, food_price):
        self.distance = distance
        self.food_price = food_price

        siege_cost = (self.distance / self.efficiency) * self.food_price
        return siege_cost

    def get_cargo_volume(self):
        pass


class BatteringRam(Siege):
    def __init__(
        self,
        max_speed,
        efficiency,
        load_weight,
        bed_area,
    ):
        super().__init__(max_speed, efficiency)
        self.load_weight = load_weight
        self.bed_area = bed_area

    def get_trip_cost(self, distance, food_price):
        br_cost = super().get_trip_cost(distance, food_price) + (self.load_weight * 0.01)
        return br_cost

    def get_cargo_volume(self):
        volume = self.bed_area * 2
        return volume


class Catapult(Siege):
    def __init__(self, max_speed, efficiency, cargo_volume):
        super().__init__(max_speed, efficiency)
        self.cargo_volume = cargo_volume

    def get_cargo_volume(self):
        return self.cargo_volume