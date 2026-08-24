package main

import (
	"fmt"
	"log"

	"ejemplo-rpc/calculadora" // Importamos nuestro paquete compartido
)

func main() {
	// Usamos el wrapper para conectar
	cliente, err := calculadora.Dial("tcp", "localhost:1234")
	if err != nil {
		log.Fatal("Error al conectar:", err)
	}
	// Nos aseguramos de cerrar la conexión al terminar
	defer cliente.Close()

	// Invocamos la función tipada
	resultado, err := cliente.Multiplicar(7, 6)
	if err != nil {
		log.Fatal("Error en la operación:", err)
	}

	fmt.Printf("El resultado de la operación es: %d\n", resultado)
}
