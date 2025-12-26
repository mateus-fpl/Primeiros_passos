import java.util.Scanner;

public class repet15 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int i, n;
        System.out.println("Digite um número ímpar");
        n = scanner.nextInt();
        System.out.println("\n");
        if (n % 2 == 1) {
            for (i = 1; i < n; i++) {
                if (i%2 == 1){
                    System.out.print(i + " ");
                }
            }
        } else {
            System.out.println("Falei que era ímpar! Programa encerrado.");
        }
        scanner.close();
    }
}
