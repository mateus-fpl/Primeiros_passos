import java.util.Scanner;

public class vetor18 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a[] = new int[10];
        int i,x;
        System.out.println("Digite os números do arranjo:");
        for (i=0; i<10; i++){
            a[i] = scanner.nextInt();
            
        }
        System.out.println("Digite um número positivo qualquer:");
        x = scanner.nextInt();
        System.out.println("\n");

        for (i=0; i<10; i++){
            if (a[i] % x == 0){
                System.out.print(a[i] + " ");
            }
        }
        scanner.close();
    }
}
