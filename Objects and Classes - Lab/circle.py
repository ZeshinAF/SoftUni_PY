class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        return self.diameter * Circle.__pi

    def calculate_area(self):
        return self.radius * self.radius * Circle.__pi

    def calculate_area_of_sector(self, angle):
        return (angle / 360) * self.radius * self.radius * Circle.__pi
