// =============================================================================
// SERVIDOR RPC
// =============================================================================

package main

import (
	"fmt"
	"log"
	"net"
	"net/http"
	"net/rpc"
)

// Estructura que define nuestro servicio RPC
type Calculator struct{}

// Argumentos para las operaciones matemáticas
type Args struct {
	A, B int
}

// Respuesta de las operaciones
type Result struct {
	Value int
}

// Método para sumar dos números
func (c *Calculator) Add(args *Args, reply *Result) error {
	reply.Value = args.A + args.B
	fmt.Printf("Suma: %d + %d = %d\n", args.A, args.B, reply.Value)
	return nil
}

// Método para restar dos números
func (c *Calculator) Subtract(args *Args, reply *Result) error {
	reply.Value = args.A - args.B
	fmt.Printf("Resta: %d - %d = %d\n", args.A, args.B, reply.Value)
	return nil
}

// Método para multiplicar dos números
func (c *Calculator) Multiply(args *Args, reply *Result) error {
	reply.Value = args.A * args.B
	fmt.Printf("Multiplicación: %d * %d = %d\n", args.A, args.B, reply.Value)
	return nil
}

// Método para dividir dos números
func (c *Calculator) Divide(args *Args, reply *Result) error {
	if args.B == 0 {
		return fmt.Errorf("división por cero no permitida")
	}
	reply.Value = args.A / args.B
	fmt.Printf("División: %d / %d = %d\n", args.A, args.B, reply.Value)
	return nil
}

func main() {
	// Crear una instancia del servicio Calculator
	calculator := new(Calculator)
	
	// Registrar el servicio RPC
	err := rpc.Register(calculator)
	if err != nil {
		log.Fatal("Error registrando el servicio:", err)
	}
	
	// Registrar el handler HTTP para RPC
	rpc.HandleHTTP()
	
	// Crear un listener en el puerto 1234
	listener, err := net.Listen("tcp", ":1234")
	if err != nil {
		log.Fatal("Error creando listener:", err)
	}
	
	fmt.Println("Servidor RPC iniciado en puerto 1234")
	fmt.Println("Esperando conexiones...")
	
	// Servir las conexiones HTTP
	log.Fatal(http.Serve(listener, nil))
}
