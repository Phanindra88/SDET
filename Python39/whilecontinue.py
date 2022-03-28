print("using else with while and continue:")
i=0
while i<5:
    i-i+1
    if i==3:
        continue
    print(i,end="  ")
else:
    print("\n inside else block")
    print("\n")
