class Solution {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        //TreeNode root = new TreeNode();
        List<Integer> NL = new ArrayList<Integer>();
        for(int i = 0; i < nums.length; i++)
            NL.add(nums[i]);
        return consTree(NL);
    }
    
    private TreeNode consTree(List<Integer> NL){
        if(NL.size() == 0) return null;
        int max = 0;
        int count = 0;
        for(int i = 0; i < NL.size(); i++){
            if(NL.get(i) > max){
                max = NL.get(i);
                count = i;
            }
        }
        TreeNode cur = new TreeNode(max);
        cur.left = consTree(NL.subList(0,count));
        cur.right = consTree(NL.subList(count+1,NL.size()));
        return cur;
    }
}
