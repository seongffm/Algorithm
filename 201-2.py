#10799
import sys
input = sys.stdin.readline

s=input().strip()
st=[]
cnt=0
for i in range(len(s)):
    if s[i]=="(":
        st.append("(")
    else:
        st.pop()
        if s[i-1]=="(":
            cnt+=len(st)
        else:
            cnt+=1
print(cnt)

