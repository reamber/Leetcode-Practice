class Solution {
    public int maxProfit(int[] prices) {
        int globalProfit = 0;
        
        for(int i = 1; i < prices.length; i++){
            int profit = prices[i] - prices[i-1]; //5-1 = 4, 6-3 = 3
            
            if(profit > 0){
                globalProfit += profit;
                
            }
            
        }
        
        return globalProfit;
        
    }
}
