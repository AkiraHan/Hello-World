class Solution {
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        int val = 0;
        if(t1 == null && t2 == null) return null;
        else if(t1 == null) return t2;
        else if(t2 == null) return t1;
        else val = t1.val + t2.val;
        TreeNode cur = new TreeNode(val);
        /**if(t1 == null){
            cur.left = mergeTrees(null, t2.left);
            cur.right = mergeTrees(null, t2.right);
        }
        else if(t2 == null){
            cur.left = mergeTrees(t1.left , null);
            cur.right = mergeTrees(t1.right, null);
        }**/
        
        cur.left = mergeTrees(t1.left, t2.left);
        cur.right = mergeTrees(t1.right, t2.right);
        
        return cur;
    }
}
