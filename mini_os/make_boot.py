code = bytes([
    0x31, 0xC0,              # xor ax, ax
    0x8E, 0xD8,              # mov ds, ax
    0x8E, 0xC0,              # mov es, ax

    
    0xB4, 0x02,              # mov ah, 0x02
    0xB0, 0x09,              # mov al, 9 sectors
    0xB5, 0x00,              # mov ch, 0
    0xB1, 0x02,              # mov cl, 2
    0xB6, 0x00,              # mov dh, 0
    0xBB, 0x00, 0x10,        # mov bx, 0x1000
    0xCD, 0x13,              # int 0x13

    # 0x1000にカーネル移動
    0xEA, 0x00, 0x10, 0x00, 0x00,  # jmp 0x0000:0x1000
])

boot = bytearray(512)
boot[0:len(code)] = code
boot[510] = 0x55
boot[511] = 0xAA

with open("boot.bin", "wb") as f:
    f.write(boot)

print("boot.bin created")
print("boot size:", len(boot))
