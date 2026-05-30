code = bytes([
    0xBE, 0x10, 0x7C,  # mov si, 0x7c10

    0x8A, 0x04,        # mov al, [si]
    0x3C, 0x00,        # cmp al, 0　０で終わりにするため。
    0x74, 0x07,        # je done

    0xB4, 0x0E,        # mov ah, 0x0e
    0xCD, 0x10,        # int 0x10

    0x46,              # inc si  siの参照、アドレスに+１する。
    0xEB, 0xF3,        # jmp loop　上に戻って繰り返し、　

    0xEB, 0xFE,        # done: infinite loop
])

message = b"Soichiro OS Booted!\0"
##biosなら0x7c00（配列の最初の要素のメモリアドレス） + 0x0010に置かれるらしい。

boot = bytearray(512)
boot[0:len(code)] = code
boot[0x10:0x10 + len(message)] = message
boot[510] = 0x55
boot[511] = 0xAA

with open("boot.bin", "wb") as f:
    f.write(boot)

print("boot.bin created")
