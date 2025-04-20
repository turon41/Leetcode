class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0]*n

        moves,balls = 0,0

        for i in range(n):
            res[i] = moves+balls
            moves+=balls
            balls+=int(boxes[i])
            #print(res,moves,balls)
        balls,moves = 0,0    
        for i in reversed(range(n)):
            res[i]+=(moves+balls)
            moves+=balls
            balls+=int(boxes[i])
            #print(res,moves,balls) 
        return res    
          

                 
        