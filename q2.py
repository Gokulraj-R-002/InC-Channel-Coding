import random
import matplotlib.pyplot as plt

# function to generate n-dimensional random binary vector
def gen_random_cw(n):
    cw = ''
    for i in range(n):
        cw += str(random.randint(0, 1))
    
    return cw
    


n_values = [15, 20]
k = 10
p_values = [0.015, 0.1, 0.45]
N = 1000

avg_errors_for_n15_k10 = []
avg_errors_for_n20_k10 = []

for n in n_values:
    for p in p_values:

        no_of_cw = pow(2, k) # number of codewords
        Code = [] # list to store the 2^k codewords

        while len(Code) < no_of_cw:
            random_cw = gen_random_cw(n) # generate a random code

            if random_cw in Code: # if the code has already been picked, do not add it one more time
                continue

            Code.append(random_cw) # else append the cw to the list


        E = 0 # E stores the total number of errors out of the N-times we use the channel


        for i in range(N):
            transmitted_cw = Code[random.randint(0, no_of_cw - 1)]

            y = '' # y stores the received vector

            for j in range(len(transmitted_cw)): # iterate through the bits in the transmitted cw
                do_flip = random.choices([0, 1], [1-p, p]) # do_flip is 1 with probability p, and 0 with probability 1-p
                # if do_flip is 1, flip the j-th bit
                # else do not flip the j-th bit
                if do_flip[0] == 1:
                    if transmitted_cw[j] == '0':
                        y += '1'
                    elif transmitted_cw[j] == '1':
                        y += '0'
                elif do_flip[0] == 0:
                    y += transmitted_cw[j]

            # y is the received vector

            min_dist = n + 1 
            # the maximum possible distance is n. 
            # So by declaring min_dist = n + 1, its value will definitely be changed to the min distance.
            
            estimated_cw = '' # to store the estimated codeword

            for j in range(no_of_cw): # iterate through all 2^k codewords
                dist = 0 # dist stores the hamming dist between y and Code[j]
                cw_beign_compared = Code[j]
                for itr in range(len(cw_beign_compared)):
                    if y[itr] != cw_beign_compared[itr]:
                        dist += 1
                
                # if dist is minimum, min_dist will be dist
                if dist < min_dist: 
                    min_dist = dist
                    estimated_cw = Code[j]

            I = 1 if transmitted_cw != estimated_cw else 0

            E += I

        avg_p_error = E / N # P_E (n,k,p,C)

        print('For n =', n, 'k =', k, 'p =', p, 'avg_error =', avg_p_error)