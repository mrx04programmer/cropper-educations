import os
import socket
from scapy.all import sniff
from scapy.all import *
from modules.colors import *
sh = os.system
s = socket.socket()
DataSend = 'Welcome to server :D'
class MITM():
    def server(self, port):
        s.bind(('', int(port)))
        s.listen(5)
        print(f"{B} [+] {W} Servidor creado en {port}")
        while True:
            # Accept all devices
            c, a = s.accept()
            print(f"{G} [+] {W} Dispositivo connectado desde : {a}")
            # Sending data in DataSend
            c.send(DataSend.encode())
            # Close connection
            c.close()
    def connect(self, rhost, rport):
        rport = int(rport)
        rhost = str(rhost)
        if rhost == '1.0.0.0' or rport == 0000:
            print(f" {R}[-] {W} RHOST & RPORT no encontrados")
        else:
            try:
                e = '\n'
                ent = e.encode()
                ''' hostname = socket.gethostbyname(rhost) '''
                print(f"{G}[INFO] {W} Conectado con {rhost}:{rport}")
                s.connect((rhost, rport))
                message = input(f"{R} --> {W}") 
                while message.lower().strip() != 'bye':
                    s.send(message.encode()+ent)
                    data = s.recv(1024).decode()
                    print('Datos recibidos:\n '+data)
                    message = input(f"{R} --> {W}") 
                s.close()
            except socket.gaierror:
                print(f"{R}[-] {W} Error , no se pudo conectar con el host.")
                exit()

            # Connect to server or host.
            s.connect((str(rhost), int(rport)))

    def sniffer(self, method, ifa, limit):
        iface = ifa
        if limit != None:
            limit = int(limit)
        if method == 'general':
            print(f"{O}[SET] {W} Interfaz -> {iface}")
            print(f"{O}[SET] {W} Limitación -> {limit}")
            print(f"{G}[INFO] {W}Escuchando trafico.. CTRL+C para terminar")
            ''' if iface:
                capture = sniff(iface=iface)
                print(f"{O}[SET] {W} Interfaz -> {iface}") '''
            if limit and iface:
                capture = sniff(iface=iface, count=limit)
            elif limit:
                capture = sniff(count=limit)
                ''' print(f"{O}[SET] {W} Limitación -> {limit}") '''
            else:
                capture = sniff()
            
            capture.summary()

        elif method == 'port':
            port = int(input(f"{W}Puerto : {O}"))
            print(f"{G}[INFO] {W} Escuchando en el puerto {port}...")
            #capture = sniff(filter='port %s' % (port))
            def r(packet):
                if packet[TCP].dport == port:
                    data = packet.sprintf()
                    print(data)
            capture = sniff(filter="port %s" % (port),iface=iface, prn=r)
            capture.summary()
        elif method == 'ftp':
            ftp_port = int(input(f"{G}Puerto de ftp (default: 21)>> {W}"))
            if ftp_port == '':
                ftp_port = 21
            print(f"{G}[INFO] {W} Escuchando protocolos de FTP ...")
            def r(packet):
                if packet[TCP].dport == ftp_port:
                    data = packet.sprintf("%Raw.load%") # Access to data of ftp traffic
                    if "USER" in data:
                        print(f"{G} Conexión desde {packet[IP].src} <--> {packet[IP].dst}")
                        data = data.split(" ")
                        data = data[1]
                        print(f"{W} Posible usuario {G}-> {P}{data}")
                    elif "PASS" in data:
                        data = data.split(" ")
                        data = data[1]
                        print(f"{W} Posible contraseña {G}-> {P}{data}")
            if iface:
                print(f"{O}[SET] {W} Interfaz -> {iface}")
                capture = sniff(filter="port %s" % (ftp_port),iface=iface, prn=r)
            else:
                capture = sniff(filter="port %s" % (ftp_port), prn=r)
            capture.summary()

        elif method == 'tcp':
            if iface:
                capture = sniff(filter='tcp', iface=iface)
                print(f"\n{O}[SET] {W} Interfaz -> {iface}")
            elif limit and iface:
                capture = sniff(filter='tcp', iface=iface, count=limit)
            elif limit:
                capture = sniff(filter='tcp', count=limit)
                print(f"{O}[SET] {W} Limitación -> {limit}")
            else:
                print(f"{G}[INFO] {W}Escuchando en el protocolo TCP...Ctrl+C para finalizar")
                capture = sniff(filter='tcp')
            capture.summary()
    def read_cap(self, file):
        file = str(file) # Example of file: captures.pcap
        print(f"{O}[READ] {W} Ruta de archivo -> {file}")
        print(f"{G}[INFO] {W} Mostrando contenido... \n{O}")
        read = sniff(offline=file) #prn=lambda x:x.summary()
