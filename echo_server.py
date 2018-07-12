import logging
import socket
import sys


FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger(__name__)


def server(log_buffer=sys.stderr):
    address = ('127.0.0.1', 10000)
    logging.info('creating server socket')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    logging.info(f'making a server on {address[0]}:{address[1]}')
    logging.info(f'binding socket to address: {address}')
    sock.bind(address)
    logging.info(f'listening on socket')
    sock.listen(1)

    try:
        while True:
            logging.info('waiting for a connection')
            conn, addr = sock.accept()

            try:
                logging.info(f'connection - {addr[0]}:{addr[1]}')

                while True:
                    buffer_size = 16
                    data = conn.recv(buffer_size)
                    logging.info(f"received {data.decode('utf8')}")
                    if data:
                        logging.info('sending data back to client')
                        conn.sendall(data)
                        logging.info(f"sent {data.decode('utf8')}")
                    else:
                        msg = f'No more data from {address[0]}:{address[1]}'
                        logging.info(msg)
                        break

            finally:
                logging.info('echo complete, client connection closed')
                conn.close()

    except KeyboardInterrupt:
        logging.info('quitting echo server')
        pass


if __name__ == '__main__':
    server()
    sys.exit(0)
