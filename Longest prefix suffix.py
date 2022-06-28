def longest(s) :
    n = len(s)
    
    for res in range(n // 2, 0, -1) :

        prefix = s[0: res]
        suffix = s[n - res: n]
        
        if (prefix == suffix) :
            return res

    return 0
    
if __name__ == "__main__":
    s = "abab"
    print(longest(s))