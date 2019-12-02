for i in range(256):
    b = bytes([i])
    print(b,int.from_bytes(b, byteorder='little', signed=True))
