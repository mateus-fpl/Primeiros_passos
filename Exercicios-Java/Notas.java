import java.util.Scanner;

public class Notas {
    public static void main (String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite a primeira nota: ");
        double nota1 = scanner.nextDouble();
        System.out.println("Digite a segunda nota:");
        double nota2 = scanner.nextDouble();
        double media = (nota1 + nota2)/2;
        if (media <= 2){
            System.out.println("Media: " + media + ". Aluno reprovado");
        }
        else if (media < 6 ) {
            System.out.println("Media: " + media + ". Aluno deve fazer P3");
        }
        else {
            System.out.println("Media: " + media + ". Aluno aprovado!");
        }
    }
}
