from correpy.parsers.brokerage_notes.b3_parser.b3_parser import B3Parser


class InterParser(B3Parser):
	last_transaction_item = ["Resumo dos negócios", "D/C"]

	def _is_transactions_last_line(self, line_text: str) -> bool:
		for transaction_item in self.last_transaction_item:
			transaction_line_item = line_text[: len(transaction_item)]
			if transaction_item == transaction_line_item:
				return True
		return False