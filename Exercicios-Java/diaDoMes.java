import java.util.Scanner;
public class diaDoMes {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o número do mês (1 a 12): ");
        int mes = scanner.nextInt();

        System.out.print("Digite o ano: ");
        int ano = scanner.nextInt();

        int dias;

        switch (mes) {
            case 1: case 3: case 5: case 7: case 8: case 10: case 12:
                dias = 31;
                break;
            case 4: case 6: case 9: case 11:
                dias = 30;
                break;
            case 2:
                // Verifica se é ano bissexto
                if ((ano % 400 == 0) || (ano % 4 == 0 && ano % 100 != 0)) {
                    dias = 29;
                } else {
                    dias = 28;
                }
                break;
            default:
                System.out.println("Mês inválido!");
                scanner.close();
                return;
        }

        System.out.println("O mês " + mes + " do ano " + ano + " tem " + dias + " dias.");
        scanner.close();
    }
}
