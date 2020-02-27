class Solution {
    public int removeDuplicates(int[] nums) {
        int count = 1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != nums[count]) {
                count++;
                nums[count] = nums[i];
            }
        }
        return count + 1;
    }
}