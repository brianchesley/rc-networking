import socket

host = ''
port = 12345

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)
while True:
    client_sock, client_addr = s.accept()
    print(client_sock.getpeername())
    status = b'HTTP/1.0 200 OK\n'
    client_sock.recv(10000)
    client_sock.send(status)
    client_sock.send(b'Content-Type: text/html\n\n')
    html = b"""
    <HTML>
    <HEAD>
    <TITLE>Your Title Here</TITLE>
    </HEAD>
    <BODY BGCOLOR="FFFFFF">
    <CENTER>Hello!</CENTER>
    <HR>
    <a href="http://somegreatsite.com">Link Name</a>
    is a link to another nifty site
    <H1>This is a Header</H1>
    <H2>This is a Medium Header</H2>
    Send me mail at <a href="mailto:support@yourcompany.com">
    support@yourcompany.com</a>.
    <P> This is a new paragraph!
    <P> <B>This is a new paragraph!</B>
    <BR> <B><I>This is a new sentence without a paragraph break, in bold
    italics.</I></B>
    <HR>
    </BODY>
    </HTML>
     """
    client_sock.send(html)
    client_sock.close()

