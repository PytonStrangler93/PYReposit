#Our football team finished the championship. The result of each match look like "x:y". Results of all matches are recorded in the collection.
#For example: ["3:1", "2:2", "0:1", ...]
#Write a function that takes such collection and counts the points of our team in the championship. Rules for counting points for each match:
#if x > y: 3 points
#if x < y: 0 point
#if x = y: 1 point
#Notes:
#there are 10 matches in the championship
#0 <= x <= 4
#0 <= y <= 4


def points(games):
    count = 0
    for score in games:
        res = score.split(':')
        if res[0]>res[1]:
            count += 3
        elif res[0] == res[1]:
            count += 1
    return count

def points(a):
    return sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in a))	

def points(games):
    result = 0
    for item in games:
        result += 3 if item[0] > item[2] else 0     
        result += 1 if item[0] == item[2] else 0
    return result

def points(games):
    return sum([0,1,3][1+(g[0]>g[2])-(g[0]<g[2])] for g in games)

def points(games):
    return sum(3 if x > y else 0 if x < y else 1 for x, y in (score.split(":") for score in games))

def points(games): 
    total = 0
    a = len(games) 
    for i in range(0,a): 
            a = games[i].split(':') 
            if a[0] > a[1]: 
                total = total + 3 
            if a[0] == a[1]: 
                total = total + 1 
            if a[0] < a[1]: 
                total = total + 0 
    return total

def points(games):
    points = 0
    for game in games:
        x = int(game[0])
        y = int(game[2])
        if x>y:
            points += 3
        elif x==y:
            points += 1
    return points

points = lambda g: sum((x>y)*3 or x==y for x,_,y in g)
