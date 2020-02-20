class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        int reversed = 0;
        while(x > reversed) {
            reversed = (reversed * 10) + (x % 10);
            x /= 10;
        }
        return x == reversed || x == reversed / 10;
    }
}