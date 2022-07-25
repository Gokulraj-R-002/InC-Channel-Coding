class TreeNode(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


def huff(node, left = True, codeword = ''):
    if type(node) is str:
        return {node : codeword} # returns a dict {char: its cw}

    # else get its children and recurse
    (left, right) = node.children()

    d = {}
    d.update(huff(left, True, codeword + '0'))
    d.update(huff(right, False, codeword + '1'))

    return d


## main code starts here

in_file = open('file3.txt', 'r')

freq = {} # a dictionary to store {char : its count}

while 1:
    c = in_file.read(1)
    if not c:
        break

    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

in_file.close()


freq = sorted(freq.items(), key = lambda x : x[1]) # sort the dict based on count

arr = freq # copy the dictionary

while len(arr) > 1: # while there is atleast two elements
    arr = sorted(arr, key = lambda x: x[1])

    # pick the first two element (i.e., 2 min elements)
    (char1, count1) = arr[0]
    (char2, count2) = arr[1]

    # remove them from the arr
    arr = arr[2 : ]

    # make a new node whose left child is char1 and right child is char2
    new_node = TreeNode(char1, char2)

    # add the new node to the array
    arr.append((new_node, count1 + count2))


codewords = huff(arr[0][0]) # arr[0][0] will is same as the root of the tree
# codewords is a dictionary that contains {character : its codeword}

print('Char | Count | Huffman Code')
print('---------------------------')
for (character, frequency) in freq:
    print('%-4r |%6s |%13s' % (character, frequency, codewords[character]))


# Read the input file and for each character, write its codeword to the output file
# using the codewords dictionary
in_file = open('file3.txt', 'r')
out_file = open('encoded_file3.txt', 'w')

Code = '' # to store the final code

while 1:
    c = in_file.read(1)
    if not c:
        break

    Code += codewords[c] # add the cw corresponding to the character to the Code


out_file.writelines(Code)


in_file.close()
out_file.close()


# Decoding
in_file = open('encoded_file3.txt', 'r')
out_file = open('decoded_file3.txt', 'w')

received = '' # to store the bits we have received so far
decoded_data = '' # to store the character corresponding to the codeword received

charater_list = list(codewords.keys())
codeword_list = list(codewords.values())

while 1:
    bit = in_file.read(1)
    if not bit:
        break

    received += bit # keep track of the received bits

    # if the bits received so far is a codeword, add the corresponding character to the decoded_data and reset the received string
    if received in codeword_list:
        pos = codeword_list.index(received)
        decoded_data += charater_list[pos]
        received = ''

out_file.write(decoded_data)

in_file.close()
out_file.close()
