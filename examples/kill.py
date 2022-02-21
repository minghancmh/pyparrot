from pyparrot.Bebop import Bebop
import math

bebop = Bebop()
bebop.emergency_land()

print("DONE - disconnecting")
bebop.disconnect()