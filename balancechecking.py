class Solution:
    def isBalanced(self, parenthesis): 
            #type parenthesis: string
            #return type: boolean
            
            #TODO: Write code below to returnn a boolean value with the solution to the prompt.
            answer = None 
            leftPar = 0
            rightPar = 0
            leftCurly = 0
            rightCurly = 0
            leftBracket = 0
            rightBracket = 0 
            for i in range(len(parenthesis)):
                 if parenthesis[i] == "(":
                      leftPar = leftPar+1
                 elif parenthesis[i] == ")":
                      rightPar = rightPar + 1
                 elif parenthesis[i] == "}":
                      rightCurly = rightCurly + 1
                 elif parenthesis[i] == "{":
                     leftCurly = leftCurly + 1
                 elif parenthesis[i] == "[":
                      leftBracket = leftBracket+1
                 elif parenthesis[i] == "]":
                      rightBracket = rightBracket + 1
            if leftPar == rightPar and leftCurly == rightCurly and leftBracket == rightBracket:
                 answer = True 
            else:
                 answer = False
            return answer 
            pass

def main():
    str1=input()
    tc1= Solution()
    ans=tc1.isBalanced(str1)
    print(ans)

if __name__ == "__main__":
    main()