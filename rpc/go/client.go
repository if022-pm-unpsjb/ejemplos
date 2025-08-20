// =============================================================================
// CLIENTE RPC (Ejecutar en un archivo separado)
// =============================================================================

// client.go
package main

import (
	"fmt"
	"log"
	"net/rpc"
)

// Mismas estructuras que en el servidor
type Args struct {
	A, B int
}

type Result struct {
	Value int
}

func main() {
	// Conectar al servidor RPC
	client, err := rpc.DialHTTP("tcp", "localhost:1234")
	if err != nil {
		log.Fatal("Error conectando al servidor:", err)
	}
	defer client.Close()
	
	fmt.Println("Conectado al servidor RPC")
	
	// Argumentos para las operaciones
	args := &Args{A: 10, B: 5}
	
	// Realizar suma
	var sumResult Result
	err = client.Call("Calculator.Add", args, &sumResult)
	if err != nil {
		log.Printf("Error en suma: %v", err)
	} else {
		fmt.Printf("Suma: %d + %d = %d\n", args.A, args.B, sumResult.Value)
	}
	
	// Realizar resta
	var subResult Result
	err = client.Call("Calculator.Subtract", args, &subResult)
	if err != nil {
		log.Printf("Error en resta: %v", err)
	} else {
		fmt.Printf("Resta: %d - %d = %d\n", args.A, args.B, subResult.Value)
	}
	
	// Realizar multiplicación
	var mulResult Result
	err = client.Call("Calculator.Multiply", args, &mulResult)
	if err != nil {
		log.Printf("Error en multiplicación: %v", err)
	} else {
		fmt.Printf("Multiplicación: %d * %d = %d\n", args.A, args.B, mulResult.Value)
	}
	
	// Realizar división
	var divResult Result
	err = client.Call("Calculator.Divide", args, &divResult)
	if err != nil {
		log.Printf("Error en división: %v", err)
	} else {
		fmt.Printf("División: %d / %d = %d\n", args.A, args.B, divResult.Value)
	}
	
	// Probar división por cero
	args.B = 0
	var divZeroResult Result
	err = client.Call("Calculator.Divide", args, &divZeroResult)
	if err != nil {
		fmt.Printf("Error esperado en división por cero: %v\n", err)
	}
}
