from Bitso import Bitso
import time

bitso = Bitso()

if __name__ == "__main__":
	while True:
		book_info = bitso.get_book_info("btc_usdt")
		print(f"You have selected: {book_info['book']} => The current price is: {book_info['last']}")
		time.sleep(10)
