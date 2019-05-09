def spam():
    for i in range(1, 21):
        if i % 5 == 0 and i % 3 == 0:
            print("SpamEgg")
        elif i % 5 == 0:
            print("Egg")
        elif i % 3 == 0:
            print("Spam")
        else:
            print(i)

def memory_efficient_spam():
    spammed = ['1','2','Spam','4','Egg','Spam','7','8','Spam','Egg','11','Spam','13','14','SpamEgg','16','17','Spam','19','Egg']
    for v in spammed:
        print(v)

if __name__ == "__main__":
    spam()
    # memory_efficient_spam()