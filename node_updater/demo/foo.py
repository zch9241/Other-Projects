format_time = '6.22'
text = '6/6.20/6.20cl'
s = text.split('/')[-1].replace('.', '')
f = format_time.replace('.', '')
print(f not in s)