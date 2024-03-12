'''

Charan is working on the boundary of his House. His boundary is made of N-bamboos, all across the house.
As Charan is a trader, he has colored his boundary in 2 colors Green and Red, which represent Bull and Beer respectively.
This year he is very bullish on the stock market, so he decided to color all the bamboo in green color. Currently, some are green and some are red. The current configuration is represented as a string S, where each index is represented as a color bamboo.

As the number of bamboo is more, he wants to make this task an interesting one. So he decided to play a game.

Below are the rules of the game:
• Consider an integer K Select a particular index say I, and target the next K bamboos.
• If the bamboo is colored Green, make it RED, and if it is Red, make it Green. doing this until all the turns Green.

You have to find the no. of minutes in which Charan can turn all the bamboo to be green. Considering each operation takes 1 minute to complete.

Example:

Let us try to understand it with an example. Consider there are N = 7 bamboos and the Integer K = 3 And the initial colors are represented as B =[RGGRGRG]

Input String: RGGRGRG

Minute 1: Let us start from index 0, taking 3 at a time (as K = 3 ) We will convert index 0-2 to vice versa

Original:
RGGRGRG

Changed:
GRRRGRG

Minute 2 :Consider index=1, taking 3 at a time (as K = 3 ), We will convert index 1-3 to vice versa

Original:
GRRRGRG

Changed:
GGGGGRG

Minute 3: As we have 'G' till index 4. We will consider the next index= 5 taking 3 at a time (as K = 3 ), We will convert 5-6 to vice versa

Original:
GGGGGRG

Changed:
GGGGGGR

Minute 4: As we have 'G' till index 5, we will take next index as 6, taking 3 at a time (as K = 3 )

Original:
GGGGGGR

Changed:
GGGGGGG

'''


def stringTransfer(s, k):
    # Convert the input string to a list
    string_list = list(s)
    length = len(string_list)
    minutes = 0
    i = 0

    while i < length:
        # Move through consecutive 'G's
        while i < length and string_list[i] == 'G':
            i += 1

        # Define the start and end of the window
        start_window = i
        end_window = min(i + k, length)

        # Check if the current position is 'R', increment minutes if so
        if i < length and string_list[i] == 'R':
            minutes += 1

        # Flip the characters within the window
        while start_window < length and start_window < end_window:
            if string_list[start_window] == 'G':
                string_list[start_window] = 'R'
            else:
                string_list[start_window] = 'G'

            start_window += 1

    return minutes


k = int(input("Enter Size Of Window: "))  # Convert input to integer
s = input("Enter String With 'R' & 'G' Value: ")

print(stringTransfer(s, k))
