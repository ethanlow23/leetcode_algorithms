class Solution {
    public int mySqrt(int x) {
        int left = 1;
        int right = x / 2;
        int res = 0;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (mid > x / mid) {
                right = mid - 1;
            } else {
                left = mid + 1;
                res = mid;
            }
        }
        return res;
    }
}