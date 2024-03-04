class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = [substr for substr in s.split() if s.strip()]
        if len(s_list) == 1:
            return "".join(s_list)
        end = len(s_list) - 1
        for i in range(len(s_list)):
            if end <= i:
                break
            temp_char = s_list[i]
            s_list[i] = s_list[end]
            s_list[end] = temp_char
            end -= 1
        return " ".join(s_list)