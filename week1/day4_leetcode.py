
#leet code valid parenthesis:
def isValid(self, s: str) -> bool:
        
    mp = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }

    stack = []

    for ch in s:

        if ch in "({[":
            stack.append(ch)

        else:
            if not stack or stack.pop() != mp[ch]:
                return False

    return not stack

#leetcode daily temperatures

class Solution:
    def dailyTemperatures(self, temperatures):

        ans = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:

                prev = stack.pop()

                ans[prev] = i - prev

            stack.append(i)

        return ans