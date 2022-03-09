class Roupas:
    __id: int
    __marca: str
    __tamanho: int
    __tipo: str

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca: int):
        self.__marca = marca

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, tamanho: int):
        self.__tamanho = tamanho

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: int):
        self.__tipo = tipo

    def __str__(self) -> str:
        return str(self.__class__) + ": " + str(self.__dict__)