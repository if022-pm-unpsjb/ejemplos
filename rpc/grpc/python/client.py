import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    """Función principal del cliente"""
    # Crear conexión con el servidor
    with grpc.insecure_channel('localhost:50051') as channel:
        # Crear el stub (cliente)
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        
        # Probar varias sumas
        test_cases = [
            (5, 3),
            (10, 20),
            (-5, 15),
            (0, 0),
            (100, 200)
        ]
        
        print("Cliente gRPC - Calculadora")
        print("=" * 30)
        
        for a, b in test_cases:
            try:
                # Crear la petición
                request = calculator_pb2.AddRequest(a=a, b=b)
                
                # Hacer la llamada RPC
                response = stub.Add(request)
                
                # Mostrar el resultado
                print(f"{a} + {b} = {response.result}")
                
            except grpc.RpcError as e:
                print(f"Error en la llamada RPC: {e}")
        
        print("\n¡Pruebas completadas!")


if __name__ == '__main__':
    run()

