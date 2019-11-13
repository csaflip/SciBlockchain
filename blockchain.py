import hashlib


class Block:
    def __init__(self, previous_hash, transactions: str):
        self.previousHash = previous_hash
        self.transactions = transactions

    def get_blockhash(self):
        blockhash = hashlib.sha256()
        blockhash.update(str(self.previousHash).encode())
        blockhash.update(self.transactions.encode())
        return blockhash.hexdigest()

    def get_transactions(self):
        return self.transactions

    def get_previous_block_hash(self):
        return self.previousHash
