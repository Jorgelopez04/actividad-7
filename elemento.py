from dataclasses import dataclass

@dataclass
class Elemento:
    nombre:str

    def __eq__(self,other):
        if isinstance(other,Elemento):
            return self.nombre==other.nombre
        
    
class Conjunto:
    contador=0
    def __init__(self,nombre:str):
        self.__id=Conjunto.contador
        Conjunto.contador +=1
        self.lista_elementos:list =[]
        self.nombre:str ==nombre

    @property

    def __id (self):
        return self.__id
    
    def contiene(self,Elemento)->bool:
        for x in self.lista_elementos:
            if Elemento == x:
                return True
            

    def agregar_elementos(self,N_Elemento):
        if N_Elemento != self.contiene:
            self.lista_elementos.append(N_Elemento)
    

    def unir(self,otro_conjunto):
        self.otro_conjunto:list =[]
        for y in self.lista_elementos:
            if not self.contiene in y:
                self.otro_conjunto.append(y)

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        elementos_interseccion = [elemento for elemento in conjunto1.Elementos if conjunto2.contiene(elemento)]
        nombre_conjunto_resultante = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        nuevo_conjunto = Conjunto(nombre_conjunto_resultante)
        nuevo_conjunto.Elementos = elementos_interseccion
        return nuevo_conjunto

    def __str__(self):
        elementos_str = ', '.join([Elemento.nombre for elemento in self.Elementos])
        return f"Conjunto {self.nombre}: ({elementos_str})"
    

            