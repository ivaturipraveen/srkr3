def min_coins(coins, target):
    # Initialize an array to store minimum number of coins needed for each value from 0 to target
    dp = [float('inf')] * (target + 1)
    dp[0] = 0  # No coins needed to make value 0

    # Iterate through each coin
    for coin in coins:
        # Update dp array for each value from the coin value to the target
        for i in range(coin, target + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[target] if dp[target] != float('inf') else -1  # Return -1 if target is not achievable

# Example usage:
coins = [1, 2, 5]
target_value = 11

result = min_coins(coins, target_value)
if result != -1:
    print(f"Minimum number of coins needed to make {target_value}: {result}")
else:
    print(f"Cannot make {target_value} with the given coins.")
