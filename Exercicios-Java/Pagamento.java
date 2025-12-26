import java.util.Scanner;
public class Pagamento {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        double valor, p1, p2, desconto, novoValor,acrescimo;
        System.out.println("Digite o valor da compra:");
        valor = scanner.nextDouble();
        System.out.println("Forma de pagamento: \n 1.A vista \n 2.A prazo");
        p1 = scanner.nextDouble();
        if (p1 == 1){
            System.out.println("1.Boleto \n 2.PIX");
            p2 = scanner.nextDouble();
            if (p2 == 1){
                System.out.println("O preço é: " + valor);
            } else if (p2 == 2) {
                desconto = (valor * 0.05);
                novoValor = valor - desconto;
                System.out.println("O valor com 5% de desconto é: " + novoValor);
            } else {
                System.out.println("Não existe essa opcao");
            }
        } else if (p1 == 2){
            System.out.println("Parcelas: \n Opçao 1 - 2 vezes: acrescimo de 5% \n Opcao 2 - 3 vezes: acrescimo de 10%");
            p2 = scanner.nextDouble();
            if (p2 == 1){
                acrescimo = (valor * 1.05)/2;
                System.out.println("O valor de cada parcela com acrescimo de 5% de juros será: " + acrescimo);
            } else if (p2 == 2) {
                acrescimo = (valor * 1.10)/2;
                System.out.println("O valor de cada parcela com acrescimo de 10% de juros será: " + acrescimo);
            } else {
                System.out.println("Não existe essa opcao");
            }
        }
        scanner.close(); 
    }
}
