import serial.tools.list_ports
import serial

class RS232C:
  def __init__(self) :
    pass

  def setRS232Parameters(self):
    self.seri

  def getCOMPort(self):
    return [ports.device + " " + ports.description for ports in serial.tools.list_ports.comports()]
    ''' 
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        yield p.device
      '''
  def startCOM(self, comport):
    try:
      # self.seri.setDTR(False)
      self.seri = serial.Serial(comport,9600) #, dsrdtr=True)
      self.seri.timeout=0.05
      self.seri.set_buffer_size = 25
      return True
    except:
      return False

  def stopCOM(self):
    try:
      if (self.seri.isOpen) :
          self.seri.close()
    except:
      pass 

  def sendCommand(self, command):
    self.seri.write(command)

  def readPolling(self):
    if self.seri.open :
      re = self.seri.readlines()
      # re = self.seri.readlines()
    else:
      re = ""
    return re
