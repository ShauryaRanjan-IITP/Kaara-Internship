nums =input #as leetcode has its own input
target = input
nmax = 10000
hash = [0]* nmax
for i in nums : 
    hash[target - i] = 1

for a,j  in enumerate(nums) :
    if hash[j] == 1 :
        break
index_1 = a
for b,k in enumerate(nums) :
    if k == target - j and a != b:
        break
index_2 = b

if index_1 > index_2 :
    index_1,index_2 = index_2,index_1

out = [index_1,index_2]
print (out)