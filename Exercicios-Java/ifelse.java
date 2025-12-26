import java.util.Scanner;
public class ifelse{
    public static void main (String[] args){
        var scanner = new Scanner(System.in);
        System.out.println("Informe o seu nome:");
        var name = scanner.next();
        System.out.println("Informe a sua idade:");
        var age = scanner.nextInt();
        System.out.println("Você é emancipado? (s/n)");
        var isEmancipated = scanner.next().equalsIgnoreCase("s");

        if (age >= 18){ 
            System.out.println("Bem vindo " + name);
            System.out.printf("%s, você tem %s anos, você pode dirigir \n", name, age);
        } else if (age >= 16 && isEmancipated) {
            System.out.printf("%s, apesar de você ter %s anos, você pode dirigir \n", name, age);
        }
        else {
            System.out.printf("%s, você não pode dirigir \n", name);
        }
        System.out.println("Fim da execução");
    }


}