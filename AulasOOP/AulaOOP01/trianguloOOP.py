class triangulo:
    #Atributos
    a:int
    b:int
    c:int

    def area(self):
        from math import sqrt
        p = (self.a + self.b + self.c) / 2
        area = sqrt(p * (p - self.a) * (p - self.b * (p - self.c))) ** 0.5
        return area
            
