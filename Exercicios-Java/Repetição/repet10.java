import java.util.Scanner;

public class repet10 {
    public static void main (String[] args){
        Scanner scanner = new Scanner(System.in);
        int i, soma = 0;
        System.out.println("Digite um número:");
        for(i=1; i<100;i++){
            if (i%2 == 0){
                soma = soma + i;
                System.out.println("A soma dos 50 primeiros números pares é: " + soma);
            }
        }
        scanner.close();
    }
}
