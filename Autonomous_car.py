import heapq
class Solution(object):
    def Autonomous_car(self, target):
        K = target.bit_length() + 1
        barrier = 1 << K
        pq = [(0, target)]
        dist = [float('inf')] * (2 * barrier + 1)
        dist[target] = 0
        while pq:
            move, targ = heapq.heappop(pq)
            if dist[targ] > move: continue

            for k in range(K+1):
                walk = (1 << k) - 1
                move2, targ2 = move + k + 1, walk - targ
                if walk == targ: move2 -= 1 
                if abs(targ2) <= barrier and move2 < dist[targ2]:
                    heapq.heappush(pq, (move2, targ2))
                    dist[targ2] = move2
        return dist[0]
val=Solution()
target=int(input())
print(val.Autonomous_car(target))
