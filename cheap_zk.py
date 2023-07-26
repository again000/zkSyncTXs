from web3 import Web3
from abi import contract_abi
import random
import time
from settings import *
from functions import *


eth_min = float(eth_min)
eth_max = float(eth_max)
private_keys = []
failed_keys = []
web3 = Web3(Web3.HTTPProvider(RPC))
contract_address = web3.to_checksum_address(contract_address)
contract = web3.eth.contract(contract_address, abi=contract_abi)

choice = int(input("\n----------------------\n1: deposit\n2: withdraw\n3: check balance\nChoice: "))


with open('keys.txt', 'r') as f:
    for line in f:
        line = line.strip()
        private_keys.append(line)


for key in private_keys:
    try:
        if choice == 1:
			if 		swap_all_balance == True:
				check_balance(key)
				deposit(eth_min, eth_max, key)
			elif 	swap_all_balance == False:
				deposit(eth_min, eth_max, key)
			else:
				print("Something wrong with settings.py")
        elif choice == 2:
			if 		swap_all_balance == True:
				withdraw(key)
			elif	swap_all_balance == False::
				withdraw(key)
			else:
				print("Something wrong with settings.py")
        elif choice == 3:
              check_balance(key)
        else:
              print(f"Wrong choice number. 1 | 2 | 3")
    except Exception as e:
        print(f"Transaction failed for private key: {key} | Error: {e}")
        failed_keys.append(key)
    
print("\n\nFailed keys: ")
for failed in failed_keys:
    print(failed)
