import land_conversion,area_conversion

length=float(input("Length : "))
breadth=float(input("Breadth : "))


print("""
Choose your input type.
Calculate your area
Convert the area into ... 
""")
def area_calculate(length, breadth):
    area=length * breadth
    return area
