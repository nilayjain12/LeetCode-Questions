class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i in range(0, len(s)):
            if s[i] == '*':
                stack.pop()
            else:
                stack.append(s[i])
        new_s = "".join(stack)

        return new_s