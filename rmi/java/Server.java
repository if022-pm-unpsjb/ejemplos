import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;

public class Server {
    public static void main(String[] args) {
        try {
            // Crea una instancia del servicio
            CalculatorImpl calculator = new CalculatorImpl();
            
            // Inicia el registro RMI en el puerto por defecto (1099)
            LocateRegistry.createRegistry(1099);
            
            // Registra el servicio en el registro RMI
            Naming.rebind("CalculatorService", calculator);
            
            System.out.println("Servidor RMI está listo.");
        } catch (Exception e) {
            System.err.println("Excepción en el servidor RMI:");
            e.printStackTrace();
        }
    }
}
