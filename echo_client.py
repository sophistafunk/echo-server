import logging
import socket
import sys


FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger(__name__)


def client(msg, log_buffer=sys.stderr):
    server_address = ('localhost', 10000)
    logging.info('creating client socket')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
    logging.info(f'connecting to {server_address[0]} port {server_address[1]}')
    sock.connect(server_address)
    received_msg = ''

    try:
        logging.info(f'sending "{msg}" to the server')
        sock.sendall(msg.encode('utf-8'))
        while str(received_msg) != msg:
            received_msg += sock.recv(16).decode('utf8')
            logging.info(f'received "{received_msg}"')
    except Exception as e:
        logging.info(e)

    finally:
        logging.info('closing client socket')
        sock.close()
        return received_msg


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage = '\nusage: python echo_client.py "this is my message"\n'
        logging.info(usage)
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)
