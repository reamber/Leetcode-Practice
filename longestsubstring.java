class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        int i = 0; //pointer that sticks at beginning, won't move unless j hits dup
        int j = 0; //pointer that moves
        int max = 0; //result we want to return, the length
        
        HashSet<Character> set = new HashSet<Character>();
        
        while(j < s.length()){
            
            if(!set.contains(s.charAt(j))){//checks for no prev char, prevent dup
                set.add(s.charAt(j));
                j++; //move j upp
                max = Math.max(max, j-i); //track longer substring
            }
            else{ //if it is a dup character
                //we want to move i pointer up, remove the starting dup
                set.remove(s.charAt(i));
                i++; //move up from starting pointer
            }
        }
        return max;
        
    }
}
