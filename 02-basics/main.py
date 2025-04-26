a = 123
b = "안녕하세요."
print("a값:{} b값:{}".format(a, b))
print(f"a값:{a} b값:{b}")

a = input("첫 번째 문자열 입력:")
b = input("두 번째 문자열 입력:")
print(a+b)

a_tuple = (1, 2, 3, 4, 5)
a_tuple[0] = 5
print(a_tuple)

a_set = set([1, 2, 3, 4])
print(a_set)

b_set = set([1, 1, 2, 2, 3, 3, 4, 5, 6])
print(b_set)

c_set = set("python40s")
print(c_set)

name_list = ["홍길동", "장다인", "김철수"]
age_list = [500, 5, 12]
for i, k in enumerate(name_list):
    print("i=", i, end=' ')
    print("k=", k)

for i, k in enumerate(name_list):
    print(k, end=' ')
    print(age_list[i])
for i, k in enumerate(name_list):
    print(name_list[i], end=' ')
    print(age_list[i])
for i in range(len(name_list)):
    print(name_list[i], end=' ')
    print(age_list[i])

test_list = [i for i in range(10)]
print(test_list)

try:
    dsdkfjdjfkdjfk
except Exception as e:
    print("에러 발생 원인", e)


class Greet():
    def hello(self):
        print("hello")

    def hi(self):
        print("hi")


human1 = Greet()
human2 = Greet()
human1.hello()
human1.hi()
human2.hello()
human2.hi()


class Student():
    def __init__(self, name, age, like):
        self.name = name
        self.age = age
        self.like = like

    def studentInfo(self):
        print(f"이름:{self.name}, 나이:{self.age}, 좋아하는것:{self.like}")


김철수 = Student("김철수", 17, "축구")
장다인 = Student("장다인", 5, "헬로카봇")
김철수.studentInfo()
장다인.studentInfo()


class Mother():
    def __init__(self):
        print("키가 크다.")
        print("공부를 잘한다.")


class Daughter(Mother):
    def __init__(self):
        super().__init__()
        print("운동을 잘한다.")


print("엄마는")
엄마 = Mother()
print("딸은")
딸 = Daughter()
