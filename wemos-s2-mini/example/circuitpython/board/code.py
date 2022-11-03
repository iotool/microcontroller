import board
import microcontroller

print("board")
for pin in dir(microcontroller.pin):
	if isinstance(getattr(microcontroller.pin, pin), microcontroller.Pin):
		print("".join(("microcontroller.pin.", pin, "\t")), end=" ")
		for alias in dir(board):
			if getattr(board, alias) is getattr(microcontroller.pin, pin):
				print("".join(("", "board.", alias)), end=" ")
	print()
