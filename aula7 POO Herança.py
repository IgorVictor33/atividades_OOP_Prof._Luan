class Pessoa:
    def __init__(self, nome, idade, endereço, cpf, sexo):

        self.__nome = nome
        self.__idade = idade
        self.__endereço = endereço
        self.__cpf = cpf 
        self.__sexo = sexo 

    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    @property
    def endereço(self):
        return self.__endereço
    @property
    def cpf(self):
        return self.__cpf
    @property
    def sexo(self):
        return self.__sexo


class Pai(Pessoa): 
     
    def __init__(self, nome, idade, endereço, cpf, sexo):
        super().__init__(nome, idade, endereço, cpf, sexo)

p = Pai('joao', 25, 'rua', '2131214231', 'masculino')
print(p.nome)

class Mae(Pessoa): 
     
    def __init__(self, nome, idade, endereço, cpf, sexo):
        super().__init__(nome, idade, endereço, cpf, sexo)

m = Mae('maria', 25, 'rua', '2131214231', 'feminino')
print(m.nome)
        
class Filho(Pessoa): 
     
    def __init__(self, nome, idade, endereço, cpf, sexo):
        super().__init__(nome, idade, endereço, cpf, sexo)

f = Filho('max', 25, 'rua', '2131214231', 'masculino')
print(f.nome)

