import subprocess
import json
import os
from pprint import pprint

from constants import *

# including mnemonic
mnemonic = os.getenv('MNEMONIC', 'tissue result rent stamp virus test kite spread advance glory order gauge')


def derive_wallets():
    command = './derive -g --mnemonic='mnemonic' --coin --numderive --cols=path,address,privkey,pubkey --format=json'

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()

    keys = json.loads(output)

    return keys

coins = {ETH: derive_wallets(coin=ETH), BTCTEST: derive_wallets(coin=BTCTEST)}

#pprint (coins)
#print(keys)
