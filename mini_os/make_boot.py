code = bytes([
    0xB4, 0x0E,        # mov ah, 0x0e

    0xB0, ord("H"),   # mov al, 'H'
    0xCD, 0x10,       # int 0x10

    0xB0, ord("i"),   # mov al, 'i'
    0xCD, 0x10,       # int 0x10

    0xB0, ord("!"),   # mov al, '!'
    0xCD, 0x10,       # int 0x10

    0xEB, 0xFE,       # infinite loop
])

boot = bytearray(512)

boot[0:len(code)] = code

boot[510] = 0x55
boot[511] = 0xAA

with open("boot.bin", "wb") as f:
    f.write(boot)

print("boot.bin created")
