import  numpy as np
n=np.array([[1,2,3],
            [7,8,9],
            [4,5,6]])
n=n*10
oned=np.array([1,2,3,4,5,6,256,20,50,99,88,77,45,412,3215])
d= np.array([[[1],[4],[7]],[['s'],['a'],['m']],[['@'],['$'],['%']],[[1],[4],[7]],[['s'],['a'],['m']],[['@'],['$'],['%']]])
con_n=n.astype(float)
#print(n+5,n-5,n*5,n/5)
#print(oned[::-1])
#print(oned[[0,5]])
#print(n[0][2])
#print((oned[oned>50]))
#oned=oned.reshape(3,5)
#oned=oned.ravel()
oned=np.insert(oned,2,9999)
oned=np.append(oned,888)
#print(oned)
#print(n)
n= np.insert(n,3,[1,2,3],axis=1)
#n=np.append(n,[[7,4,1]],axis=0)
#print(n)

n1=np.array([[1,2],[7,8]])
n2=np.array([[3,4],[5,6]])
print(n1[1][0])
print(np.delete(n1,0,axis=0))
