name=['Nirajan','Kiran','Bhuwan']
bikes=['ns200','bullet','shine']

bike_detail=zip(name, bikes)
dic=dict(zip(name, bikes))
print(dic)
for (a,b) in bike_detail:
    print(a, b)