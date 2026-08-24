# Ejemplo gRPC con Python

Este ejemplo usa gRPC con Python. El proyecto fue generado mediante [uv](https://docs.astral.sh/uv/) y el ejemplo mediante Gemini.

A continuación, se describen los pasos, por si se desea replicar:

## Creación del proyecto
Con uv instalado, ejecutar: 
```
$ uv init python-rpc
$ cd python-rpc
$ uv add grpcio grpcio-tools
```

Esto genera un directorio con el nombre del proyecto y luego instala las dependencias necesarias.

Luego, para generar el código necesario a partir del archivo `.proto`, ejecutar:
```
$ uv run python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculadora.proto
```

## Para ejecutar
En una terminal, ejecutar `uv run servidor.py` y en otra `uv run cliente.py`.
