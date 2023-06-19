class Triangulo:
    def __init__(self,ladoa,ladob,ladoc):
        self.a = ladoa
        self.b = ladob
        self.c = ladoc

    def perimetro(self):
        return self.a+self.b+self.c

    def tipo_lado(self):
        if self.a==self.b and self.b == self.c:
            return 'equilátero'
        elif self.a != self.b and self.b != self.c and self.c != self.a:
            return 'escaleno'
        else:
            return 'isósceles'

    def retangulo(self):
        if (self.a)**2 + (self.b)**2 == (self.c)**2:
            return True
        else:
            return False

    def semelhantes(self,t2):
        tr1 = [self.a,self.b,self.c]
        tr2 = [t2.a,t2.b,t2.c]
        tr1.sort()
        tr2.sort()

        if tr1[0]/tr2[0] == tr1[1]/tr2[1] and tr1[1]/tr2[1] == tr1[2]/tr2[2]:
            return True
        else:
            return False

        
        
