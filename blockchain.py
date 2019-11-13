import hashlib


class Block:
    def __init__(self, previous_hash: float, transactions):
        self.previousHash = previous_hash
        self.transactions = transactions


    def get_blockhash(self):
        trans_str = str(self.transactions)
        blockhash = hashlib.sha256(trans_str.encode()).hexdigest()
        return blockhash



    def get_transactions(self):
        return self.transactions

    def get_previous_block_hash(self):
        return self.previousHash
