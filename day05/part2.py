fresh = []

def merge(fresh, pair):
    for i, (fs, fl) in enumerate(fresh):
        if (pair[0] - fl) * (pair[1] - fs) <= 0:
            fresh.pop(i)
            return merge(fresh, (min(pair[0], fs), max(pair[1], fl)))
    return pair[0], pair[1]

with open("input.txt", "r") as fp:
    for interval in fp.read().split("\n\n")[0].splitlines():
        fresh.append(merge(fresh, [int(val) for val in interval.split('-')]))

print(sum(l - s + 1 for s, l in fresh))