import binascii
import btle

class NeblinaDelegate(btle.DefaultDelegate):
	def __init__(self,params):
		self.Name = params
		btle.DefaultDelegate.__init__(self)

	def handleNotification(self, cHandle, data):
		print(cHandle)
		print(data)
		print(self.Name)

periph = btle.Peripheral("C3:C3:98:17:8E:D5","random")
print("Setup delegate")
periph.setDelegate( NeblinaDelegate('Neblina') )

Battery_Service_UUID = "0000180F-0000-1000-8000-00805f9b34fb"

try:
	print("Trying to get Descriptors")
	desc = periph.getDescriptors(1,7)
	for descriptor in desc:
		print(descriptor)
except btle.BTLEException as e:
	print("Exception =>",e)



def getBattery():
	try:
		print("Getting battery")
#		serv = periph.getServiceByUUID("6e400001-b5a3-f393-e0a9-e50e24dcca9e")
		serv = periph.getServiceByUUID(Battery_Service_UUID)
		while True:
			char = serv.getCharacteristics()
			print("%s," % binascii.hexlify(char[0].read())),
#			print(char[0].propertiesToString())
#i		print(char[1].propertiesToString())
#		while True:
#			if periph.waitForNotifications(1.0):
#				continue
#			print "Waiting..."
	except btle.BTLEException as e:
		print("Exception =>",e)
	finally:
		periph.disconnect()

getBattery()



