"""
A simple charity listing app.
Data is stored in a cloud datastore that looks something like the following:

+------------+------------------------+------------+-------------------+-------------+-----------+----------------------------------+
| Name       | Description            | Address       | Type           |Phone Number | Hours     | Reviews                          |
+============+========================+===============+================+=============+===========+==================================+
| ReHome     | Discount Furniture     | 100 Milky Way | Charity        | 1800CASHNOW | Mon 4-8PM | "My favorite charity in Medford."|
+------------+------------------------+------------+-------------------+-------------+-----------+----------------------------------+
"""
from .Model import Model
from google.cloud import datastore

def from_datastore(entity):
    """Translates Datastore results into the format expected by the
    application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]

    This returns:
        [ name, description, address, type, phone, hours, reviews ]
    where name, email, and message are Python strings
    and where date is a Python datetime
    """
    if not entity:
        return None
    if isinstance(entity, list):
        entity = entity.pop()
    return [entity['name'], entity['description'], entity['address'], entity['typeOfCharity'], entity['phone'], entity['hours'], entity['reviews'], entity['latitude'], entity['longitude']]

class model(Model):
    def __init__(self):
        self.client = datastore.Client('cs356-w22-john-ziegler')

    def select(self):
        query = self.client.query(kind = 'Charity')
        entities = list(map(from_datastore,query.fetch()))
        entities = [x for x in entities if x != None]
        return entities
        """
        Inserts each entry into database
        :param name: String | Since names can be any combination and length, we just want to handle this as a string 
        :param description: String | Since descriptions can be long, we want to handle these as strings
        :param address: String | Addresses could be represented as <address number><street name><street type><location type><location number>, which currently we are handling with strings
        :param typeOfCharity: String | Since the typeOfCharity of charities haven't been determined, we currently just accept a string description of the charity
        :param phone: String | Phone numbers are hard, and I'm not sure storing them as int or longs is smart, plus we can handle extension codes this way as well
        :param hours: String | Hours could be handled as a date format but at this point my code is looking like a yarn shop so might as well keep up the strings
        :param reviews: String | People have a lot to say, but very few ideas to convey, so we just let them type away.
        :return: True | Returns true if the program successfully adds the entry into the database
        :raises: Database errors on connection and insertion
        """
    def insert(self, name, description, address, typeOfCharity, phone, hours, reviews, latitude, longitude):
        key = self.client.key('Charity')
        rev = datastore.Entity(key)
        rev.update( {
            'name': name,
            'description' : description,
            'address' : address,
            'typeOfCharity' : typeOfCharity,
            'phone' : phone,
            'hours' : hours,
            'reviews' : reviews,
            'latitude' : latitude,
            'longitude' : longitude
            })
        self.client.put(rev)
        return True
