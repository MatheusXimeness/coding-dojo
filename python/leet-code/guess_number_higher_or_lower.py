class Solution(object):

    def __init__(self):
        self.pick = 6
        self.high = 10
        self.low = 1
    
    def guess_number(self, n):
        print(n)
        if n < self.pick:
            return 1
        elif n > self.pick:
            return -1
        return 0

guess = int(input("Guess the number: "))
solution = Solution()
target = False
while not target:
    aws = solution.guess_number(guess)
    if aws == 0:
        print("You find the number: ", guess)
        target = True
    elif aws == 1:
        guess = int(input("The number is lower than your last guess: "))
    else:
        guess = int(input("The number is higher than your last guess: "))