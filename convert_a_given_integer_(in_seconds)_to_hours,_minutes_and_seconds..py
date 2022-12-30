seconds=int(input())
hours=seconds//3600
rem_sec=seconds%3600
min=rem_sec//60
rem_sec=rem_sec%60
print("H:M:S-{}:{}:{}".format(hours,min,rem_sec))

