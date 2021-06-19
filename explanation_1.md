# Explanation for each question 

###1) Problem 1: square root of an integer:
    I used a dictionary as my data structure to get and set values
    The Time complexity is  O(n) because I traversed the range of the list to get the square of the number
    The space complexity is 0(1) 
   

###2) Problem 2: Search in a Rotated Sorted Array:
    I am searching base on half of the record, after first getting the mid 
    I check if the mid is the pivot, then I search base on it 
    Since I am searching half the array Time Complexity is 0(log(n))
    The space complexity is 0(log(n))
   

###3) Problem 3: Rearrange Array Digit:
    I first sort the array with sort function which time complexity is O(log(n))
    Then I loop by odd and even looping by both half 
    Then I keep adding the number to the sum of even and sum of odd 
    The time complexity is 0(log(n)) because I didn't traverse through all the list 
    The space complexity is 0(log(n))


###4) Problem 4: Dutch National Flag:
    I used the Dutch National Flag algorithm 
    I have a low, high and middle variable where low is 0 and mid is 0 and high is length of array 
    The algorithm is that low will always be 0 and high should always be 2 in between we will have 1
    When I have a 0 at mid I swap mid and low element, and increment mid and low with 1
    When I have a 1 I just increment the mid 
    When I have a 2 I will reduce high by 1 
    Overall I am checking that mid is always less than high
    Since this is a single traversal 
    The time complexity  is  0(log(n)) 
    The space complexity is 0(1)
   

###5)Problem 5: Autocomplete with Tries:
    I am using a dictionary to keep each word and giving its child a class of TrieNode(which also have a dictionary for the next word)
    The loops continue till the word is completed and is_word will be true for the word
    1) find method 
        To find a word, I loop through the word given and traverse through the dictionary of each node child
        Since I am traversing through the list 
        the time complexity is 0(n)
        the space complexity is 0(1)
    2) suffixes method 
        To get all the suffix of a word, I get the prefix and use it to traverse the children of the word till is_word variable is true
        Since I am traversing through the list 
        the time complexity is 0(n)
        the space complexity is 0(n) because I  am saving all the words I get in a word_list variable 

###6) Problem 6 Max and Min in an Unsorted Array:
    I traverse through the list, and keep two variables max_num and min_num to keep the current max and min number
    The time complexity is 0(n)
    The space complexity is 0(n)
   

###7) Problem 7: HTTPRouter using a Trie:
    I am using trie data structure to keep the path supplied
    Each path has a node which has a dictionary called a children, this goes on till the end of the path is gotten and handler is True 
    
    1) add_handler method:
      split the path given by / which time complexity is O(n)
      then I loop though the list to add children to TrieNode 
      when the loop comes to and end I add the handler to the current Node which indicated the end of the path 
      The time complexity is 0(n)
      The space complexity is 0(1)
      
    2) lookup method:
      split the path given by / which time complexity is O(n)
      Then I traverse each child of the Node I come across, checking the next child is the same as the next element in my list 
      when I get to the last I get the handler and return it
      The space complexity is 0(1)
      
      
    
   
    

