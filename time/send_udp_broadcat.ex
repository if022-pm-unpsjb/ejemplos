{:ok, socket} = :gen_udp.open(9999, broadcast: true)

:gen_udp.send(socket, {192,168,41,255}, 8888, "hola")
