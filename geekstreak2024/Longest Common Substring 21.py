#User function Template for python3
class Solution:
    def longestCommonSubstr(self, str1, str2):
        # Get the lengths of both strings
        len1, len2 = len(str1), len(str2)
        
        # Create a 2D list to store lengths of longest common suffixes of substrings
        # dp[i][j] will be the length of the longest common substring ending at str1[i-1] and str2[j-1]
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        
        # Initialize the result variable to store the maximum length
        max_length = 0
        
        # Fill the dp array
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_length = max(max_length, dp[i][j])
                else:
                    dp[i][j] = 0
        
        # Return the length of the longest common substring
        return max_length