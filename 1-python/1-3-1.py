# Step 1: Solve the problem!
# ranlist = [8, 4, 7, 0, 4, 3, 2] 
# total = sum(ranlist) 28
# count = len(ranlist) 7
# mean = total / count 4.0
# print(mean)

# Step 2: Generalize the solution into a function
def average(numlist: list[float]) -> float: # here numlist is an argument 
    # the argument should (not enforced) be a list of floats and it will return a float
    total = sum(numlist)
    count = len(numlist)
    mean = total / count
    return mean

# Step 3: Test the function
# test with something you *know* the answer to
# sum is 28, count is 7, mean is 4.0
# numlist = [2, 3] # does not conflict with the function argument of the same name!
# ranlist = [8, 4, 7, 0, 4, 3, 2] # INPUT: this is a variable
# a = average(ranlist) # PROCESS: call the funtion (positional)
# a = average(numlist=ranlist) # PROCESS: call the funtion (named)
# print(a) # OUTPUT

def test_average():
    numbers = [1,1,1,1]
    expect = 1.0
    actual = average(numbers)
    assert expect == actual

test_average()
