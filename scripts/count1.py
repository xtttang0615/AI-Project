Text = 'TACGCATTACAAAGCACA'
Pattern = 'AA'

count = 0
for i in range(len(Text) - len(Pattern) + 1):   # 逐位滑窗
    if Text[i:i+len(Pattern)] == Pattern:
        count += 1
print('Count1 =', count)