class Solution:
    def reverse(self, x: int) -> int:
        rev=str(x)[::-1]
        if rev[-1]=='-':
          rev='-'+rev[:-1]
        if int(rev) > (2 ** 31 - 1) or int(rev) <(-2 ** 31) :
          return 0
        else:
          return int(rev)

a=1234
sol=Solution()
rev_a=sol.reverse(a)
print(f"input value {a}")
print(f"reversed value {rev_a}")


a=12344444444444444444444444447
sol=Solution()
rev_a=sol.reverse(a)
print(f"input value {a}")
print(f"reversed value {rev_a}")

a=-4567
sol=Solution()
rev_a=sol.reverse(a)
print(f"input value {a}")
print(f"reversed value {rev_a}")