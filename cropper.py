from modules.mitm import *
from getpass import getuser

crop = MITM()
i = 'enp2s0'
def main():
    user = getuser()
    if user == 'root':
        pass
    else:
        print(f"{R}Ejecuta el script con privilegios necesarios (root/Adminstrador)")
    
    while True:
        shell = input(f"{R}Cropper >> {W}")
        if shell == 'help':
            print("""
    server   : Iniciar servidor básico
    connect  : Conectarse a un host remoto (connect <ip> <port>)
    sniffer  : Realizar Ataque MITM sin envenamiento en la red
    read_cap : Leer contenido de archivos de red
""")
        elif "server" in shell:
            port = input(f"{O}Puerto {R}>>{W}")
            crop.server(port)
        elif "connect" in shell:
            ip = shell.split()[1]
            port = shell.split()[2]
            try:
                crop.connect(ip, port)
            except ConnectionRefusedError:
                print(f"{R} - {W}Conexión no posible")
        elif "sniffer" in shell:
            print(O+"#"*40)
            print(G+"Tipo de Protocolos:"+W)
            print("1. general")
            print("2. ftp")
            print("3. puerto especifico")
            protocol = input(f"{R}Tipo de Protocolo\n---> {W}")
            if protocol == '1':
                metodo = "general"
            elif protocol == '2':
                metodo = "ftp"
            else:
                metodo = 'port'
            crop.sniffer(metodo, i, None)
        elif "clear" in shell:
            sh("clear")
            






if __name__ == '__main__':
    try:
        main()

    except Exception as e:
        print(R+"ERR "+W+e)