from time import sleep
import datetime
for c in range(10,-1,-1):
    if c != 0:
        print(f'{c} 🧨')
        sleep(1)
    else:
        print(f'{c} 🥳')
print(f'Feeeliz {datetime.datetime.now().year} 🎆🎆🎆')