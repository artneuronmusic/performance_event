from faker import Faker
import random
from random import randint, randrange
from faker_web import WebProvider
import re
from faker_e164.providers import E164Provider
import phonenumbers
import urllib
fake = Faker(locale='en_US')

#-------------------------------------------------------#
# turn the fake numbers into xxx-xxx-xxxx format
#ex: +1-100-695-4529x5551, 744.048.4866x174, 001-622-733-1574, (813)376-9178
#-------------------------------------------------------#
restaurant_list = ['Dubious Clams Brewing Company', 'The Drunken', "Sammie's",'un·cooked', 'Water Pig', 'Fry the music', 'Egg Slut', 'Call Your Mother', 'Foulmouthed Brewing', 'Meet Classical',
'The Catbird Seat', 'Hot Chix – Boston', "Obed and Isaac's", 'Fat Baby', 'Plan B Running', 'Bun Huggers Old Fashion',  
'Spanked Puppy', 'Holy Accustic', 'Tandem Coffee + Bakery', 
'Mr. & Mrs. Bun', 'Phlavz']
new = [i for i in restaurant_list]
new2 = [x.format() for x in restaurant_list]
print(type(new))
print(type(new2))

# restaurant_name = random.choices(restaurant_list)
# restaurant_name_format = ''.join(restaurant_name)
# print(restaurant_name, type(restaurant_name))
# print(restaurant_name_format, type(restaurant_name_format))
# restaurant_name = random.choices(restaurant_list)
# restaurant_name_format = ''.join(restaurant_name)
# new = re.sub(r'\W', '', restaurant_name_format)

# new = fake.company()
# print(type(new))
# print(type(new))
# print(type(restaurant_name_format))
# print (urllib.parse.quote(restaurant_name_format, safe=''))

# new = {}
# genre_choices=[
#             ('Alternative'), ('Blues'), ('Classical'), ('Country'), ('Electronic'), ('Folk'), ('Funk'), ('Hip-Hop'),
#             ('Heavy Metal'), ('Instrumental'), ('Jazz'), ('Musical Theatre'), ('Pop'), ('Punk'), ('R&B'),('Reggae'),
#             ('Rock n Roll'), ('Soul'), ('Other')
# ]
# genre = random.choices(genre_choices)
# new['genre']= genre
# print('{} '.format(new['genre']))

# def format_number(number):
#     """
#     format ths input number as xxx-xxx-xxxx
#     for example: 744.048.4866x174 -> 744-048-4866
#     """
#     first_transformation=''
#     if len(number) >10 :
#         new = format(int(number[:-1]), ",").replace(",", "-") + number[-1]
#         # print(new)
#         new_number = re.findall('[0-9]{3}\-[0-9]{3}\-[0-9]{4}', new)[0]
#         #print(new_number)
#         first_transformation=new_number
#         #print(new_number)
#         first_transformation=new_number
#     elif len(number) == 10 and number.startswith('00'):
#         first_transformation=number[0]+number[1]+format(int(number[:-1]), ",").replace(',', '-')+number[-1]
#         #first_transformation=format(int(number[:-1]), ",").replace(',', '-')+number[-1]
#         #   print(format(int(number[:-1]), ",").replace(',', '-')+number[-1])
#         # print("2")
#     elif len(number) == 10 and number.startswith('0'):
      
#         first_transformation = number[0]+format(int(number[:-1]), ",").replace(',', '-')+number[-1]
#         #print(number[0]+format(int(number[:-1]), ",").replace(',', '-')+number[-1])
#         # print("3")
#     elif len(number) == 10:
#          first_transformation=format(int(number[:-1]), ",").replace(',', '-')+number[-1]
#         #   print(format(int(number[:-1]), ",").replace(',', '-')+number[-1])

   
   
#     return first_transformation
    

''' ex: 744.048.4866, 001-622-733-1574, (813)376-9178'''

# TEST_CASES = [
#     ("0521604350", "052-160-4350"),
#     ("744.048.4866x174", "744-048-4866"),
#     ("(813)376-9178", "813-376-9178"),
#     ("001-622-733-1574", "622-733-1574"),
#     ('0093331212', "009-333-1212")
# ]
# for original, formatted in TEST_CASES:
#     computed=check_number(original)
#     if computed == formatted:
#         print("PASS", original, computed)
#     else:
#         print("FAIL", original, computed)
        
# number =  '0093331212'
# new_number = phonenumbers.parse(number, 'US')
# area_number = phonenumbers.format_number(new_number, phonenumbers.PhoneNumberFormat.NATIONAL)

# new_number = number[0]+number[1]+format(int(number[:-1]), ",").replace(',', '-')+number[-1]
# print(new_number)



# number1 = fake.phone_number()
# print(check_number(number1))

# fake.add_provider(E164Provider)
# from faker_music import MusicProvider

# from random import randint, randrange
#-----------------#
#Faking 20 cases for testing

#-----------------#

# restaurant_list = ['Dubious Clams Brewing Company', 'The Drunken', "Sammie's",'un·cooked', 'Water Pig', 'Fry the music', 'Egg Slut', 'Call Your Mother', 'Foulmouthed Brewing', 'Meet Classical',
# 'The Catbird Seat', 'Hot Chix – Boston', "Obed and Isaac's", 'Fat Baby', 'Plan B Running', 'Bun Huggers Old Fashion',  
# 'Spanked Puppy', 'Holy Accustic', 'Tandem Coffee + Bakery', 
# 'Mr. & Mrs. Bun', 'Phlavz']

# #wont use from faker_music based on the website prerequisite
# genre_choices=[
#             ('Alternative'), ('Blues'), ('Classical'), ('Country'), ('Electronic'), ('Folk'), ('Funk'), ('Hip-Hop'),
#             ('Heavy Metal'), ('Instrumental'), ('Jazz'), ('Musical Theatre'), ('Pop'), ('Punk'), ('R&B'),('Reggae'),
#             ('Rock n Roll'), ('Soul'), ('Other')
#         ]

seeking_description = ['Talented artist who is willing to perform and share music', 'No expereinced is not problem; we are looking for musicians who has passion, even just new to the field', 'its a great and friendly place for performers']
# # print(type(choices[1]))
#----------------------------------
# new = fake.msisdn()
# def phone_number_format():
#     for i in range(10):
#         new = fake.phone_number()
#     # new_format = ''.join(e for e in new if e.isnumeric())
#     # if len(new_format)>10:
#         new_regex = re.sub('[^0-9]+', '', new)

# number1 = '(221)842-4315x85045'
# number1='0015987465970'


# new_regex = re.sub('[^0-9]+', '', new_format1)
# result = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(new_number_list[:-1])) + new_number_list[-1]
# print(result)



# fake.add_provider(WebProvider)
# address='032 May Motorway Apt. 390\nAndreahaven, ND 68555'
# address ="9942 Beth Drive Apt. 811\nHarperchester, GA 16790"
# address=fake.address()
# print(address)
# new_address = address.split('\n')
# city_state_format = new_address[1].split(', ')
# state = city_state_format[1]
# state_format = re.findall('[a-zA-Z]+', state)

# print(city_state_format)
# print(state_format)

# # format_pattern(address): 
# address=fake.address()
# # print(address)
# #pattern = re.compile(r'^[\w]PO$')
# pattern = re.compile(r'\wPO')

# pattern_check = pattern.findall(address)
# # print(pattern_check)#=>empty


# i=0
# address_result = {}
# while i<5:

#     address=fake.address()
#     print(address)
#     #pattern = re.compile(r'^[\w]PO$')
#     pattern = re.compile(r'\wPO')

#     pattern_check = pattern.findall(address)
#     if not pattern_check:
#         print("IF" + str(i))
#         address_seperate=re.split('\n', address)
#         # print(address_seperate)
#         address_list_address= address_seperate[0]
#         city_state = address_seperate[1].split(', ')
#         address_list_city= city_state[0]
#         # print(address_list_city)
#         state = city_state[1]
#         address_list_state=re.findall('[a-zA-Z]+', state)
#         # print(address_list_state)
#         address_result['address'] = address_list_address
#         address_result['city'] = address_list_city
#         address_result['state'] = ''.join(address_list_state)
#         break

#     else:
#         i+=1

# print(address_result)
# print(type(address_result['state']))
        
    



    
#     address=fake.address()
#     print(address)
#     #pattern = re.compile(r'^[\w]PO$')
#     pattern = re.compile(r'\wPO')

#     pattern_check = pattern.findall(address)
#     print(pattern_check)#=>empty
#     i+=1
   
# # if not pattern_check:
#     # print(pattern_check)
# address_seperate=re.split('\n', address)
# print(address_seperate)
# address_list_address= address_seperate[0]
# city_state = address_seperate[1].split(', ')
# address_list_city= city_state[0]
# print(address_list_city)
# state = city_state[1]
# address_list_state=re.findall('[a-zA-Z]+', state)
# print(address_list_state)
# print(i)


#else:
#    address=fake.address()
#    pattern = re.compile(r'[\w]PO$')
#    pattern_check = pattern.findall(address)

    




# print(seperate_address)
# address_list = {}
# address="9942 Beth Drive Apt. 811 Harperchester, GA 16790"
# address_seperate=re.split('\n|,|. ', address)
# print(address_seperate)
# state = address_seperate[2].split(' ')[0]
# print(f'location: {address_seperate[0]}, city:{address_seperate[1]}, state:{state}')
# address_list['address']= address_seperate[0]
# address_list['city']= address_seperate[1]
# address_list['state']=address_seperate[2].split(' ')[0]
# print(address_list['address'])
# print(address_list['city'])
# print(address_list['state'])
# def split_info(item):
# # def generate_data(num):
#     pass

# customer ={}
# for n in range(0, 20):
#         customer[n]={}
#         customer[n]['id']= n
# print(customer)


#name = random.choices(restaurant_list)
#address=fake.address() #9942 Beth Drive Apt. 811 Harperchester, GA 16790
#city
#state
#phone=fake.phone_number() #001-735-019-4897
#genres=random.choices(genre_choices)
#website=fake.url() or "www"+name+.com
#facebook_link="www.fcebook.com/"+name
# seeking_talent =bool(random.getrandbits(1))

# print(seeking_talent)

# if seeking_talent:
#     new = ''
#     new = random.choice(seeking_description)


# print(new)








#artist_image url:fake.image_url()
#fake.email()
