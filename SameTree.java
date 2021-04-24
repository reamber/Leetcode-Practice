class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        Boolean check = false;
        if(p == null && q == null){
            return true;
        }
        if(p == null || q == null){
            return false;
        }
        if (p.val == q.val){
            check = true; 
            return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
        }
        else{
            check = false;
        }
        return check;
        
    }
}
