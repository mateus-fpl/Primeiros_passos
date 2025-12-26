import java.util.Scanner;
public class nImpar {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int cont=1, impar=1;
        System.out.println("Digite um número:");
        int n = scanner.nextInt();
        scanner.close();
        while (cont <= n){
            System.out.print(impar + " ");
            cont++;
            impar = impar + 2;
        }
        
    }
}
