from collections import OrderedDict
from re import match

# MGxxxLL/A

def get_models(mode):
    while True:
        enter = raw_input('\nSelect:\n'
                          '1. View model numbers\n'
                          '2. Enter model numbers for tracking\n'
                          '3. Track all 6+ models (beep only)\n'
                          ': ')
        if not match('[1-3]', enter):
            print '\n%s is not a valid choice' % enter
        elif enter == '1':
            display_models()
        elif enter == '2':
            alert_models = []
            beep_models = []

            if mode in [1, 3]:
                alert_models = _get_models('LOUD ALERT')
            if mode in [2, 3]:
                while True:
                    beep_models = _get_models('QUIET BEEP')
                    if set(alert_models) & set(beep_models):
                        print '\nThere are models in the beep list duplicated from the alert list.'
                    else:
                        break

            return alert_models, beep_models

        elif enter == '3':
            return [], ['MG' + model + 'LL/A' for model in all_keys]

def _get_models(type):
    while True:
        models = raw_input('\nEnter the models for which you\'d like a ' + type + '.\n'
                           'Format is a comma-separated list of the 3-digit model short codes\n'
                           '(e.g. "AL2,AU2,AP2")\n'
                           ': ')

        if not match('([a-zA-Z0-9]{3},)*[a-zA-Z0-9]{3}$', models):
            print '\nThere is a problem with input %s' % models
        else:
            model_list = models.upper().split(',')
            valid = True
            for model in model_list:
                if model not in all_keys:
                    valid = False

            if not valid:
                print '\nOne of your selections is not a valid model code.'
            else:
                return ['MG' + model + 'LL/A' for model in model_list]

def display_models():

    while True:
        models = raw_input('\nSelect a list:\n'
                           '1. AT&T\n'
                           '2. Verizon\n'
                           '3. Sprint\n'
                           '4. T-Mobile\n'
                           '5. All\n'
                           ': ')

        if not match('[1-5]', models):
            print '%s is not a valid choice' % models
        else:
            print_model_list(int(models))
            return

def print_model_list(models):
    if models == 1:
        print_att_models()
    elif models == 2:
        print_verizon_models()
    elif models == 3:
        print_sprint_models()
    elif models == 4:
        print_tmobile_models()
    else:
        print_att_models()
        print_verizon_models()
        print_sprint_models()
        print_tmobile_models()

def print_att_models():
    print '\nAT&T models:'
    _print_models(att_models)

def print_verizon_models():
    print '\nVerizon models:'
    _print_models(verizon_models)

def print_sprint_models():
    print '\nSprint models:'
    _print_models(sprint_models)

def print_tmobile_models():
    print '\nT-Mobile models:'
    _print_models(tmobile_models)

def _print_models(list):
    for model, description in list.items():
        print '%s - %s' % (model, description)

def nice_model_name(model):
    short_code = model[2:5]
    if short_code in att_models.keys():
        return att_models[short_code]
    elif short_code in verizon_models.keys():
        return verizon_models[short_code]
    elif short_code in sprint_models.keys():
        return sprint_models[short_code]
    elif short_code in tmobile_models.keys():
        return tmobile_models[short_code]

att_models = OrderedDict([
    ('AL2', '6+ Space Grey 16GB AT&T'),
    ('AU2', '6+ Space Grey 64GB AT&T'),
    ('AP2', '6+ Space Grey 128GB AT&T'),
    ('AM2', '6+ Silver 16GB AT&T'),
    ('AV2', '6+ Silver 64GB AT&T'),
    ('AQ2', '6+ Silver 128GB AT&T'),
    ('AN2', '6+ Gold 16GB AT&T'),
    ('AW2', '6+ Gold 64GB AT&T'),
    ('AR2', '6+ Gold 128GB AT&T'),
    # ('4N2', '6 Space Grey 16GB AT&T'),
    # ('4W2', '6 Space Grey 64GB AT&T'),
    # ('4R2', '6 Space Grey 128GB AT&T'),
    # ('4P2', '6 Silver 16GB AT&T'),
    # ('4X2', '6 Silver 64GB AT&T'),
    # ('4U2', '6 Silver 128GB AT&T'),
    # ('4Q2', '6 Gold 16GB AT&T'),
    # ('502', '6 Gold 64GB AT&T'),
    # ('4V2', '6 Gold 128GB AT&T'),
])

verizon_models = OrderedDict([
    ('CK2', '6+ Space Grey 16GB Verizon'),
    ('CR2', '6+ Space Grey 64GB Verizon'),
    ('CN2', '6+ Space Grey 128GB Verizon'),
    ('CL2', '6+ Silver 16GB Verizon'),
    ('CT2', '6+ Silver 64GB Verizon'),
    ('CP2', '6+ Silver 128GB Verizon'),
    ('CM2', '6+ Gold 16GB Verizon'),
    ('CU2', '6+ Gold 64GB Verizon'),
    ('CQ2', '6+ Gold 128GB Verizon'),
    # ('5W2', '6 Space Grey 16GB Verizon'),
    # ('632', '6 Space Grey 64GB Verizon'),
    # ('602', '6 Space Grey 128GB Verizon'),
    # ('5X2', '6 Silver 16GB Verizon'),
    # ('642', '6 Silver 64GB Verizon'),
    # ('612', '6 Silver 128GB Verizon'),
    # ('5Y2', '6 Gold 16GB Verizon'),
    # ('652', '6 Gold 64GB Verizon'),
    # ('622', '6 Gold 128GB Verizon'),
])

sprint_models = OrderedDict([
    ('CV2', '6+ Space Grey 16GB Sprint'),
    ('D22', '6+ Space Grey 64GB Sprint'),
    ('CY2', '6+ Space Grey 128GB Sprint'),
    ('CW2', '6+ Silver 16GB Sprint'),
    ('D32', '6+ Silver 64GB Sprint'),
    ('D02', '6+ Silver 128GB Sprint'),
    ('CX2', '6+ Gold 16GB Sprint'),
    ('D42', '6+ Gold 64GB Sprint'),
    ('D12', '6+ Gold 128GB Sprint'),
    # ('692', '6 Space Grey 16GB Sprint'),
    # ('6G2', '6 Space Grey 64GB Sprint'),
    # ('6D2', '6 Space Grey 128GB Sprint'),
    # ('6A2', '6 Silver 16GB Sprint'),
    # ('6H2', '6 Silver 64GB Sprint'),
    # ('6E2', '6 Silver 128GB Sprint'),
    # ('6C2', '6 Gold 16GB Sprint'),
    # ('6J2', '6 Gold 64GB Sprint'),
    # ('6F2', '6 Gold 128GB Sprint'),
])

tmobile_models = OrderedDict([
    ('AX2', '6+ Space Grey 16GB T-Mobile'),
    ('C52', '6+ Space Grey 64GB T-Mobile'),
    ('C22', '6+ Space Grey 128GB T-Mobile'),
    ('C02', '6+ Silver 16GB T-Mobile'),
    ('C62', '6+ Silver 64GB T-Mobile'),
    ('C32', '6+ Silver 128GB T-Mobile'),
    ('C12', '6+ Gold 16GB T-Mobile'),
    ('C72', '6+ Gold 64GB T-Mobile'),
    ('C42', '6+ Gold 128GB T-Mobile'),
    # ('542', '6 Space Grey 16GB T-Mobile'),
    # ('5A2', '6 Space Grey 64GB T-Mobile'),
    # ('572', '6 Space Grey 128GB T-Mobile'),
    # ('552', '6 Silver 16GB T-Mobile'),
    # ('5C2', '6 Silver 64GB T-Mobile'),
    # ('582', '6 Silver 128GB T-Mobile'),
    # ('562', '6 Gold 16GB T-Mobile'),
    # ('5D2', '6 Gold 64GB T-Mobile'),
    # ('592', '6 Gold 128GB T-Mobile'),
])

all_keys = att_models.keys() + verizon_models.keys() + sprint_models.keys() + tmobile_models.keys()













