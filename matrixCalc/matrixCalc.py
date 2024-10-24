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
    def cloneMatrix(self, M):
        res = Matrix(M.m,M.n,0)
        for i in range(0,M.m):
            for j in range(0,M.n):
                res.indexFill(i,j,M.M[i][j])
        return res
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
    def transMatrix(self):
        res=Matrix(self.n,self.m,0)
        for i in range(0,self.m):
            for j in range(0,self.n):
                res.indexFill(j,i,self.M[i][j])
        return res
    def diagMatrix(self):
        if (self.m==self.n):
            res = Matrix(self.m,self.n,0)
            res = res.cloneMatrix(self)
            for c in range(0,self.m):
                mem=[]
                for i in range(0,self.m):
                    for j in range(0,self.n):
                        if(i==c):
                            mem.append(res.indexElement(i,j))
                        elif((i>c)and(j==c)):
                            memN = res.M[i][j]
                            #self.M[i][c]=str(0)
                            res.indexFill(i,c,str(0))
                        elif((i>c)and(j>=c)):
                            #ymn=float(memN)/float(mem[c])
                            ymn=float(memN)/float(mem[c])
                            #self.M[i][j]=str(float(self.M[i][j])-float(mem[j])*ymn)
                            res.indexFill(i,j,str(float(res.M[i][j])-float(mem[j])*ymn))        
            return res
    def determMatrix(self):
        if (self.m==self.n):
            S=Matrix(self.m,self.n,0)
            S=S.cloneMatrix(self)
            S=S.diagMatrix()
            res=1
            for i in range(0,self.m):
                for j in range(0,self.n):
                    if i==j:
                        res=res*float(S.M[i][j])
            return res

