class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> pTriangle = new ArrayList<>();
        for (int i = 0; i < numRows; i++) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < i + 1; j++) {
                if (j == 0 || j == i) {
                    row.add(1);
                } else {
                    row.add(pTriangle.get(i - 1).get(j) + pTriangle.get(i - 1).get(j - 1));
                }
            }
            pTriangle.add(row);
        }
        return pTriangle;
    }
}