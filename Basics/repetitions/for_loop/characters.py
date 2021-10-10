print("What strange markings do you see?")
user_mark = input()
print("Identifying")
for count in range(0, len(user_mark),1):
    print(f"index {count}:", user_mark[count])
print("done")