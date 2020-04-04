import socket

#prepare the fill-ins based on user input
server = input('Enter the name of website url (Ex: "www.kennesaw.edu"): ')
path = ""
output_name = input('Enter name for output file: ')

#standard http port number
port = 80

#create the HTTP method for connecting to the website
initial_line = "GET " + path + " HTTP/1.1 \n"
header_line = "Host: " + server + "\n"

#create socket
client_socket = socket.socket()

#connect socket to web server and retrieve results
client_socket.connect((server, port))

client_socket.sendall(initial_line.encode())
client_socket.sendall(header_line.encode())
client_socket.sendall("\n".encode())

client_socket.shutdown(1)

response = ""
bytes = client_socket.recv(2048)
while len(bytes) > 0:
    response += bytes.decode()
    bytes = client_socket.recv(2048)

print(response)

client_socket.close()

