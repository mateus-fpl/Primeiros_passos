//ler um número inteiro n positivo e exibir os números os n primeiros impares
//Se n=5, exibir 1,3,5,7,9
import java.util.Scanner;

public class ImparFor1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite um número inteiro positivo: ");
        int n = scanner.nextInt();
        while (n <= 0){
            System.out.print("O número deve ser positivo");
            n = scanner.nextInt();
        }
        System.out.println("\nVeja os " + n + " os primeiros impares:");
        int impar = 1;
        for (int cont=1; cont <=n; cont=cont + 1){
            System.out.print(impar + " ");
            impar = impar + 2;
        }
        
        scanner.close();
    }
}