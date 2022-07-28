
import json
import re
import random
from random import randint, randrange
from faker import Faker
from faker_web import WebProvider
import phonenumbers

fake = Faker(locale='en_US')
number_result = ''
address_list = {}
restaurant_list = ['Dubious Clams Brewing Company', 'The Drunken', "Sammie's",'un·cooked', 'Water Pig', 'Fry the music', 'Egg Slut', 'Call Your Mother', 'Foulmouthed Brewing', 'Meet Classical',
'The Catbird Seat', 'Hot Chix Boston', "Obed and Isaac's", 'Fat Baby', 'Plan B Running', 'Bun Huggers Old Fashion',  
'Spanked Puppy', 'Holy Accustic', 'Tandem Coffee + Bakery', 
'Mr. & Mrs. Bun', 'Phlavz']

#wont use from faker_music based on the website prerequisite
genre_choices=[
            ('Alternative'), ('Blues'), ('Classical'), ('Country'), ('Electronic'), ('Folk'), ('Funk'), ('Hip-Hop'),
            ('Heavy Metal'), ('Instrumental'), ('Jazz'), ('Musical Theatre'), ('Pop'), ('Punk'), ('R&B'),('Reggae'),
            ('Rock n Roll'), ('Soul'), ('Other')
]

seeking_talent_description = ['Talented artist who is willing to perform and share music', 'No expereinced is not problem; we are looking for musicians who has passion, even just new to the field', 'its a great and friendly place for performers']
seeking_venue_description = ['Affordable places for performance', 'places which love music and enjoy it', 'Any performing places in USA']

def build_venue_data(amount: int):
    data_items = []
    for i in range(1, amount):  
        restaurant_name = random.choices(restaurant_list)
        restaurant_name_format = ''.join(restaurant_name)
        restaurant_name_str = re.sub(r'\W', '', restaurant_name_format)
        random_address = create_full_address(fake.address()) 
        seeking_for_talent = bool(random.getrandbits(1))

        data_info = {
            'id': int(i),
            'name': restaurant_name_format,
            'address': random_address['address'],
            'city': random_address['city'],
            'state': random_address['state'],
            'phone': check_number(fake.phone_number()),
            'genres': random.choices(genre_choices),
            'image_link': fake.image_url(),
            'website_link': "www."+restaurant_name_str+".com",
            'facebook_link': "www.fcebook.com/"+restaurant_name_str,
            'seeking_talent': seeking_for_talent,
            'seeking_talent_description': check_request_and_description(seeking_for_talent, seeking_talent_description)
        }
        data_items.append(data_info)
    
  
    with open('venue_data1.json', 'w') as v_data:
        json.dump(data_items, v_data)
    print('Venue Data has been created')


def build_artist_data(amount: int):
    artist_items = []
    for i in range(1, amount):  
        artist_name = fake.company()
        random_address = create_full_address(fake.address()) 
        artist_name_format = ''.join(artist_name)
        artist_name_str = re.sub(r'\W', '', artist_name_format)
        seeking_for_venue = bool(random.getrandbits(1))
        

        data_info = {
            'id': int(i),
            'name': artist_name,
            'city': random_address['city'],
            'state': random_address['state'],
            'phone': check_number(fake.phone_number()),
            'genres': random.choices(genre_choices),
            'image_link': fake.image_url(),
            'website_link': "www."+ artist_name_str+".com",
            'facebook_link': "www.fcebook.com/"+ artist_name_str,
            'seeking_venue': seeking_for_venue,
            'seeking_venue_description': check_request_and_description(seeking_for_venue, seeking_venue_description)
        }
        artist_items.append(data_info)
    with open('artist_data1.json', 'w') as a_data:
        json.dump(artist_items, a_data)
    print('Venue Data has been created')


def check_request_and_description(request_info, seeking_description):
    new = ''
    if request_info:
        new = random.choice(seeking_description)
    return new

def create_full_address(address):
    i=0
    address_result = {}
    while i<5:
        address=fake.address()
        # print(address)
        #pattern = re.compile(r'^[\w]PO$')
        pattern = re.compile(r'\wPO')

        pattern_check = pattern.findall(address)
        if not pattern_check:
            # print("IF" + str(i))
            address_seperate=re.split('\n', address)
            # print(address_seperate)
            address_list_address= address_seperate[0]
            city_state = address_seperate[1].split(', ')
            address_list_city= city_state[0]
            # print(address_list_city)
            state = city_state[1]
            address_list_state=re.findall('[a-zA-Z]+', state)
            # print(address_list_state)
            address_result['address'] = address_list_address
            address_result['city'] = address_list_city
            address_result['state'] = ''.join(address_list_state)
            break
        else:
            i+=1

    return address_result

  
def check_number(number_sample):
    
    number = ''
    new_number = phonenumbers.parse(number_sample, 'US')
    area_number = phonenumbers.format_number(new_number, phonenumbers.PhoneNumberFormat.NATIONAL)
    # print(area_number)
    if len(area_number)==10:
         number_result=(format_number(area_number))
    else:
        number_list = str(area_number).split(' ')
        # print(number_list)
        if len(number_list) > 1:
            # print('number1')
            # print(number_list[0])
            # print(number_list[1])
            first_two = ''.join(number_list[:2])
            # print(first_two)
            number = ''.join(e for e in first_two if e.isnumeric())
            # print(number)
            number_result=(format_number(number))
        else: 
            # print('number2')
            number = number_list[0]
            number_result=(format_number(number))

    return number_result

def format_number(number):
    """
    format ths input number as xxx-xxx-xxxx
    for example: 744.048.4866x174 -> 744-048-4866
    """
    first_transformation=''
    if len(number) >10 :
        new = format(int(number[:-1]), ",").replace(",", "-") + number[-1]
        # print(new)
        new_number = re.findall('[0-9]{3}\-[0-9]{3}\-[0-9]{4}', new)[0]
        #print(new_number)
        first_transformation=new_number
        #print(new_number)
        first_transformation=new_number
    elif len(number) == 10 and number.startswith('00'):
        first_transformation=number[0]+number[1]+format(int(number[:-1]), ",").replace(',', '-')+number[-1]
        #first_transformation=format(int(number[:-1]), ",").replace(',', '-')+number[-1]
        #   print(format(int(number[:-1]), ",").replace(',', '-')+number[-1])
        # print("2")
    elif len(number) == 10 and number.startswith('0'):
      
        first_transformation = number[0]+format(int(number[:-1]), ",").replace(',', '-')+number[-1]
        #print(number[0]+format(int(number[:-1]), ",").replace(',', '-')+number[-1])
        # print("3")
    elif len(number) == 10:
         first_transformation=format(int(number[:-1]), ",").replace(',', '-')+number[-1]
        #   print(format(int(number[:-1]), ",").replace(',', '-')+number[-1])

   
   
    return first_transformation


build_venue_data(21)
build_artist_data(21)
    

