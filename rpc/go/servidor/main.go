package main

import (
	"log"
	"net"
	"net/rpc"
	
	"ejemplo-rpc/calculadora" // Importamos nuestro paquete compartido
)

// ServicioCalculadora contiene la implementación real
type ServicioCalculadora int

// Multiplicar recibe los argumentos definidos en el paquete compartido
func (s *ServicioCalculadora) Multiplicar(args *calculadora.Argumentos, respuesta *int) error {
	*respuesta = args.A * args.B
	return nil
}

func main() {
	servicio := new(ServicioCalculadora)

	// Registramos el servicio explícitamente con el nombre "Calculadora"
	rpc.RegisterName("Calculadora", servicio)

	listener, err := net.Listen("tcp", ":1234")
	if err != nil {
		log.Fatal("Error al iniciar servidor:", err)
	}

	log.Println("Servidor RPC escuchando en el puerto 1234...")
	rpc.Accept(listener)
}
