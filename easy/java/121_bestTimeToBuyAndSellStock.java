class Solution {
    public int maxProfit(int[] prices) {
        int buyPrice = Integer.MAX_VALUE;
        int maxProfit = 0;
        for (int i = 0; i < prices.length; i++) {
            buyPrice = prices[i] < buyPrice ? prices[i] : buyPrice;
            maxProfit = prices[i] - buyPrice > maxProfit ? prices[i] - buyPrice : maxProfit;
        }
        return maxProfit;
    }
}