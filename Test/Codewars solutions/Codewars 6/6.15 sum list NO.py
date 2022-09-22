# The Western Suburbs Croquet Club has two categories of membership,
# Senior and Open. They would like your help with an application form that
# will tell prospective members which category they will be placed.

# To be a senior, a member must be at least 55 years old and have a
# handicap greater than 7. In this croquet club, handicaps range from -2
# to +26; the better the player the lower the handicap.

# Input
# Input will consist of a list of pairs. Each pair contains information
# for a single potential member. Information consists of an integer for
# the person's age and an integer for the person's handicap.

# Output
# Output will consist of a list of string values (in Haskell and C: Open
# or Senior) stating whether the respective member is to be placed in the
# senior or open category.

# Example
# input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
# output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]

def open_or_senior(data):
    for index, i in enumerate(data):
        if sum(i) >= 62:
            data[index] = 'Senior'
            return data
        else:
            data[index] = 'Open'
            return data
# заменяет только первое значение.....


def openOrSenior(data):
    return ["Senior" if age >= 55 and handicap >=
            8 else "Open" for (age, handicap) in data]


def openOrSenior(data):
    res = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            res.append("Senior")
        else:
            res.append("Open")
    return res


def openOrSenior(data):
    def categorize(age, handicap):
        if age >= 55 and handicap > 7:
            return 'Senior'
        return 'Open'

    return [categorize(*item) for item in data]


def openOrSenior(data):
    # Hmmm.. Where to start?
    ret = []
    for datum in data:
        age, handicap = datum
        if age >= 55 and handicap > 7:
            ret.append('Senior')
        else:
            ret.append('Open')
    return ret


print(open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]))
