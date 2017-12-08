## https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
## Given a n x n matrix where each of the rows and columns are sorted in ascending order, 
## find the kth smallest element in the matrix.
## Note that it is the kth smallest element in the sorted order, not the kth distinct element.
## Medium, 69ms, 70.66%

## This is not meant to be solved this way

class Solution(object):
    def kthSmallest(self, matrix, k):
        
        ## Simply create a new 1-dim list, sort, and return
        
        newlist = []
        for i in matrix:
            for j in i:
                newlist.append(j)
        newlist.sort()
        return newlist[k-1]
