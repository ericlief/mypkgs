import sys, re

def swap(s, i , j, n):
    if j >= n:
        return
    if s[i] > s[j]:
        temp = s[j]
        s[j] = s[i]
        s[i] = temp
    swap(s, i+1, j+1, n)

    
def swap_sort(s, passes):
    if passes == 0:
        return
    swap(s, 0,1,passes)
    swap_sort(s, passes-1)

def sort(s):
    n = len(s)
    if n <= 1:
        return
    swap_sort(s, n)
    
    
if __name__ == "__main__":
    for line in sys.stdin:
        line = line.rstrip()
        #print(line)
        chars = list(line)
        #print(chars)
        sort(chars)
        #print(chars)
        s = str(chars)
        s = s[1:-1]
        #print(s)
        s= re.sub("[,']", '', s)
        s= re.sub(" ", '', s)
        
        #print(s)
        lc = re.findall(r'[a-z]+', s)
        lc = str(lc)
        lc = lc[2:-2]
        uc = re.findall(r'[A-Z]+', s)
        uc = str(uc)
        uc = uc[2:-2]
        nums = re.findall('[0-9]+', s)
        nums = str(nums)
        nums = nums[2:-2]
        #print(nums)
        out = lc+uc+nums
        sys.stdout.write(out)
        #print(out)
    