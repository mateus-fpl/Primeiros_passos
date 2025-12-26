// Ler o prêmio da loteria, ler o percentual de aposta de três amigos, calcular o 
//valor que cada um leva e exibir

import javax.swing.JOptionPane;

public class Loteria {
    public static void main(String[] args) {

        String aux;

        //Entrada de dados
        double premio = Double.parseDouble(JOptionPane.showInputDialog("Digite o premio da semana"));

        double apostaAmigo1 = Double.parseDouble(JOptionPane.showInputDialog("Quanto o amigo 1 apostou?"));

        double apostaAmigo2 = Double.parseDouble(JOptionPane.showInputDialog("Quanto o amigo 2 aposrtou?"));

        double apostaAmigo3 = Double.parseDouble(JOptionPane.showInputDialog("Quanto o amigo 3 apstou?"));

        double apostaTotal = apostaAmigo1 + apostaAmigo2 + apostaAmigo3;

        //Processamento de dados
        double premio1 = apostaAmigo1 / apostaTotal * premio;
        double premio2 = apostaAmigo2 / apostaTotal * premio;
        double premio3 = apostaAmigo3 / apostaTotal * premio;

        //Saída de dados
        aux = "O amigo 1 leva R$ " + String.format("%.2f", premio1) + "\nO amigo 2 leva R$ " + String.format("%.2f", premio2)
         + "\nO amigo 3 leva R$ " + String.format("%.2f", premio3);
        JOptionPane.showMessageDialog((null), aux);
        
    }
    
}
