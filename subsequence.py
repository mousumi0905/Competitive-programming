#Given two strings s and t,
#  return true if s is a subsequence of t, or false otherwise.

def isSubsequence(s, t):
        n,m = len(s),len(t)
        i,j = 0,0
        while (i < n and j < m):
            if (s[i] == t[j]):
                 i += 1
            j += 1
        return i == n

isSubsequence("abc", "ahbgdc")
     
          
            