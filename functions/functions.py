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
	print(f"Deposited {value_eth} ETH | Hash: {transaction_hash}")
	random_sleep()


def withdraw(pvt_key):
	address = web3.eth.account.from_key(pvt_key).address
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
	print(f"Withdrawing {web3.from_wei(balance, 'ether')} ETH for {address}\nHash: {transaction_hash}\nPrivate key: {pvt_key}")
	random_sleep()

def check_balance_wallet(pvt_key):
	# we are using here pvt key and afterwards the function to get wallet for getting balance of native (eth)
	web3 = Web3(Web3.HTTPProvider(RPC))
	wallet_address = web3.eth.account.from_key(pvt_key).address
	return web3.from_wei(web3.eth.get_balance(wallet_address),"ether")


def check_balance(pvt_key):
	web3 = Web3(Web3.HTTPProvider(RPC))
	contract = web3.eth.contract(contract_address, abi=contract_abi)
	address  = web3.eth.account.from_key(pvt_key).address
	balance  = contract.functions.getBalance().call({'from': address})
	print(f"Address: {address}\nPrivate key: {pvt_key}\nBalance: {web3.from_wei(balance, 'ether')} ETH\n")
	return balance