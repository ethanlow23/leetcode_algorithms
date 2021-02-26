class Solution {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> resultList = new ArrayList<List<Integer>>();
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            List<Integer> subList = new ArrayList<>();
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = q.poll();
                subList.add(node.val);
                if (node.left !== null) q.add(node.left);
                if (node.right !== null) q.add(node.right);
            }
            resultList.add(0, subList);
        }
        return resultList;
    }
}