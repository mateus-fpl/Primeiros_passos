import java.util.Scanner;

public class media {
    public static void main (String[] args){
    Scanner scanner = new Scanner(System.in);
       int cont = 1; 
       int soma = 0;
       int n;
              
       double media;
       while (cont <=10){
        System.out.println("Digite o proximo numero:");
        n = scanner.nextInt();
        soma = soma + n ;
        cont++;
       }
       media = (double) soma/10.0;
       System.out.println("A media é: " + media);
       scanner.close();
    }
}
