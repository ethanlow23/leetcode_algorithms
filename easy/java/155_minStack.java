class MinStack {

    /** initialize your data structure here. */
    private Stack<Integer> s1 = new Stack<>();
    private Stack<Integer> minS1 = new Stack<>();
    
    public MinStack() {
        
    }
    
    public void push(int x) {
        if (minS1.isEmpty() || x <= minS1.peek()) {
            minS1.push(x);
        }
        s1.push(x);
    }
    
    public void pop() {
        int x = s1.pop();
        if (x == minS1.peek()) {
            minS1.pop();
        }
    }
    
    public int top() {
        return s1.peek();
    }
    
    public int getMin() {
        return minS1.peek();
    }
}