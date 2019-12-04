import hashlib
import datetime
from typing import List


class Transaction:
    def __init__(self, filename: str):
        self.hash = ''
        self.filename = filename
        with open(filename, 'rb') as f:
            h1 = hashlib.sha256(f.read()).hexdigest()  # hashes contents of file
            self.hash = h1

    def get_hash(self):
        if self.hash == '':
            return self.filename
        else:
            return self.hash


class Block:
    def __init__(self, previous_hash, transactions: List[Transaction], version: int):
        self.previousHash = previous_hash
        self.transactions = transactions
        self.stamp = datetime.time()
        self.version = version

    def get_blockhash(self):
        tophash = ''
        for transaction in self.transactions:
            tophash += transaction.get_hash()
        blockhash = hashlib.sha256()
        blockhash.update(str(self.previousHash).encode())
        blockhash.update(tophash.encode())
        return blockhash.hexdigest()

    def get_transactions(self):
        return self.transactions

    def get_previous_block_hash(self):
        return self.previousHash

    def get_timestamp(self):
        return self.stamp

    def get_version(self):
        return self.version

