#!/usr/bin/env python

import sys
import qrcode

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: <text-data>')
        sys.exit(1)

    data = sys.argv[1]
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    sys.stdout.flush()
    # Use sys.stdout.buffer if available (Python 3), avoiding
    # UnicodeDecodeErrors.
    stdout_buffer = getattr(sys.stdout, 'buffer', None)
    if not stdout_buffer:
        if sys.platform == 'win32':  # pragma: no cover
            import msvcrt
            msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)
        stdout_buffer = sys.stdout

    img.save(stdout_buffer)
