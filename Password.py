import random
import array
maxlen=int(input('enter an number'))
a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
b=['1','2','3','4','5','6','7','8','9']
c=['@','#','$','%','^','&','*','!']
d=['A','B','C','D','E','F','G','H','I','J','K','L','M','N']

combined_list=a+b+c+d

rand_a = random.choice(a)
rand_b=random.choice(b)
rand_c=random.choice(c)
rand_d=random.choice(d)

password=rand_a+rand_b+rand_c+rand_d
for x in range(maxlen-4):
    password=password+random.choice(combined_list)
    temp_pass_list=array.array('u',password)
    random.shuffle(temp_pass_list)
    
password=""
for x in temp_pass_list:
    password=password+x
            
print(password)