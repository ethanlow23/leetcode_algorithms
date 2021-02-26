class Solution {
    public String countAndSay(int n) {
        String result = "1";
        String countSay;
        int count;
        char say;
        for (int i = 1; i < n; i++) {
            countSay = result;
            result = "";
            count = 1;
            say = countSay.charAt(0);
            for (int j = 1; j < countSay.length(); j++) {
                if (countSay.charAt(j) != say) {
                    result += Integer.toString(count) + say;
                    count = 1;
                    say = countSay.charAt(j);
                } else {
                    count++;
                }
            }
            result += Integer.toString(count) + say;
        }
        return result;
    }
}