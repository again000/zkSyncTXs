from web3 import Web3
from abi import contract_abi
import random
import time
from settings import *

def random_sleep():
    sleep_duration = random.randint(from_sec, to_sec)
    print(f"Sleeping for {sleep_duration} seconds")
    time.sleep(sleep_duration)

def deposit(min_val, max_val, pvt_key):
	address = web3.eth.account.from_key(pvt_key).address
	value_eth = "{:.8f}".format(random.uniform(min_val, max_val))
	value_wei = web3.to_wei(value_eth, 'ether')
	transaction = contract.functions.deposit().build_transaction({
		'from': web3.to_checksum_address(address),
		'value': value_wei,
		'gasPrice': web3.to_wei(0.25, 'gwei'),
		'nonce': web3.eth.get_transaction_count(web3.to_checksum_address(address))
	})
	transaction['gas'] = int(web3.eth.estimate_gas(transaction))
	signed_txn = web3.eth.account.sign_transaction(transaction, pvt_key)
	transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction).hex()
	random_sleep()
	return print(f"Deposited {value_eth} ETH | Hash: {transaction_hash}")

def deposit_swap(keep_value_from,keep_value_to,pvt_key):
	address = web3.eth.account.from_key(pvt_key).address
	balance = check_balance_wallet(pvt_key)			
	value = dc.Decimal.from_float(float("0.0000" + str(random.randrange(keep_value_from,keep_value_to))))
	# balance minus value
	value_eth = "{:.8f}".format(balance - value)   
	value_wei = web3.to_wei(value_eth, 'ether')
	transaction = contract.functions.deposit().build_transaction({
		'from': web3.to_checksum_address(address),
		'value': value_wei,
		'gasPrice': web3.to_wei(0.25, 'gwei'),
		'nonce': web3.eth.get_transaction_count(web3.to_checksum_address(address))
	})
	transaction['gas'] = int(web3.eth.estimate_gas(transaction))
	signed_txn = web3.eth.account.sign_transaction(transaction, pvt_key)
	transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction).hex()
	random_sleep()
	return print(f"Deposited {value_eth} ETH | Hash: {transaction_hash}")

def withdraw(pvt_key):
	web3 = Web3(Web3.HTTPProvider(RPC))
	address = web3.eth.account.from_key(pvt_key).address
	contract = web3.eth.contract(contract_address, abi=contract_abi)
	balance = contract.functions.getBalance().call({'from': address})
	transaction = contract.functions.withdraw(
		balance
	).build_transaction({
		'from': web3.to_checksum_address(address),
		'value': 0,
		'gasPrice': web3.to_wei(0.25, 'gwei'),
		'nonce': web3.eth.get_transaction_count(web3.to_checksum_address(address))
	})
	transaction['gas'] = int(web3.eth.estimate_gas(transaction))
	signed_txn = web3.eth.account.sign_transaction(transaction, pvt_key)
	transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction).hex()
	random_sleep()
	return print(f"Withdrawing {web3.from_wei(balance, 'ether')} ETH for {address}\nHash: {transaction_hash}\nPrivate key: {pvt_key}")

def withdraw_swap(keep_value_from, keep_value_to, pvt_key):
	contract_balance = check_balance(pvt_key)
	value = dc.Decimal.from_float(float("0.0000" + str(random.randrange(keep_value_from,keep_value_to))))
	# balance minus value
	value_eth = "{:.8f}".format(contract_balance - value)
	balance = float(value_eth)
	if balance < 0:
		balance == 0
		raise Exception("Resulting wei value must be between 1 and 2**256 - 1")
	elif balance > 0:
		balance	
		try:
			balance = web3.to_wei(balance, 'ether')
		except Exception as e:
			print(f"""Wallet: {web3.eth.account.from_key(key).address} has a lower ballance. Error message: {e}""")
	else:
		pass
	transaction = contract.functions.withdraw(
		balance
	).build_transaction({
		'from': web3.to_checksum_address(address),
		'value': 0,
		'gasPrice': web3.to_wei(0.25, 'gwei'),
		'nonce': web3.eth.get_transaction_count(web3.to_checksum_address(address))
	})
	transaction['gas'] = int(web3.eth.estimate_gas(transaction))
	signed_txn = web3.eth.account.sign_transaction(transaction, pvt_key)
	transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction).hex()
	random_sleep()
	return print(f"Withdrawing {web3.from_wei(balance, 'ether')} ETH for {address}\nHash: {transaction_hash}\nPrivate key: {pvt_key}")

def check_balance_wallet(pvt_key):
	# we are using here pvt key and afterwards the function to get wallet for getting balance of native (eth)
	web3 = Web3(Web3.HTTPProvider(RPC))
	wallet_address = web3.eth.account.from_key(pvt_key).address
	random_sleep()
	return web3.from_wei(web3.eth.get_balance(wallet_address),"ether")

def check_balance(pvt_key):
	web3 = Web3(Web3.HTTPProvider(RPC))
	contract = web3.eth.contract(contract_address, abi=contract_abi)
	address  = web3.eth.account.from_key(pvt_key).address
	balance  = contract.functions.getBalance().call({'from': address})
	random_sleep()
	print(f"Address: {address}\nPrivate key: {pvt_key}\nBalance: {web3.from_wei(balance, 'ether')} ETH\n")
	return balance