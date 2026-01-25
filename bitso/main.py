from Bitso import Bitso
	
if __name__ == "__main__":
	bitso = Bitso()
	book_info = bitso.get_book_info("btc_usdt")
	
	print(f"You have selected: {book_info['book']} the current price is: {book_info['last']}")
