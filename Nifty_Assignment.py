pairs = []
with open('input.txt') as file:
    lines = [line.strip() for line in file if line.strip()]
i=0
while i < len(lines):
    line= lines[i]
    i=i+1
    if i<len(lines) and lines[i].replace(' ','').isdigit():
        numbers=list(map(int,lines[i].split()))
        i=i+1
        
        top3=sorted(numbers,reverse=True)[:len(numbers)]
        avg=sum(top3)/3
    else:
        avg=0
    pairs.append((line, avg))

for pair in pairs:
    print(f"{pair[0]}: {pair[1]:.2f}")
