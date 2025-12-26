import java.util.Scanner;

public class repet14 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int i, n;
        System.out.println("Digite um número par:");
        n = scanner.nextInt();
        System.out.println("\n");
        if (n % 2 == 0) {
            for (i = 0; i < n; n--) {
                if (n%2 == 0){
                    System.out.print((n-2) + " ");
                }
            }
        } else {
            System.out.println("Falei que era par! Programa encerrado.");
        }
        scanner.close();
    }
}
    