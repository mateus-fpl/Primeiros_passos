
import java.util.Scanner;

public class DivisivelPorTres {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite um numero inteiro:");
        int n = scanner.nextInt();
        int copia = n;
        int soma = 0;
        while (n > 0) {
            soma = soma + n % 10; //soma += n%10
            n = n / 10;

        }
        scanner.close();
        if (soma % 3 ==0) {
            System.out.println(copia + " e divisivel por 3");
        } else {
            System.out.println(copia + " nao e divisivel por 3");
        }
    }
}
