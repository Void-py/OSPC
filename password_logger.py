import pickle
import socket


passwd = "wireshark"

with open("log_file.bin","ab") as f:
    usr_inp = input("Enter the password : ")
    if(usr_inp!=passwd):
        ip_addr = socket.gethostbyname(socket.gethostname())
        pickle.dump(ip_addr,f);
