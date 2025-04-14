
import java.rmi.Naming;

public class Client {
    public static void main(String[] args) {
        try {
            // Busca el servicio en el registro RMI
            Calculator calculator = (Calculator) Naming.lookup("rmi://localhost/CalculatorService");
            
            // Llama al método remoto
            int result = calculator.add(5, 3);
            System.out.println("Resultado de la suma: " + result);
        } catch (Exception e) {
            System.err.println("Excepción en el cliente RMI:");
            e.printStackTrace();
        }
    }
}
