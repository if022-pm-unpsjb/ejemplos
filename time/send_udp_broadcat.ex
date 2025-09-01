{:ok, socket} = :gen_udp.open(9990, broadcast: true)

:gen_udp.send(socket, {192,168,1,255}, 8888, "hola")
