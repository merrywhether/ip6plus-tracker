from httplib import HTTPConnection
from itertools import izip
from json import loads
from re import match



def get_zip_code():
    while True:
        zip_code = raw_input('\nEnter your 5-digit zip code\n'
                             ': ')
        if not match('\d{5}$', zip_code):
            print '\n%s is not a valid zip code' % zip_code
        else:
            return zip_code

def get_target_stores(zip_code):
    from main import HOST, PATH_ROOT

    connection = HTTPConnection(HOST)
    connection.request("GET", '{root}{zip_code}&parts.0=MG502LL%2FA'.format(root=PATH_ROOT, zip_code=zip_code))
    stores = loads(connection.getresponse().read())['body']['stores']

    store_names = [store['storeName'] for store in stores]

    print '\nThese are the stores Apple shows are near your zip code: '
    store_indexes = range(1, len(store_names)+1)
    for index, store in izip(store_indexes, store_names):
        print '%s. %s' % (index, store)
    print '%s. TRACK ALL STORES IN AREA' % str(len(store_names)+1)

    while True:
        index_string = raw_input('Enter the stores whose inventory you\'d like to monitor.\n'
                                    'Format is a comma-separated list of the number indexes.\n'
                                    '(e.g. "1,3,8")\n'
                                    ': ')
        if not match('(\d{1,2},)*\d{1,2}', index_string):
            print '\nThere is a problem with input %s' % index_string
        elif index_string == str(len(store_names)+1):
            return [store for store in store_names]
        else:
            str_indexes = index_string.split(',')
            indexes = [int(index) for index in str_indexes]
            valid = True
            for index in indexes:
                if index not in store_indexes:
                    valid = False

            if not valid:
                print '\nOne of your selections was not in the list.'
            else:
                return [store_names[index-1] for index in indexes]

