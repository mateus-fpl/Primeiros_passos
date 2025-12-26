import java.util.Scanner;

public class repet12 {
    public static void main(String [] args){
        Scanner scanner = new Scanner(System.in);
        int i,n;
        System.out.println("Digite um número");
        n = scanner.nextInt();

        for (i=0; i<n; n--){
            System.out.println((n-1) + " ");
        }
        scanner.close();
    }
}
