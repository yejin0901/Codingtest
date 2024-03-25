public class Solution {
    public String solution(String s) {
        StringBuilder answer = new StringBuilder();
        String[] sList = s.split(" ", -1); 
        
        for (int i = 0; i < sList.length; i++) {
            if (!sList[i].isEmpty()) {
                answer.append(Character.toUpperCase(sList[i].charAt(0)));
                if (sList[i].length() > 1) {
                    answer.append(sList[i].substring(1).toLowerCase());
                }
            }
            
            if (i < sList.length - 1) {
                answer.append(" ");
            }
        }
        
        return answer.toString();
    }
}
