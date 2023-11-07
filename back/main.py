from http.server import HTTPServer
from services.request import Requests

import sys

def main():
    server_address = ('127.0.0.1', 8000)
    try:
        server = HTTPServer(server_address, Requests)
        print(f"Servidor rodando em {server_address[0]}:{server_address[1]}")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Servidor interrompido pelo usuário.")
    except Exception as e:
        print(f"Erro inesperado: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()
