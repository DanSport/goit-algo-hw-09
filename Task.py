import time

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    change = {}
    for coin in coins:
        num_coins = amount // coin
        if num_coins > 0:
            change[coin] = num_coins
            amount -= num_coins * coin
        if amount == 0:
            break
    return change

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    change = {}
    for coin in reversed(coins):
        while amount >= coin and dp[amount] == dp[amount - coin] + 1:
            if coin not in change:
                change[coin] = 1
            else:
                change[coin] += 1
            amount -= coin
    return change

# Приклад використання
amount = 11951113
print("Жадібний алгоритм:", find_coins_greedy(amount))
print("Динамічне програмування:", find_min_coins(amount))

start_time = time.time()
find_coins_greedy(amount)
greedy_time = time.time() - start_time

start_time2 = time.time()
find_min_coins(amount)
dynamic_time = time.time() - start_time2

print("Час жадібного алгоритму:", greedy_time)
print("Час алгоритму динамічного програмування:", dynamic_time)
