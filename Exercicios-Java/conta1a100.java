//exibir os valores de 1 a 100, utilizando while
public class conta1a100 {

    public static void main(String[] args) {
        int cont = 1;
        System.out.println("numeros de 1 a 100:");
        while (cont <= 100) { //teste: valor final
            System.out.print(cont + " ");
            cont = cont + 1; //cont++ : atualizacao
        }
        System.out.println("\ncont na saida: " + cont);
    }
}