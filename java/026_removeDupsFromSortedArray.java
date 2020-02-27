// [1,1,2]
// [0,0,1,1,1,2,2,3,3,4]

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