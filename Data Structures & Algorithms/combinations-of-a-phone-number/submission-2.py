class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        digit_dict = {
            "2" : ['a', 'b', 'c'],
            "3" : ['d', 'e', 'f'],
            "4" : ['g', 'h', 'i'],
            "5" : ['j', 'k', 'l'],
            "6" : ['m', 'n', 'o'],
            "7" : ['p', 'q', 'r', 's'], 
            "8" : ['t', 'u', 'v'],
            "9" : ['w', 'x', 'y', 'z'],
        }

        res = []

        if len(digits) == 0: 
            return res
        

        def backtracking(path, digit_index):

            # base case, if we hit he last digit, return 
            if digit_index == len(digits): 
                res.append("".join(path))
                return 

            
            curr_digit = digits[digit_index]

            for char in digit_dict[curr_digit]:

                path.append(char)
                backtracking(path, digit_index + 1)
                path.pop()

        
        backtracking([], 0)

        return res
