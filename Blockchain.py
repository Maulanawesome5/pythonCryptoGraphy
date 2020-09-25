pip install flask requests

{
  'index': 35089,
  'transactions': [
    {
      'sender': 'some_people',
      'receiver': 'another_people',
      'amount': 3
    }
  ],
  'previous_hash': '83e74d5c6b0eded8c32bc90e8bcbd316798d7f9570dcb57e6f2a80cdb1b12198',
  'timestamp': 1524604177.5967348,
  'proof': 121231
}

# Membuat class untuk mendefinisikan Objek Blockchain
from time import time

class Blockchain:
  def __init__(self):
    self.chain = []
    self.current_transactions = []
    self.new_block(previous_hash=1, proof=100)

def new_block(self, proof, previous_hash=None):
  block = {
      'index': len(self.chain) + 1,
      'timestamp': time(),
      'transactions': self.current_transactions,
      'proof': proof,
      'previous_hash': previous_hash or self.hash(self.chain[-1]),
  }
  self.chain.append(block)
  self.current_transactions = []
  return block

# Membuat metode untuk menambahkan transaksi
  def new_transactions(self, sender, recipient, amount):
    self.current_transactions.append({
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    })
    return self.last_block['index'] + 1

    @property
    def last_block(self):
      return self.chain[-1]

# Proof of Work
from hashlib import sha256
x = 1 #proof
y = 0
while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
  y += 1
  
import hashlib

def proof_of_work(self, last_proof):
  proof = 0
  while self.valid_proof(last_proof, proof) is False:
    proof += 1
  return proof

@staticmethod
def valid_proof(last_proof, proof):
  guess = f'{last_proof}{proof}'.encode()
  guess_hash = hashlib.sha256(guess).hexdigest()
  return guess_hash[:4] == "0000"
