def find_last_person(n):
    if n <= 0 or n > 100:
        return "請輸入 1 ~ 100 的數字"

    people = list(range(1, n + 1))
    index = 0

    while len(people) > 1:
        # 找到第3個人：從目前位置往後移動兩位（因為報數是1, 2, 3）
        index = (index + 2) % len(people)
        eliminated = people.pop(index)  # 踢出
        print(f"踢出:{eliminated}, 剩下{people}")

    return f"最後留下的是第 {people[0]} 順位"


if __name__ == "__main__":
    try:
        n = int(input("請輸入人數 (1~100):"))
        print(find_last_person(n))
    except ValueError:
        print("請輸入有效的整數")
