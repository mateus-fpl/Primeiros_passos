import java.util.Scanner;

public class vetor5{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        int[] a = new int[10];
        int soma = 0;
        System.out.println("Digite seus valores:");
        for (int i=0; i<10; i++){
            System.out.print("Posição " + i + ": ");
            a[i] = scanner.nextInt();
            soma = soma + a[i];
        }
        System.out.println("A soma dos números é:" + soma);
        scanner.close();
    }
    
}