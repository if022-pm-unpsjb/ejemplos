import grpc

# Importamos los archivos generados automáticamente
import calculadora_pb2
import calculadora_pb2_grpc

def ejecutar():
    # Nos conectamos al servidor en el puerto 50051
    with grpc.insecure_channel('localhost:50051') as canal:
        
        # El Stub nos da autocompletado y seguridad de tipos
        stub = calculadora_pb2_grpc.CalculadoraStub(canal)
        
        # Preparamos el mensaje con los argumentos
        args = calculadora_pb2.Argumentos(a=7, b=6)
        
        # Llamamos al método como si fuera una función local
        respuesta = stub.Multiplicar(args)
        
        print(f"El resultado es: {respuesta.resultado}")

if __name__ == '__main__':
    ejecutar()
