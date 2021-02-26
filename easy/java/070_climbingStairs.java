class Solution {
    public int climbStairs(int n) {
        if (n < 0) return 0;
        if (n < 2) return 1;
        int[] memo = new int[n + 1];
        if (memo[n] != 0) {
            return memo[n];
        } else {
            memo[n] = climbStairs(n - 1) + climbStairs(n - 2);
            return memo[n];
        }
    }
}