{:ok, _} = :gen_udp.open(8888)

IO.puts("Esperando ...")

receive do
  _ -> IO.puts(DateTime.utc_now)
end
