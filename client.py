from tinkoff.invest import Client

import tokenRead

def getClient(tokenPath):
     return Client(tokenRead.getFirstLine(tokenPath)[0])