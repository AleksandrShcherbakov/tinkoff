import client
import sys
import logging

PATH_LOG = './log'

if __name__ == '__main__':
    logging.basicConfig(filename=PATH_LOG, level=logging.INFO)
    logging.info('start working')

    try:
        pathToken = sys.argv[1]
    except RuntimeError:
        logging.error('no path to file with token in argv[1]')
        raise RuntimeError('no path to file with token in argv[1]')

    with (client.getClient(pathToken)) as client:
        accountsResp = client.users.get_accounts()
        print(accountsResp)
        instrumentStatus = client.instruments.shares()
        print(instrumentStatus)
