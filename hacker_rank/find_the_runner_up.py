'''
Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. 
You are given  scores. 
Store them in a list and find the score of the runner-up.
'''

n = int(input())
arr = map(int, input().split())

sorted_list = list(sorted(arr))

nodups = sorted([*set(sorted_list)])
print(nodups[-2])