'''

    Design Pattern 7: Structure Patterns - Adapter.

'''

class UsbCable:
    
    def __init__(self):
        self.isPlugged = False

    def plugUsb(self):
        self.isPlugged = True

class MicroUsbCable:
    
    def __init__(self):
        self.isPlugged = False

    def plugMicroUsb(self):
        self.isPlugged = True

class MicroToUsbAdapter(UsbCable):
    def __init__(self, microUsbCable):
        self.microUsbCable = microUsbCable
        self.microUsbCable.plugMicroUsb()


class UsbPort:

    def __init__(self):
        self.portAvailable = True
    
    def plug(self, usb):
        if self.portAvailable:
            usb.plugUsb()
            self.portAvailable = False
        else:
            print(f'The port is not available!')

if __name__ == '__main__':
    usbCable = UsbCable()
    usbPort1 = UsbPort()
    usbPort1.plug(usbCable)

    microToUsbAdapter = MicroToUsbAdapter(MicroUsbCable())
    usbPort2 = UsbPort()
    usbPort2.plug(microToUsbAdapter)