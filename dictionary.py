personal_details={'name':'Nirajan Joshi', 'age':23, 'education_qualification':'BIM','phone':9847620206}
print(personal_details['name'])
print(personal_details)
#get method return the value if possible and return none if not possible.
print(personal_details.get('phone'))
#set default value
print(personal_details.get('dob', '18 July 1998'))
print(personal_details.get('age',25))

personal_details['address']='Kushma, parbat'
print(personal_details['address'])

#Dictionary Tasks

numeric_to_word={'1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine','0':'Zero',}
phone_number=input('Enter your number.')
output=""
for ch in phone_number:
    output+=numeric_to_word.get(ch, '!')+" "
print(output)