from databus import DataBus

class DataBusI2C(DataBus):
  hardware_data_bus = None

  def send(self,*remain):
    self.hardware_data_bus.writeto(remain[0],remain[1])
  
  def recv(self,*remain):
    return self.hardware_data_bus.readfrom(remain[0],remain[1])