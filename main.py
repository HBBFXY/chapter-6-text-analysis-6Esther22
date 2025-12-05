def analyze_text(text):
    char_freq = {}
    for char in text:
        char_freq[char] = char_freq.get(char, 0) + 1
    sorted_chars = sorted(char_freq.keys(), key=lambda x: char_freq[x], reverse=True)
    return sorted_chars
if __name__ == "__main__":
    print("文本字符频率分析器")
    print("====================")
    print("请输入一段文本（输入空行结束）：")
    lines = []
    while True:
        try:
            line = input()
            if line == "":
                break
            lines.append(line)
        except EOFError:
            break
    text = "\n".join(lines)   
    if not text.strip():
        print("未输入有效文本！")
    else:
        sorted_chars = analyze_text(text)
        print("\n字符频率降序排列:")
        print(", ".join(sorted_chars))
        print("\n提示: 尝试输入中英文文章片段，比较不同语言之间字符频率的差别")
