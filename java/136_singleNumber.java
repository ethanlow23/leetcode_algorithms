class Solution {
    public int singleNumber(int[] nums) {
        Map<Integer, Integer> values = new HashMap<>();
        for (int i : nums) {
            values.put(i, values.getOrDefault(i, 0) + 1);
        }
        for (int i : nums) {
            if (values.get(i) == 1) {
                return i;
            }
        }
        return 0;
    }
}