#17413
import sys
input = sys.stdin.readline

s=input().strip()+" "
st=[]
res=""
check=True
for i in s:
    if i=="<":
        check=False
        for _ in range(len(st)):
            res+=st.pop()
    st.append(i)
    if i==">":
        check=True
        for _ in range(len(st)):
            res+=st.pop(0)
    elif i==" "and check:
        st.pop()
        for _ in range(len(st)):
            res+=st.pop()
        res+=" "
print(res.strip())

