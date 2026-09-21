"""
Problem    : 0026. Remove Duplicates from Sorted Array
Link       : https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Difficulty : Easy
Tags       : Array, Two Pointers
Runtime    : 0 ms (beats 100.0%)
Memory     : 22.5 MB (beats 80.32%)
"""

class Solution {
public:
    int removeDuplicates(vector<int>& arr) {
       int i = 0;
    for(int j = 1; j < arr.size(); j++) {
        if(arr[j] != arr[i]) {
            arr[++i] = arr[j];
        }
    }
    return i + 1;
 }
};
