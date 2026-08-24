package calculadora

import "net/rpc"

// Argumentos: Estructura compartida para enviar los datos
type Argumentos struct {
	A, B int
}

// ClienteCalculadora: Nuestro Type-Safe Wrapper para el cliente
type ClienteCalculadora struct {
	*rpc.Client
}

// Dial encapsula la conexión y devuelve nuestro cliente tipado
func Dial(network, address string) (*ClienteCalculadora, error) {
	cliente, err := rpc.Dial(network, address)
	if err != nil {
		return nil, err
	}
	return &ClienteCalculadora{cliente}, nil
}

// Multiplicar oculta la llamada RPC y los strings "mágicos"
func (c *ClienteCalculadora) Multiplicar(a, b int) (int, error) {
	args := Argumentos{A: a, B: b}
	var respuesta int
	
	err := c.Call("Calculadora.Multiplicar", args, &respuesta)
	return respuesta, err
}
