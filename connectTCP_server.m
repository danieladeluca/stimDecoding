function tcp = connectTCP_server(IP, port)


fprintf(['Starting TCP/IP server on [Address: ' IP...
    ' - Port: %u]...'], port)

tcp = tcpserver(IP, port);

fprintf('Server Ready! waiting for connection from clients...\n')