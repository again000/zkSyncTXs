from web3 import Web3
from abi import contract_abi
import random
import time
from settings import *
from functions import *
import decimal as dc

choice = int(input("\n----------------------\n1: deposit\n2: withdraw\n3: check contract balance\n4: check wallet balance\nChoice: "))

eth_min = float(eth_min)
eth_max = float(eth_max)
private_keys = []
failed_keys = []
web3 = Web3(Web3.HTTPProvider(RPC))
contract_address = web3.to_checksum_address(contract_address)
contract = web3.eth.contract(contract_address, abi=contract_abi)

def download_wallets():
	with open('keys.txt', 'r') as f:
		for line in f:
			line = line.strip()
			private_keys.append(line)
	return private_keys

def main():
	private_keys = download_wallets()
	for key in private_keys:
		try:
			if choice == 1:
				if 		swap_all_balance == True:
					balance = check_balance_wallet(key)			
					value = dc.Decimal.from_float(float("0.0000" + str(random.randrange(keep_value_from,keep_value_to))))
					# balance minus value
					value_eth = "{:.8f}".format(balance - value)   
					value_wei = web3.to_wei(value_eth, 'ether')
					deposit_swap(value_wei,pvt_key)
				elif 	swap_all_balance == False:
					deposit(eth_min, eth_max, key)
				else:
					print("Something wrong with settings.py")
			elif choice == 2:
				if 		swap_all_balance == True:
					withdraw(key)
				elif	swap_all_balance == False:
					withdraw(key)
				else:
					print("Something wrong with settings.py")
			elif choice == 3:
				check_balance(key)
			elif choice == 4:
				print(f"""Wallet: {web3.eth.account.from_key(key).address} and it's balance {"{:.8f}".format(check_balance_wallet(key))}""")
			else:
				print(f"Wrong choice number. 1 | 2 | 3 | 4")
		except Exception as e:
			print(f"Transaction failed for private key: {key} | Error: {e}")
			failed_keys.append(key)

if __name__ == "__main__":
	main()
    
# print("\n\nFailed keys: ")
# for failed in failed_keys:
#     print(failed)
