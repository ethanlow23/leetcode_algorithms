# Best Time to Buy and Sell Stock

def maxProfit(prices):
  cur_min = prices[0]
  max_profit = 0
  for price in prices:
    if price < cur_min:
      cur_min = price
    else:
      max_profit = max(max_profit, price - cur_min)
  return max_profit
