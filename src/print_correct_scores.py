def correct_scores(wrong_scores):
    return [int(str(score)[::-1]) for score in wrong_scores]


if __name__ == "__main__":
    raw_input = input("請輸入錯誤的分數(以空格分隔，例如：35 46 57 91 29):\n輸入: ")
    try:
        input_scores = list(map(int, raw_input.strip().split()))
        corrected = correct_scores(input_scores)
        print("修正後的分數為:", corrected)
    except ValueError:
        print("請輸入正確的數字格式，例如：35 46 57 91 29")
