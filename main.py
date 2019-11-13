from blockchain import Block

genesis_transaction = 'This is the first transaction'

genesisBlock = Block(0, genesis_transaction, 1)

print(genesisBlock.get_blockhash())

second = Block(genesisBlock.get_blockhash(), 'This is the second transaction', 1)

print(second.get_blockhash())

third = Block(second.get_blockhash(), 'This is my third message.', 1)

print(third.get_blockhash())

