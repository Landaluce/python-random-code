from typing import List


def get_max_profit(prices: List[int]) -> int:
    profits = [prices[y] - prices[x] for x in range(len(prices))
               for y in range(x + 1, len(prices)) if prices[y] > prices[x]]
    return max(profits) if profits else 0


def main():
    print(get_max_profit([7, 1, 5, 3, 6, 4]), "sol = 5")
    # Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.
    print(get_max_profit([7, 6, 4, 3, 1]), "sol = 0")
    # Explanation: In this case, no transaction is done, so the maximum profit is 0.


if __name__ == "__main__":
    main()
