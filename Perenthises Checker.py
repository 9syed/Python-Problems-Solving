def ispar(self,s):
    
    stack = [] 
    for char in s:
        if char in ['{','[','('] : 
            stack.append(char) 
        
        else:       
            
            if len(stack) == 0: 
                return False

            if char == '}':
                if stack[-1] == '{':
                    stack.pop()
                    continue
            if char == ')':
                if stack[-1] == '(':
                    stack.pop()
                    continue
            if char == ']':
                if stack[-1] == '[':
                    stack.pop()
                    continue
            return False  
    
    if len(stack): 
        return False
    return True