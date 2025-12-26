import java.util.Scanner;

public class repet5 {

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int soma = 0;
        System.out.println("Digite 10 valores abaixo:");
        for (int i=0; i<10; i++){
            int entrada = scanner.nextInt();
            soma = soma + entrada;
        }
        System.out.println("O resultado da soma é: " + soma);
        scanner.close();
    }
}