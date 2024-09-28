import socket

class TCP_Handler():
  def __init__(self):
    self.sock = socket.socket(socket.AF_INET)
  def connecting(self, ip, port):
    try:
      self.sock.connect(ip, port)
      return True
    except:
      return False
  def stopping(self):
    self.sock.close()
  def send_msg(self, command):
    self.sock.send(command)
    