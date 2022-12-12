import socket
import threading

class Echo(threading.Thread):
  def __init__(self, src_sock: socket.socket,
    dst_sock: socket.socket, buffer_size: int = None):
    threading.Thread.__init__(self)
    self.src_sock = src_sock
    self.dst_sock = dst_sock
    if buffer_size == None:
      self.buffer_size = 1024
    else:
      self.buffer_size = buffer_size

  def run(self):
    print(f'{threading.current_thread()}: enter')
    try:
      while True:

        if self.src_sock.fileno() == -1:
          print(f'{self.src_sock.getsockname()}: Closed')
          self.src_sock.close()
          print(f'{threading.current_thread()}: exit')
          return

        data = self.src_sock.recv(self.buffer_size)
        if not data:
          print(f'{self.src_sock.getsockname()}: Closed')
          self.src_sock.close()
          print(f'{threading.current_thread()}: exit')
          return

        print(f'''Received {len(data)} bytes from 
{self.src_sock.getsockname()}:''', data)
        # Set the response to echo back the received data
        response = data
        self.dst_sock.sendall(response)
    finally:
      self.src_sock.close()
      print(f'{threading.current_thread()}: exit')
