import hashlib
import time

# the upper bound of all potential nonces
MAX_NONCE = 2**32


# perform PoW in a iteration manner
def proof_of_work(header, difficulty_bits):
    # calculate the difficulty target from difficulty bits
    target = 2**(256 - difficulty_bits)

    # perform the iteration, until finding a nonce which satisfies the target
    for nonce in range(MAX_NONCE):
        hash_res = hashlib.sha256(
            (str(header) + str(nonce)).encode('utf-8')).hexdigest()
      
        if int(hash_res, 16) < target: # difficult requirement
            print(f'success with nonce {nonce}\n')
            print(f'hash in hex is:\t\t {hash_res}')
            return nonce
          
    # target cannot be satisfied even all nonces are traversed
    print(f'failed after {MAX_NONCE} tries\n')
    return MAX_NONCE


def main():

    difficulty_bits = 10
    print(f'difficulty:\t\t {2**difficulty_bits} ({difficulty_bits} bits)\n')
    print('starting search ...')

    start_time = time.time()
    block_header = 'We are PolyU, Together We Excel!'
    nonce = proof_of_work(block_header, difficulty_bits)
    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f'elapsed time:\t {elapsed_time:.4f} seconds')
    print(f'hashrate:\t\t {float(int(nonce) / elapsed_time):.4f} hash/s')


if __name__ == '__main__':
    
    main()
