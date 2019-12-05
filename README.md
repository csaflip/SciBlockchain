# SciBlockchain
Blockchain concept for storing scientific papers.

Thist blockchain applications primarily consists of two objects, Blocks and Transactions.

Transaction:
To create a new transaction, simply provide the string of the filename with its extension. Note: the file has to be in the same directory as the python file.
The hash of the file is created by reading the file and hashing its data contents.

get_hash() can be used to retrieve the hash of the transaction.

Example. ex_transaction = Transaction('mytestfile.pdf')
ex_transaction.get_hash()


Blocks:
Recieves previous hash of a block, list of transaction objects, and a version number.
When a block is created, a timestamp is also generated. It can be accessed with get_timestamp()

The block version number is currently 1.
The list of transactions passed in is used to calculate the block's hash.
Each transactions hash is concatenated together, along with the hash of the previous block into one string.
This string is then hashed with SHA256 to generate the block's unique hash.

All of the other getter functions are explanatory in the blockchain.py file.

The code in main.py is used to show an example of a chain of blocks being created, along with some sample transactions.


To run this code, simple download the files, put them in a folder with some files you would like to add to the blockchain. Then, when 
creating transactions, just use the names of the files that you put in the same directory that you would like to hash.
