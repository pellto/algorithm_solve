from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out = []
        for num in range(1, n + 1):
            o = ""
            if num % 3 == 0:
                o += "Fizz"
            if num % 5 == 0:
                o += "Buzz"
            if o == "":
                out.append(str(num))
            else:
                out.append(o)
        return out


if __name__ == "__main__":
    s = Solution()
    print(s.fizzBuzz(3))  # ["1", "2", "Fizz"]
    print(s.fizzBuzz(5))  # ["1", "2", "Fizz", "4", "Buzz"]
    print(
        s.fizzBuzz(15)
    )  # ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
