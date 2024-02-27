from ftplib import FTP
from config import ftp_user, ftp_host, ftp_password

host = ftp_host
user = ftp_user
password = ftp_password

with FTP(host) as ftp:
    ftp.login(user=user, passwd=password)
    print(ftp.getwelcome())

    # Download file from server
    server_file_path = "/home/gauri/Desktop/sockets-tcp-networking/python-tutorials/ftp-client/ftp_server/server_test.txt"
    local_file_path = "client_text.txt"
    with open(local_file_path, 'wb') as file:
        ftp.retrbinary("RETR " + server_file_path, file.write, 1024)

    # Upload file to server
    local_file_path = "local_text.txt"
    server_file_path = "/home/gauri/Desktop/sockets-tcp-networking/python-tutorials/ftp-client/ftp_server/upload_test.txt"
    with open(local_file_path, 'rb') as file:
        ftp.storbinary('STOR ' + server_file_path, file)

    ftp.quit()
