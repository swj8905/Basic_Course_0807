# r 모드 : 읽기모드
   # - 만약 파일이 존재 하지 않으면, 에러를 뱉는다.
f = open("./test.txt", "r", encoding="utf-8")
# result = f.read()
# result = f.readline()
# result = f.readline()
result = f.readlines()
f.close()

print(result)