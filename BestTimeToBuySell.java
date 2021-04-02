class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int current = 0; 
        for(int i = 1; i < prices.length; i++){
            
            current = Math.max(prices[i] - prices[i-1], current += prices[i] - prices[i-1] );
            
            if(profit < current){
                profit = current;
            }      
        }
        return profit;
        
    }
}
