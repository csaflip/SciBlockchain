from blockchain import Block, Transaction


# SAMPLE BLOCKCHAIN EXAMPLE

# Genesis block building
genesis_transaction = []
genesis_transaction.append(Transaction('sample.pdf'))
genesisBlock = Block(0, genesis_transaction, 1)

# Adding blocks with different transcations
second_transactions = []
second_transactions.append(Transaction('test.pdf'))
second_transactions.append(Transaction('docfile.docx'))
second = Block(genesisBlock.get_blockhash(), second_transactions, 1)

third_transactions = []
third_transactions.append(Transaction('R1.docx'))
third_transactions.append(Transaction('main.py'))
third = Block(second.get_blockhash(), third_transactions, 1)


print(genesisBlock.get_blockhash())
print(second.get_blockhash())
print(third.get_blockhash())



