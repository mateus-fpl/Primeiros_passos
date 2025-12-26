import java.util.Scanner;

public class repet9 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite um número");
        int i = 0;
        int n;

        n = scanner.nextInt();
        System.out.println("\n");
        
        for (i = 1; i<=n; i++){
            if (i%2 == 1)
            System.out.println(i);
        }
        
        scanner.close();
    }
}
