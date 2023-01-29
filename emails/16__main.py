def sum_prices(prices):
    if (num_prices := len(prices)) < 2:
        print(f"You passed {num_prices} price(s) but must pass at least 2!")
        return

    prices_sum = sum(prices)
    print(f"The sum of the prices is ${prices_sum}.")


sum_prices([1])
sum_prices([1, 2, 3])
