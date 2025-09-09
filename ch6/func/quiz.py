def calc(**kwarge):
    for key in kwarge:
        print(key)


calc(apple = 1200, banana=800, orange=1500)


dic = {'철수':90, '영희':85,'민수':100}

def show_scores(**kwargs):
    for value in kwargs.values():
        print(value)

show_scores(철수=90,영희=85,민수=100)


dic = {'seoul':950, 'busan':340,'incheon':300 }
def show_population(**kwargs):
    for people in kwargs.items():
        print(people)

show_population(seoul=950, busan=340,incheon=300)



