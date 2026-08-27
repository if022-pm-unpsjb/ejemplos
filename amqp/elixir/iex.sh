docker run -e CLOUDAMQP_URL -it --rm -v "$(pwd)":/app -w /app -u $(id -u):$(id -g) --network host -e MIX_HOME=/app/mix_home -e HEX_HOME=/app/hex_home elixir:otp-27-alpine iex -S mix
