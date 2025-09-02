#docker container run --rm -v $(pwd):/app -w /app --user $(id -u):$(id -g) --network host elixir:alpine elixir $1
docker container run -p 8888:8888/udp -p 9999:9999/udp --rm -v $(pwd):/app -w /app --user $(id -u):$(id -g) elixir:alpine elixir $1
