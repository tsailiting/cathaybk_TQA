from collections import Counter


def count_characters(text):
    # 將文字轉為大寫，並只保留英文字母與數字
    filtered = [char.upper() for char in text if char.isalnum()]
    counter = Counter(filtered)

    # 排序輸出：先數字0-9，再A-Z
    for ch in sorted(counter.keys(), key=lambda x: (x.isalpha(), x)):
        print(f"{ch} {counter[ch]}")


if __name__ == "__main__":
    message = "Hello welcome to Cathay 60th year anniversary"
    count_characters(message)
