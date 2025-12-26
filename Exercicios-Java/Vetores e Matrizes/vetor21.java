import java.util.Scanner;

public class vetor21 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a[] = new int[10];
        int b[] = new int[10];
        int c[] = new int[10];
        int i = 0;
        System.out.println("Digite os valores do vetor A:");
        for (i=0; i<10; i++){
            System.out.print("Posição " + i + ": ");
            a[i] = scanner.nextInt();
        }

        System.out.println("Digite os valores do vetor B:");
        for (i=0; i<10; i++){
            System.out.print("Posição " + i + ": ");
            b[i] = scanner.nextInt();
        }

        for (i=0; i<10; i++){
            c[i] = a[i] - b[i];
            System.out.println("C[" + i + "]: " + c[i]);
        }
        scanner.close();
    }
}
