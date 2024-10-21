class Matrix:
    def __init__(self,m,n,flag):
        self.M=[]
        self.m=m
        self.n=n
        if flag:
            for i in range(0,m):
                Mem=[0]*(n)
                for j in range(0,n):
                    Mem[j] = input("Write line " + str(i+1) + " and column "+ str(j+1)+": ")
                self.M.append(Mem)
        else:
            for i in range(0,self.m):
                Mem=[0]*(n)
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
    def sumMatrix(self,M):
        if ((self.m==M.m) and (self.n==M.n)):
            res = Matrix(self.m, self.n,0)
            for i in range(0,self.m):
                for j in range(0,self.n):
                    res.indexFill(i,j,str(int(self.indexElement(i,j))+int(M.indexElement(i,j))))
            return res
        else:
            return 0
    def subMatrix(self,M):
        if ((self.m==M.m) and (self.n==M.n)):
            res = Matrix(self.m, self.n,0)
            for i in range(0,self.m):
                for j in range(0,self.n):
                    res.indexFill(i,j,str(int(self.indexElement(i,j))-int(M.indexElement(i,j))))
            return res
        else:
            return 0
    def multiMatrix(self,M):
        if ((self.m==M.n)):
            res = Matrix(self.m, M.n,0)
            for i in range(0,self.n):
                for j in range(0,self.m):
                    mem=0
                    for c in range(0,M.n):
                        mem+=int(self.indexElement(i,c))*int(M.indexElement(c,j))
                    res.indexFill(i,j,str(mem))
            return res

        


m1=int(input("Wrrite line first matrix: "))
n1=int(input("Wrrite column first matrix: "))
m2=int(input("Wrrite line second matrix: "))
n2=int(input("Wrrite column second matrix: "))
print("Info first matrix")
M1=Matrix(m1,n1,1)
print("Info second matrix")
M2=Matrix(m2,n2,1)
print("First matrix")
M1.writeMatrix()
print("Second matrix")
M2.writeMatrix()
M3=M1.sumMatrix(M2)
print("Sum")
M3.writeMatrix()
M4=M2.subMatrix(M1)
print("Sub")
M4.writeMatrix()
M5=M1.multiMatrix(M2)
print("Multi")
M5.writeMatrix()
