from Bitso import Bitso

bitso = Bitso()

if __name__ == "__main__":
	book_info = bitso.get_book_info("btc_usdt")
	print(f"You have selected: {book_info['book']} the current price is: {book_info['last']}")
