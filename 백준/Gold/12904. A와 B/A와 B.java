import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

// a,b 로만 존재
// 문자열 뒤에 A추가 / 문자열 뒤집고 뒤에 B추가
// 만들 수 있는가 없는가







public class Main {
    static int[] parent;

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        String S = sc.next();
        StringBuilder T = new StringBuilder(sc.next());

        while(T.length() > S.length()){
            if(T.charAt(T.length()-1) == 'A'){
                T.deleteCharAt(T.length()-1);
            } else if(T.charAt(T.length()-1) == 'B'){
                T.deleteCharAt(T.length()-1);
                T.reverse();
            }
        }
        
        if(T.toString().equals(S)){
            System.out.println(1);
        } else{
            System.out.println(0);
        }
        
        sc.close();





    }







}