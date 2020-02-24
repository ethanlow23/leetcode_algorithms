class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> values = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int remainder = target - nums[i];
            if (values.containsKey(remainder)) {
                return new int[] { values.get(remainder), i };
            }
            values.put(nums[i], i);
        }
        throw new IllegalArgumentException("No Solution");
    }
}