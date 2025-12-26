import java.util.Scanner;

public class repet6 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int soma = 0, entrada;
        double media;
        int i =0;
        System.out.println("Digite os valores das notas:");
        for (i=0; i<10;i++){
            entrada = scanner.nextInt();
            soma = soma + entrada;
        }
        media = (double) soma/i;
        System.out.println("O total das notas é: " + soma + " e sua média é:" + media);
        scanner.close();
    }
}
