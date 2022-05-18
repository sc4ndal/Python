inStr = "  한글 Python 프로그래밍  "
outStr = ""
print('['+inStr.strip()+']') #양옆 공백 제거
print(inStr.replace(' ','')) #공백을 아무것도 안 넣음으로 바꿔서 공백 제거

for i in range(0, len(inStr)):
    if inStr[i] != ' ':
        outStr += inStr[i]
    else: outStr += '/'

print("원래 문자열 =>"+'['+inStr+']')
print("공백 삭제 문자열 =>"+'['+outStr+']')