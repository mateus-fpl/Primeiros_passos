import java.util.Scanner;

public class repet11 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int i;
        int n;
        System.out.println("Digite um número:");
        n = scanner.nextInt();

        for (i=0; i<n;i++){
            System.out.print(i + " ");
        }
        scanner.close();
    }
}
