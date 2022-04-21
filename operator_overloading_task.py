import math
from unicodedata import name


class Student:
    def __init__(self, name, math, science, social, english):
        self.name=name
        self.math=math
        self.sci=science
        self.soc=social
        self.eng=english
    def __sub__(self,other):
        math=self.math-other.math
        sci=self.sci-other.sci
        soc=self.soc-other.soc
        eng=self.eng-other.eng
        return Student('Default',math, sci,soc,eng)
    
    def __str__(self):
        return 'Name :{} Math={} Science={} Social={} English={}'.format(self.name, self.math, self.sci, self.soc, self.eng)
    
s1=Student("Nirajan",84,81,89,91)
s2=Student("Bimal",75,89,80,95)
s3=s1-s2
print(s3)
