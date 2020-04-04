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



