import java.util.Scanner;

public class vetor39 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int i, n, j;
        int contador = 1;
        System.out.println("Digite um número positivo:");
        n = scanner.nextInt();
        for (i = 1; i <= n; i++) {
            for (j = 1; j <= i; j++) {
                System.out.print(contador + " ");
                contador++;
            }
            System.out.println();
        }
        scanner.close();
    }
}
