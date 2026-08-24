import grpc
from concurrent import futures

# Importamos los archivos generados automáticamente
import calculadora_pb2
import calculadora_pb2_grpc

# Implementamos el servicio heredando de la clase generada
class ServicioCalculadora(calculadora_pb2_grpc.CalculadoraServicer):
    
    def Multiplicar(self, request, context):
        # request contiene 'a' y 'b', tal como lo definimos en el .proto
        resultado_calc = request.a * request.b
        
        # Devolvemos el mensaje Respuesta estructurado
        return calculadora_pb2.Respuesta(resultado=resultado_calc)

def iniciar_servidor():
    # Creamos un servidor gRPC con un pool de hilos
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # Registramos nuestro servicio en el servidor
    calculadora_pb2_grpc.add_CalculadoraServicer_to_server(ServicioCalculadora(), servidor)
    
    # Escuchamos en el puerto 50051 (el puerto por defecto de gRPC)
    servidor.add_insecure_port('[::]:50051')
    servidor.start()
    print("Servidor gRPC escuchando en el puerto 50051...")
    
    # Mantenemos el servidor corriendo
    servidor.wait_for_termination()

if __name__ == '__main__':
    iniciar_servidor()
