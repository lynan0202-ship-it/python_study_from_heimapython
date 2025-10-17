count=0

for i in range(2,101):
    for j in range(2,i//2+1):
        if i%j==0:
            break
    else:
        print(f'{i}是质数',end=' ')
        count += 1
        if count % 3==0:
            print('\t')


