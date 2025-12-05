s=input("请输入字符串:")
freq={}
for char in s:
    freq[char] = freq.get(char, 0) + 1
sorted_chars = [char for char, _ in sorted(freq.items(), key=lambda x: x[1], reverse=True)]
print("按频率降序的字符:",",".join(sorted_chars))
