for i in range(0,1000):
    for x in range (0,4):
        hit = 0


results = []
for a in range(0,1000000):
    hit = 0
    wheel = list(range(0,10))
    for i in range (0,5):
        num = random.sample(wheel, 1)
        wheel.remove(num[0])
        if num[0] in (1,2,3):
            hit +=1
        else:
            continue
    results.append(hit)
collections.Counter(results)