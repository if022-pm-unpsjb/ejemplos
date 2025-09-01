{:ok, socket} = :gen_udp.open(9999)

:gen_udp.send(socket, {192,168,1,8}, 8888, "hola")
