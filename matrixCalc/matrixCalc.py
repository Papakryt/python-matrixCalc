class Matrix:
    def __init__(self,m,n):
        self.M=[]
        self.m=m
        self.n=n
        for i in  range(0,m):
            Mem=[0]*(n)
            for j in range(0,n):
                Mem[j] = input("Write line " + str(i+1) + " and column "+ str(j+1)+": ")
            self.M.append(Mem)
    def writeMatrix(self):
        for i in self.M:
            stroke = ""
            for j in i:
                stroke = stroke+ j +"   "
            print(stroke+"\n")
    def indexElement(self,i,j):
        return self.M[i][j]
    def indexFill(self,i,j,res):
        self.M[i][j]=res
    def sumMatrix(self,Matrix):
        if ((self.m==Matrix.m) and (self.n==Matrix.n)):
            for i in range(0,self.m):
                for j in range(0,self.n):
                    self.M[i][j]=str(int(self.indexElement(i,j))+int(Matrix.indexElement(i,j)))
        else:
            return 0
    def subMatrix(self,Matrix):
        if ((self.m==Matrix.m) and (self.n==Matrix.n)):
            for i in range(0,self.m):
                for j in range(0,self.n):
                    self.M[i][j]=str(int(self.indexElement(i,j))-int(Matrix.indexElement(i,j)))
        else:
            return 0
    def multiMatrix(self,Matrix):
        res = self.Matrix(self.m, Matrix.n)
        if ((self.m==Matrix.n)):
            for i in range(0,self.n):
                for j in range(0,self.m):
                    mem=0
                    for c in range(0,Matrix.n):
                        mem+=self.indexElement(i,c)*Matrix.indexElement(c,j)
                    res.indexFill(i,j,mem)
            return res

        


m1=int(input("Wrrite line first matrix: "))
n1=int(input("Wrrite column first matrix: "))
m2=int(input("Wrrite line second matrix: "))
n2=int(input("Wrrite column second matrix: "))
print("Info first matrix")
M1=Matrix(m1,n1)
print("Info second matrix")
M2=Matrix(m2,n2)
print("First matrix")
M1.writeMatrix()
print("Second matrix")
M2.writeMatrix()
M1.sumMatrix(M2)
print("Sum")
M1.writeMatrix()
M2.subMatrix(M1)
print("Sub")
M2.writeMatrix()
M3=Matrix(3,3)
M3=M1.multiMatrix(M2)
print("Multi")
M3.writeMatrix()
