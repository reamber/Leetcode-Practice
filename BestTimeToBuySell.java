class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0; //answer to return
        int current = 0; //temp holder
        for(int i = 1; i < prices.length; i++){ //loop through array
            
            current = Math.max(prices[i] - prices[i-1], current += prices[i] - prices[i-1] ); //compare and pick larger profit. prices[i] = sell time prices[i-1] = buy time
            
            if(profit < current){
                profit = current; //update the answer
            }      
        }
        return profit;
        
    }
}
