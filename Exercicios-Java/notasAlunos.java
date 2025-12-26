import java.util.Scanner;

public class notasAlunos {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Sistema de Média e Classificação da Turma (10 Alunos):");
        
        double nota;
        double soma = 0;
        int total = 10;
        int i;
        
        int abaixo_5 = 0;
        int entre_5_e_69 = 0;
        int acima_7 = 0;
        
        for (i = 1; i <= total; i++){
            System.out.print("Digite a nota do aluno " + i + ": ");
            nota = scanner.nextDouble();
            soma = soma + nota;

            if (nota < 5.0) {
                abaixo_5++;
            } else if (nota >= 5.0 && nota < 7.0) {
                entre_5_e_69++;
            } else {
                acima_7++;
            }
        }
        
        double media = soma / total;
        
      
        System.out.println("A soma total das notas é: " + soma);
        System.out.printf("A média da turma é: %.2f\n", media);
        System.out.println("Abaixo de 5,0: " + abaixo_5 + " alunos");
        System.out.println("Entre 5,0 e 6,9: " + entre_5_e_69 + " alunos");
        System.out.println("Acima de 7,0: " + acima_7 + " alunos");
       

        scanner.close();
    }
}