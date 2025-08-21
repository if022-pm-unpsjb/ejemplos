# Erpc

RPC en Elixir.

Ejecutar en una terminal:
```
$ iex --sname nodo1@localhost -S mix
```

En otra terminal:
```
$ iex --sname nodo2@localhost -S mix
```

Luego, en la primer terminal:
```
iex> :erpc.call(:nodo2@localhost, Erpc, :hello, ["fran"]) 
Hello fran
:ok
iex>
```

Con `spawn`:
```
iex> Node.spawn(:nodo2@localhost, Erpc, :hello, ["Fran"])
#PID<18359.157.0>
Hello Fran             
iex> 
```

