function tcp = connectTCP_server(IP, port, bufferSize)


fprintf(['Starting TCP/IP server on [Address: ' IP...
    ' - Port: %u]...'], port)
try
    tcp = tcpip(IP, port, 'NetworkRole', 'server');
    fprintf(' started.\n')
catch me
    fprintf(' failed.  Aborting the experiment \n')
end
set(tcp, 'InputBufferSize', bufferSize);
fprintf('Server Ready! waiting for connection to Psychopy client...')