'''

The program will recieve 3 English words inputs from STDIN

These three words will be read one at a time, in three separate line
The first word should be changed like all vowels should be replaced by *
The second word should be changed like all consonants should be replaced by @
The third word should be changed like all char should be converted to upper case
Then concatenate the three words and print them

Case 1
Input:
how
are
you

Expected Output : h*wa@eYOU

Case 2
Input:
how
999
you

Expected Output : h*w999YOU

'''

def transform(w1, w2, w3):
    vowels = ["a", "e", "i", "o", "u"]

    word1=w1.replace(" ","")
    word2=w2.replace(" ","")
    word3=w3.replace(" ","")
    
    # convert string word1 and word2 into list word1_list and word2_list
    word1_list = list(word1)
    word2_list = list(word2)

    # finding vowels in word1 and convert it to "%"
    for i in range(0, len(word1_list)):
        for j in range(0, len(vowels)):
            if word1_list[i] == vowels[j]:
                word1_list[i] = "%"

    # finding consonent in word2 and convert it to "#"
    for i in range(0, len(word2_list)):

        if word2_list[i] not in vowels:
            word2_list[i] = "#"

    # convert word3 into lower order
    word3_lower = word3.lower()

    # convert word1_list into the string
    new_w1 = ""
    for x in word1_list:
        new_w1 += x

    # convert word2_list into the string
    new_w2 = ""
    for x in word2_list:
        new_w2 += x

    return new_w1 + new_w2 + word3_lower


word1 = input("Enter First Word: ")
word2 = input("Enter Second Word: ")
word3 = input("Enter Third Word: ")
word = transform(word1, word2, word3)
print(word)
