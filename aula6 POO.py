

# class FormaGeometrica():
    
#     def __init__(self, lado):
#          self.__lado = lado
        
#     @property
#     def perimetro(self):
#         pass
#     @property
#     def area(self):
#         pass
#     @property
#     def lado(self):
#         return self.__lado
        

# class Quadrado(FormaGeometrica):

#     def __init__(self, lado):
#         super().__init__(lado)


#     @property
#     def area(self):
#         return self.lado ** 2

#     # @property
#     # def perimetro(self): 
#     #     return self.lado * 4

# q = Quadrado(2)
# print(q.perimetro)



# class Quadrado():
    
#     def __init__(self, lado, perimetro):
#         self.__lado = lado
#         self.area = self.area
#         self.perimetro = perimetro
    
#     @property
#     def area(self):
#         return self.__lado ** 2
    
#     @area.setter
#     def area(self, val):
#         self.__area = val
    
#     def perimetro(self):
#         return self.__lado * 4


# q = Quadrado(4 , 4)
# print(q.area)
# print(q.perimetro)

# class Retangulo():



#     def __init__(self, base, altura):
#         self.__base = base 
#         self.__altura = altura 
        
#     @property
#     def area(self):
#         return self.__base * self.__altura
    
#     @property
#     def perimetro(self):
#         return (self.__base * 2 ) + (self.__altura * 2)

#     @property
#     def base(self):
#         return self.__base

#     @property
#     def altura(self):
#         return self.__altura
    



# r = Retangulo(4, 2)
# print(r.perimetro)

# from math import pi

# class Circulo():

#     def __init__(self, raio):
#         self.__raio = raio
        
#     @property
#     def raio(self):
#         return self.__raio
    
#     @property
#     def perimetro(self):
#         return 2 * pi * self.__raio
    
#     @property
#     def diametro(self):
#         return self.__raio * 2
    
#     @property
#     def area(self):
#         return pi * self.__raio * self.__raio

# c = Circulo(5)
# print(c.diametro)


class Triangulo():
    def __init__(self, base, altura, lado_a=2, lado_b=3, lado_c=5, angulo_ab=90, angulo_ac=30, angulo_bc=60):
    
        self.__base = base 
        self.__altura = altura
        self.__lado_a = lado_a
        self.__lado_b = lado_b
        self.__lado_c = lado_c
        self.__angulo_ab = angulo_ab
        self.__angulo_ac = angulo_ac
        self.__angulo_bc = angulo_bc 

    @property
    def base(self):
        return self.__base
    
    @property
    def altura(self):
        return self.__altura
    
    @property
    def lado_a(self):
        return self.__lado_a

    @property
    def lado_b(self):
        return self.__lado_b
    
    @property
    def lado_c(self):
        return self.__lado_c

    @property
    def angulo_ab(self):
        return self.__angulo_ab
    
    @property
    def angulo_ac(self):
        return self.__angulo_ac
    
    @property
    def angulo_bc(self):
        return self.__angulo_bc

    @property 
    def area(self):
         return (self.__base * self.__altura) / 2
 
    @property
    def perimetro(self):
        return self.__lado_a + self.__lado_b + self.__lado_c

    @property
    def tipo_triangulo(self):
        if self.__lado_a == self.__lado_b and self.__lado_b == self.__lado_c:
            return 'triangulo equilatero'
        elif self.__lado_a == self.__lado_b or self.__lado_a == self.__lado_c:  
            return 'triangulo isóceles'
        else:
            return 'triangulo escaleno'
        



t = Triangulo(2,2, 1, 3, 2)
print(t.tipo_triangulo)


