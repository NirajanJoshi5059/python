#Land area conversion

#Feet to haat
def ft_to_haat(ft):
    haat=ft*.666666666667
    return haat
#Haat to feet
def haat_to_ft(haat):
    ft=haat*1.5
    return ft

#sqft to yard
def sqft_to_yard(sqft):
    yard=sqft*(1/9)
    return yard
#yard to square feet
def yard_to_sqft(yard):
    sqft=yard*9
    return sqft
    
#dam to square meter
def dam_to_msq(dam):
    msq=dam*1.99
    return msq
#square meter to dam
def msq_to_dam(msq):
    dam=msq*.5025125628
#paisa to daam
def paisa_to_dam(paisa):
    dam=paisa*4
    return dam
#daam to paisa
def dam_to_paisa(dam):
    paisa=dam*.25
    return paisa
#aana to paisa
def aana_to_paisa(aana):
    paisa=aana*4
    return paisa
#paisa to aana
def paisa_to_aana(paisa):
    aana=paisa*.25
    return aana
#ropani to aana
def ropani_to_aana(ropani):
    aana=ropani*16
    return aana
#aana to ropani
def aana_to_ropani(ropani):
    ropani=aana*0.0625
    return ropani