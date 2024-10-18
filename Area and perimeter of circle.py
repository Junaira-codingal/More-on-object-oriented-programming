class Circle:
    
    def __init__(self, r):
        self.radius = r  

    def area(self):
        return 3.14 * self.radius ** 2  
    
    def perimeter(self):
        return 2 * 3.14 * self.radius 
    
    def diameter(self):
        return 2 * self.radius
    
    def sector_area(self, angle):
        return (angle / 360) * self.area()

# Take an input from user
radius = float(input("Enter the radius: "))
angle = float(input("Enter an angle for the sector: "))

c1 = Circle(radius)

print(f"Area of the circle = {c1.area()}")
print(f"Perimeter of the circle = {c1.perimeter()}")  
print(f"Diameter = {c1.diameter()}") 
print(f"Sector area = {c1.sector_area(angle)}")