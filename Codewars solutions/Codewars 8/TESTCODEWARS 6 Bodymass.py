#Write function bmi that calculates body mass index (bmi = weight / height2).
#if bmi <= 18.5 return "Underweight"
#if bmi <= 25.0 return "Normal"
#if bmi <= 30.0 return "Overweight"
#if bmi > 30 return "Obese"

def bmi(weight, height):
    z = weight/(height**2)
    if z <= 18.5: 
        return "Underweight"
    elif z <= 25.0: 
        return "Normal"
    elif z <= 30.0:
        return "Overweight"
    else:
        return "Obese"
print(bmi(50, 1.5))

print((lambda w, h: "Underweight" if w/(h**2) <= 18.5 else "Normal" if w/(h**2) <= 25.0 else "Overweight" if w/(h**2) <= 30 else "Obese" )(90, 1.8))

bmi = lambda w,h: (lambda b=w/h**2: ["Underweight", "Normal", "Overweight", "Obese"][(18.5<b) + (25<b) + (30<b)])()
bmi=lambda w,h:next(s for s,t in zip("Obese Overweight Normal Underweight".split(),(30,25,18.5,0))if w/h/h>t)
def bmi(weight, height):
    ratio = weight / height ** 2
    
    if ratio > 18.5:
        if ratio > 25:
            if ratio > 30:
                return 'Obese'
            return 'Overweight'
        return 'Normal'
    return 'Underweight'