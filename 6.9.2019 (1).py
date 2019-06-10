
# coding: utf-8

# In[15]:


seq = [1,2,3,4,5]
i = 0
for var in seq:
    print("%d element is : %d"%(i, var))
    i = i +1
else:
        print("i am else optional block")
        print("I can execute when no more updation")
    


# In[16]:


seq = "Srishti Sharma"
le = 0
for var in seq:
    le = le +1
else:
        print("len of", seq,"is", le)


# In[17]:


N=int(input("enter N value"))
sum=0
for var in range(1,N+1):
    sum = sum +var
else:
    print("sum of 1st %d Natural number is %d"%(N,sum))
    


# In[22]:


# print multiplication table
N = int(input("enter N value : "))
seq =range(1,11)

for var in seq:
    print("%d * %d = %d"%(N,var, N*var))
          


# In[24]:


mypairs =[(1,2), (3,4), (5,6)]
for (tup1, tup2) in mypairs:
    print(tup1)
    


# In[36]:


i = [1, 2, 3, 4]

out = []
for num in i:
   out.append(num%2)

print(out)
    

