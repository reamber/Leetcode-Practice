class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>(); //stack
        // () -> stack (,if next c == ) and you pop (
        //fifo
        //[()] -> [(
        //when u get to ), you want to pop (
        //when you get to [, you want to pop ]
        
        for (char c : s.toCharArray()) { //[()]
            if(c == '(' || c == '[' || c == '{') stack.push(c); //[(
            else if(stack.empty()) return false;
            else if(c == ')' && stack.pop() != '(') return false;//) pop (
            else if(c == ']' && stack.pop() != '[') return false;
            else if(c == '}' && stack.pop() != '{') return false;
        }
        return stack.isEmpty(); 
        
    }
}
