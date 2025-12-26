import java.util.Scanner;

public class vetor14 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a[] = new int[10];
        int i, j;

        System.out.println("Digite os números do arranjo:");

        // Lê todos os números primeiro
        for (i = 0; i < 10; i++) {
            a[i] = scanner.nextInt();
        }

        System.out.println("\nNúmeros repetidos encontrados:");

        // Compara cada elemento com os que vêm depois
        for (i = 0; i < 10; i++) {
            for (j = i + 1; j < 10; j++) {
                if (a[i] == a[j]) {
                    System.out.println(a[i]);
                }
            }
        }

        scanner.close();
    }
}