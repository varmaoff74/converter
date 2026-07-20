from converter.device.detector import DeviceDetector


device = DeviceDetector().detect()

print(device.to_dict())