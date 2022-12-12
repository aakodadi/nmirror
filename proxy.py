from echo import Echo
import socket
import threading

class Proxy(threading.Thread):
  def __init__(self, host: str, port: int,
      target_host: str, target_port: int,
      max_clients: int = None, timeout: float = None,
      buffer_size: int = None):
    threading.Thread.__init__(self, daemon = True)
    self.host = host
    self.port = port
    self.sock = socket.socket(socket.AF_INET,
      socket.SOCK_STREAM)
    self.sock.bind((self.host, self.port))
    self.target_host = target_host
    self.target_port = target_port
    if max_clients == None:
      self.max_clients = 5
    else:
      self.max_clients = max_clients
    if timeout == None:
      self.timeout = 60
    else:
      self.timeout = timeout
    if buffer_size == None:
      self.buffer_size = 1024
    else:
      self.buffer_size = buffer_size


  def run(self):
    print(f'{threading.current_thread()}: enter')
    self.sock.listen(self.max_clients)
    print('Listening on:', (self.host, self.port))
    while True:
      client_sock, client_address = self.sock.accept()
      print('Client:', client_sock.getsockname())
      client_sock.settimeout(self.timeout)
      target_sock = socket.socket(socket.AF_INET,
        socket.SOCK_STREAM)
      target_sock.settimeout(self.timeout)
      target_sock.connect((self.target_host,
        self.target_port))
      client_to_target_echo = Echo(
        src_sock = client_sock, dst_sock = target_sock,
        buffer_size = self.buffer_size)
      target_to_client_echo = Echo(
        src_sock = target_sock, dst_sock = client_sock,
        buffer_size = self.buffer_size)
      client_to_target_echo.start()
      target_to_client_echo.start()
    print(f'{threading.current_thread()}: exit')