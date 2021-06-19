"""
Problem:
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

leetcode discussion link: https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/1282605/python-or-88ms-or-Time%3A-O(n%2Bm)-and-Space-O(1)

Accepted | Runtime: 88 ms | Time: O(m+n) & Space O(1)
"""
 def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #edge case:
        if not nums1 and not nums2:
            return -1
        if not nums2 and len(nums1)==1:
            return nums1[0]
        if not nums1 and len(nums2)==1:
            return nums2[0]

        l_n1,l_n2 = len(nums1), len(nums2)
        ind_n1 , ind_n2 =  0, 0
        m1 ,m2 = -1,-1
        
        ## if one of len num is odd, the middle index is median (l_n1 + l_n2 )//2
        if ((l_n1 + l_n2 )%2 == 1):
            for count in range((l_n1 + l_n2 )//2+1): #2
                if (ind_n1!=l_n1 and ind_n2!=l_n2):
                    if nums1[ind_n1] > nums2[ind_n2]:
                        m1 = nums2[ind_n2] 
                        ind_n2+=1
                    else:
                        m1 = nums1[ind_n1] 
                        ind_n1+=1 #
                elif (ind_n1 <l_n1):
                    m1 = nums1[ind_n1]
                    ind_n1+=1
                else:
                    m1 = nums2[ind_n2]
                    ind_n2+=1
            return m1
        ## else the median is  will be average of elements 
        ## at index ((l_n1 + l_n2 )/2 - 1) and (l_n1 + l_n2 )/2
        else: 
            for count in range((l_n1 + l_n2 )//2+1): 
                m2 = m1 
                if (ind_n1!=l_n1 and ind_n2!=l_n2):
                    if nums1[ind_n1] > nums2[ind_n2]:
                        m1 = nums2[ind_n2] 
                        ind_n2+=1
                    else:
                        m1 = nums1[ind_n1] 
                        ind_n1+=1 #
                elif (ind_n1 <l_n1):
                    m1 = nums1[ind_n1]
                    ind_n1+=1
                else:
                    m1 = nums2[ind_n2]
                    ind_n2+=1

            return (m2+m1)/2
