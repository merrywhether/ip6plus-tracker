#! /usr/bin/env python

from os import system
from os.path import dirname, realpath, join
from pickle import load, dump
from re import match

from location import get_zip_code, get_target_stores
from models import get_models, nice_model_name
from monitor import start_monitoring


HOST = 'store.apple.com'
PATH_ROOT = '/us/retailStore/availabilitySearch?zip='
FILE_PATH = dirname(realpath(__file__))

def start():
    system('clear')
    print '''                                          ...                MMM
                                  .  .,MMMMMMMMMD. .        MMM.
                                   .DMMMMMMMMMMMMMM      . MMM
                         .MMMMMMM..MMMM?        MMMM .    MMM+.            .  .
                        .IMMMO?:   ?$    ,.      MMM   . NMMM             .8MM.
                         .           ...MMM.     MMM  .. MMM.              MMM
                                       .OMM~    MMM8    OMM~.              MMM
                            .7.         .MMN  .MMMM.    MMM.....           MMM   .
                           .ZMM+         MMM7MMMM:     ~MM~ MMMM .         MMM   .
                            OMMZ         MMMMMMM       MMM.   MMN.  . .IMMMMMMMMMMMMM
                           .?MMN        .MMMMZ         MMM ...DMM. +MMMMMMMMMMMMMMMM
                            .MMM         MMM ..        MMM    MM8   OMMZ,  MMM. .
                           ..MMM.        MMM           MMM  .IMM           MMM.
                           ..MMMN.       8MM          .7MM, MMM.          .DMM
                              MMM.      .OMM            MMMMMM            . MM.
                                        .ZMM             7MM..              ...
                             ..        .   ~              .  .            .   .






                                                                       ..
                                                                     .
       ...  . ,,..                                                    .MMM
     ZMMMMMMMMMMMMMM,             .. ..  .  .NMM7                     .$MM                                          . .
 +MMMMMMMMM?.  ..  ...            ?NZ     DMMMMMMM                      MM$..                                     .  ZD~
MMMMM? .. MM=.        .MM .    MMMMM8.. NMMMM:.+MM~       ...   ...  ...MMM.      .   .  .   DMMMM?      MMM    ..MMMMM,
          MMM          MM$   MMMMM    ,MMMM    .MM8.   .  MMMMMMM+      MMM   .   7MMM.    MMMMMMMMM.    MMM    MMMMZ
          MMM          MMM  MMMM..     MM..     MMM.  .  MMMM..NMM.     MMM    $MMMMM=    MMM.....$MM    DMM= OMMMM
          MMM          MMM MMM$                .MMM     MMM... . .      MMMIOMMMMM,     .MMM+$MMMMMMM    :MMM.MMM.
         .MMM          IMM~MMZ .           .$O: MMM   .NMM ... .  .     $MMMMMM7.        MMMMMMMMM~  .    MMMMMM
          MMM           MMMMM .        . MMMMMMMMMM    MMM              .MMMMMMI         DMM..... . .  .  MMMMM7.
          MMM.          MMMM=         . MMMM. MMMMM.  .MMM  .      MD    MMMMMMMMN    .   MMM. .  . MM  ..OMMMM.
          MMM.         .MMMM.        . MMM= ...=MMMM...$MMM....$MMMMM   .MMM. ,MMMMM.    .,MMMM?7MMMM+   . MMMM
          NMM.          $MMM.        ..MMM. ..MMMMMMI...OMMMMMMMMMM.     NMM     MMMMM   .. MMMMMMMM       MMMM
          ?MM            MMM           MMMMMMMMMM        .:NMMI          ~MM        MMM .                  .MM=.
          ...            ..             DMMMMM:            .              MM+     ...                         ..
                                       ...                               . Z
    '''

    print 'Welcome to the iPhone 6+ CLI tracking tool v1.1.2, from Risto Keravuori (www.risto.io).\n' \
          'Please enjoy, and good luck in your search!'

    mode = get_mode()

    if mode == 4:
        with open(join(FILE_PATH, 'previous.pickle'), 'rb') as f:
            data = load(f)

        zip_code = data['zip_code']
        target_stores = data['target_stores']
        alert_models = data['alert_models']
        beep_models = data['beep_models']

        print '\nRestarting monitoring with the following settings:'
        print '-- zip code: %s' % zip_code
        print '-- target_stores: ',
        for store in target_stores[:-1]:
            print '%s, ' % store,
        print target_stores[-1]
        print '-- alert models: ',
        for model in alert_models[:-1]:
            print '%s, ' % nice_model_name(model),
        print nice_model_name(alert_models[-1]) if alert_models else '--'
        print '-- beep models: ',
        for model in beep_models[:-1]:
            print '%s, ' % nice_model_name(model),
        print nice_model_name(beep_models[-1]) if beep_models else '--'

    else:
        zip_code = get_zip_code()
        target_stores = get_target_stores(zip_code)
        alert_models, beep_models = get_models(mode)
        with open(join(FILE_PATH, 'previous.pickle'), 'wb') as f:
            dump({'zip_code': zip_code,
                  'target_stores': target_stores,
                  'alert_models': alert_models,
                  'beep_models': beep_models}, f)

    start_monitoring(zip_code, target_stores, alert_models, beep_models)

def get_mode():
    while True:
        mode = raw_input('\nSelect a mode:\n'
                         '1. Monitor models with loud alert\n'
                         '2. Monitor models with quiet beep\n'
                         '3. Mix modes\n'
                         '4. Reload previous search terms\n'
                         ': ')
        if not match('[1-4]', mode):
            print '\n%s is not a valid mode' % mode
        else:
            return int(mode)