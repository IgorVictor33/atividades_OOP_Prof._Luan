# class Mamifero:
#     def som(self):
#         print('emitir um som')

# class Homem(Mamifero):
#     def som(self):
#         print('Oi')

# class Cachorro(Mamifero):
#     def som(self):
#         print('au au')

# class Gato(Mamifero):
#     def som(self):
#         print('meow')

# mamifero = Mamifero()
# mamifero.som()

# animais = [Homem(), Cachorro(), Gato()]
# for animal in animais:
#     animal.som()


class Conta_corrente:

    def __init__(self, saldo ,percentual_imposto):
        self.__saldo = saldo
        self.__percentual_imposto = percentual_imposto
    
    @property
    def calcula_imposto(self):
        self.__saldo * self.__percentual_imposto
        return self.__saldo - (self.__saldo * self.__percentual_imposto)
        
    @property
    def valor(self):
        return self.__saldo

    @property
    def percentual(self): 
       return self.__saldo * self.__percentual_imposto

class Poupança(Conta_corrente):

    def valor(self):
        return self.__saldo


class ContaImposto(Conta_corrente):
 
    def __init__(self, saldo, percentual_imposto):
        super().__init__(saldo, percentual_imposto)


c = Conta_corrente(1000, 0.20)
print(c.percentual)


    
