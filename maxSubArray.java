class Solution {
    public int maxSubArray(int[] nums) {
        int sum = nums[0];
        int currSum = nums[0];
        
        for(int i = 1; i < nums.length; i++){ //loop through array
            
            currSum = Math.max(nums[i], currSum += nums[i]); //compare current element and see if it should continue adding
            
            if(sum < currSum){
                sum = currSum; //update the answer
            }      
        }
        return sum;
        
    }
}
