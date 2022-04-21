class Student:
    def __init__(self, m1,m2):
        self.m1=m1
        self.m2=m2
    #we are over writing the default method
    def __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        m3=Student(m1, m2)
        return m3
    
    def __gt__(self, other):
        res1=self.m1+self.m2
        res2=other.m1+other.m2

        if res1 > res2:
            True
        else:
            False
    #if we do like this we need to call __str__()method
    # def __str__(self):
    #     return self.m1, self.m2
    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)
    
s1=Student(75,74)
s2=Student(58,88)
s3=s1+s2
print(s3.m1)

if s1>s2:
    print('s1 have higher marks')
else:
    print('s2 have higher marks')

#print(s2.__str__())
print(s2)