SECTOR_SIZE = 512

with open("boot.bin", "rb") as f:
    boot = f.read()

with open("kernel.bin", "rb") as f:
    kernel = f.read()

kernel_sectors = (len(kernel) + SECTOR_SIZE - 1) // SECTOR_SIZE
kernel_padded_size = kernel_sectors * SECTOR_SIZE
kernel = kernel + bytes(kernel_padded_size - len(kernel))

with open("os-image.bin", "wb") as f:
    f.write(boot)
    f.write(kernel)

print("os-image.bin created")
print("boot size:", len(boot))
print("kernel size padded:", len(kernel))
print("kernel sectors:", kernel_sectors)
print("image size:", len(boot) + len(kernel))