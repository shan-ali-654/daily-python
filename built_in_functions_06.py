# 1. One sentence: what is a function, and what's the main reason we use them?
# Function is a block of Code that we use to make code lines lower and reuse some lines again when we are get needed those . this act as a  block of code that we can reuse by just calling function name instead of writing from blank . 

# ----------------
# 2. Python functions into two types. Name both, and give a one-line difference.
# Built_in Fuctions : Those fucntions which is already provided by python to use them like max , sorted, range etc some other as well . 
# User _ Defined _ Functions : Those functions which is totally defined by user . To make its code functionality more better and perfect . 

# ------------------

# 3.  What does type() tell you about a variable? What does id() tell you? Keep them separate.
# type() tells us about type of our data. 
# id() Tells us where our data will stored in our system memory the exact location it tolds. 

# ---------------------
# 4. You have words = ["Python", "Programming", "Code", "Functions"] and you want the longest word. You reach for max(words). Does plain max(words) give you the longest word? Answer yes/no and explain what max() actually does with a list of strings.
# No it will not give, instead of that it returnn word thta si alphabaticaly bigger . not by length 
# ---------------------
# 5. sorted() goes ascending by default. You need highest-to-lowest. Name at least one way to get descending order.
# We using a reverse = True as a second element with variable name in function so this way we got printed it 
# as i shown 
# num = range(2, 8)
# print(sorted(num , reverse=True))


# ---------------------
# 6. input() — what type does it always hand back to you, no matter what the user types? So if you write age = input("age: ") and then age + 5, what happens and why?
# It always Return Strings. It return Type Error. Because we are entering a string with input() but with  add on + method we adds integers, so integer plus string is not a add into each other it shows type error . 

# --------------------------
# 7. eval("5 + 3 * 2") returns 11, not 16. Walk me through why it's 11. Then give me one concrete reason you'd never run eval() on text that came from a stranger.
# It returns 11 because it first done multiplication then addition so by this way it got 11 , eval has one issue it use enterd value as pyhthon and runs it even if it is deleting our code or file this type some things so 

