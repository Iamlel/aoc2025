with open("input.txt", "r") as fp:
    intervals, ingredients = fp.read().split("\n\n")
    intervals = [[int(val) for val in line.split('-')] for line in intervals.splitlines()]
    
print(sum(any(int(i) >= s and int(i) <= l for s, l in intervals) for i in ingredients.splitlines()))