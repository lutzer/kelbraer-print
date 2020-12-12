from printer.Adafruit_Thermal import Adafruit_Thermal
from PIL import Image,ImageChops

img = Image.open("assets/lena.bmp")

printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)