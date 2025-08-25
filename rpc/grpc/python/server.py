import grpc
from concurrent import futures
import calculator_pb2
import calculator_pb2_grpc


class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    """Implementación del servicio de calculadora"""
    
    def Add(self, request, context):
        """Función que suma dos enteros"""
        result = request.a + request.b
        print(f"Recibida petición: {request.a} + {request.b} = {result}")
        
        # Crear y retornar la respuesta
        response = calculator_pb2.AddResponse()
        response.result = result
        return response


def serve():
    """Función para iniciar el servidor gRPC"""
    # Crear el servidor con pool de hilos
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # Agregar el servicer al servidor
    calculator_pb2_grpc.add_CalculatorServicer_to_server(
        CalculatorServicer(), server
    )
    
    # Configurar el puerto
    listen_addr = '[::]:50051'
    server.add_insecure_port(listen_addr)
    
    # Iniciar el servidor
    server.start()
    print(f"Servidor iniciado en {listen_addr}")
    
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("\nDeteniendo el servidor...")
        server.stop(0)


if __name__ == '__main__':
    serve()

