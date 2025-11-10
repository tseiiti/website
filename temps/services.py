from spyne import Application, rpc, ServiceBase, Unicode, Integer
from spyne.protocol.soap import Soap11

class MySoapService(ServiceBase):
  @rpc(Unicode, Integer, _returns=Unicode)
  def say_hello(ctx, name, times):
    return u' '.join([u'Hello, %s' % name] * times)
  
  @rpc(Integer, Integer, _returns=Integer)
  def add_numbers(ctx, num1, num2):
    return num1 + num2

soap_app = Application([MySoapService],
                        tns='my.soap.example',
                        in_protocol=Soap11(validator='lxml'),
                        out_protocol=Soap11())