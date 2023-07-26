
#--CONFIG--#

#Insert Private keys in keys.txt; One key per line | Приватные ключи в созданный файл keys.txt. По 1 в строку, не должны начинаться с 0x
from_sec = 1      #|Wait from N seconds between transactions | Минимальное значение "ждать от N sec между транзакиями". Для рандомного выбора 
to_sec = 100	    #|Wait to N seconds between transactions | Максиимальное значение "спать до N sec между транзакциями". Для рандомного выбора 
eth_min = 0.00001 #|Min ETH quantity for deposit | Значение ETH минимального депозита. Для рандомного выбора
eth_max = 0.0001   #|Max ETH quantity for deposit | Значение ETH максимального депозита. Для рандомного выбора
contract_address = "0x7442E417C0B53d622d93F5D7BbD84eEd808F26C5" #|Contract address. DO NOT CHANGE if own contract is not deployed | Адрес контракта. НЕ МЕНЯТЬ если не свой не деплоили
RPC = "https://mainnet.era.zksync.io" #|RPC for web3 provider. DO NOT CHANGE if you dont have own RPC | RPC web3 провайдера. НЕ МЕНЯТЬ если нет своей
#----------#
# flag true/false
swap_all_balance = True

# от скольки монет оставлять
# до скольки монет оставлять
keep_value_from = 0
keep_value_to   = 0
#----------#