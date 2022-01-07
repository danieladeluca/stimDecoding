function tcp = connectTCP_server(IP, port)


fprintf(['Starting TCP/IP server on [Address: ' IP...
    ' - Port: %u]...'], port)

tcp = tcpip(IP, port,'NetworkRole', 'server');

fprintf('Server Ready!\nWaiting for connection from clients...\n')