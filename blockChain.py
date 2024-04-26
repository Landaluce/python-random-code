import hashlib
import json
from time import time
from typing import List, Dict, Any


class Blockchain:
    def __init__(self):
        self.chain: List[Dict[str, Any]] = []
        self.current_transactions: List[Dict[str, Any]] = []

        # Create the genesis block
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof: int, previous_hash: str = None) -> Dict[str, Any]:
        """
        Create a new Block in the Blockchain.

        Args:
            proof (int): The proof given by the Proof of Work algorithm.
            previous_hash (str): Hash of the previous Block.

        Returns:
            dict: New Block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender: str, recipient: str, amount: int) -> int:
        """
        Create a new transaction to go into the next mined Block.

        Args:
            sender (str): Address of the Sender.
            recipient (str): Address of the Recipient.
            amount (int): Amount.

        Returns:
            int: The index of the Block that will hold this transaction.
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block: Dict[str, Any]) -> str:
        """
        Create a SHA-256 hash of a Block.

        Args:
            block (dict): Block.

        Returns:
            str: Hash string.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self) -> Dict[str, Any]:
        return self.chain[-1]

    def proof_of_work(self, last_proof: int) -> int:
        """
        Simple Proof of Work Algorithm:
        - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'.
        - p is the previous proof, and p' is the new proof.

        Args:
            last_proof (int): Previous Proof.

        Returns:
            int: New Proof.
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof: int, proof: int) -> bool:
        """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?

        Args:
            last_proof (int): Previous Proof.
            proof (int): Current Proof.

        Returns:
            bool: True if correct, False if not.
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"


def main():
    # Example usage:
    blockchain = Blockchain()
    blockchain.new_transaction('Alice', 'Bob', 1)
    blockchain.new_transaction('Bob', 'Charlie', 2)

    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    blockchain.new_block(proof)

    print("Blockchain:", blockchain.chain)


if __name__ == "__main__":
    main()
