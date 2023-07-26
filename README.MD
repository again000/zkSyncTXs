<!-- BUBBLE SCRIPTS INC -->

<!-- 
Base scripts
 -->

git init

git pull https://github.com/again000/zkSyncTXs.git

<!-- python -m pip freeze > requirements.txt -->
python -m pip install -r requirements.txt

<!-- selects changes -->
git add .
<!-- records changes LOCALLY -->
git commit -m "new file" 
<!-- shares changes -->
git push

git push --set-upstream https://github.com/again000/zkSyncTXs.git master


<!-- 

Script requirements

 -->

 <!-- 
 
Sladkiy

1) чекаем флаг swap_all_balance при вызове DEPOSIT, 
1.1) если флаг false, то берём значения из переменных eth_min и eth_max
1.2) если флаг true, то 
1.2.1) чекаем баланс кошелька на БЛОКЧЕЙНЕ (=balance_chain)
1.2.2) определяем сколько оставить на БЛОКЧЕЙНЕ путём выбора рандомной величины между keep_value_from и keep_value_to (разрядность keep_value_from и keep_value_to =8, те от xxx,00000001 до xxx,99999999)
1.2.3) считаем value будущей транзакции balance_chain - число из п 1.2.2
1.2.4) процессим транзакцию с балансом из п 1.2.3

Sladkiy 2
2) чекаем флаг swap_all_balance при вызове WITHDRAW, 
2.1) если флаг false, то берём значения из переменных eth_min и eth_max
2.2) если флаг true, то 
2.2.1) чекаем баланс кошелька на КОНТРАКТЕ (=balance_contract)
2.2.2) определяем сколько оставить на КОНТРАКТЕ путём выбора рандомной величины между keep_value_from и keep_value_to (разрядность keep_value_from и keep_value_to =8, те от xxx,00000001 до xxx,99999999)
2.2.3) считаем value будущей транзакции balance_contract - число из п 2.2.2
2.2.4) процессим транзакцию с балансом из п 2.2.3

таким образом если я хочу ЗАДЕПОЗИТИТЬ макс баланс кошеля в контракт, я делаю swap_all_balance=true и оставляю немного ETH чтобы вывести деньги из контракта

а если я хочу ВЫВЕСТИ весь баланс из контакта, я делаю swap_all_balance=true и keep_value_from=keep_value_to=0
 
-->