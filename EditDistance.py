class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #when min path comes up, brain goes to BFS
        #BFS needs a queue
        queue = collections.deque([(0,0,0)]) #i, j, number of operations
        while(queue):
            i, j, n = queue.popleft()
            #if words are equal, return n, base case: "" = ""
            if word1[i:] is word2[j:]:
                return n
            if len(word2[j:]) == 0:
                queue.append((i+1, j, n+1))#delete if word2 = "", word1 != ""
                continue
            if len(word1[i:]) == 0:
                queue.append((i, j+1, n+1))#insert if word1 = "", word2 != ""
                continue
            if(word1[i] is word2[j]):
                queue.appendleft((i+1,j+1, n))
            else:
                #Append all options
                queue.append((i+1, j+1, n+1))#replace
                queue.append((i, j+1, n+1))#insert
                queue.append((i+1, j, n+1))#delete
        return 0