class Solution {
    public String addBinary(String a, String b) {
        String answer = "";
        int aIndex = a.length() - 1;
        int bIndex = b.length() - 1;
        int sum = 0;
        while (aIndex >= 0 || bIndex >= 0) {
            if (aIndex >= 0) {
                sum += a.charAt(aIndex--) - '0';
            }
            if (bIndex >= 0) {
                sum += b.charAt(bIndex--) - '0';
            }
            answer = Integer.toString(sum % 2) + answer;
            sum /= 2;
        }
        return answer = sum == 0 ? answer : Integer.toString(sum % 2) + answer;
    }
}