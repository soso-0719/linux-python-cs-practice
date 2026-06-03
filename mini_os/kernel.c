void _start(void) {
    volatile char *video = (volatile char *)0xb8000;

    video[160] = 'S';
    video[161] = 0x07;
    video[162] = 'O';
    video[163] = 0x07;

    while (1) {
    }
}
