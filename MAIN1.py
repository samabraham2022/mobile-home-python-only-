import time
from datetime import datetime
import webbrowser
import sys
import pygame
import sqlite3
from datetime import date
from matplotlib import pyplot as plt
import random as ran
pygame.mixer.init()
for i in range(13):
    print('')
    
def main():
    
    print()
    print()
    print()
    print('                                                          ______     _______ ')
    print('                                                         I           I    I              ')
    print('                                                         I           I    I              ')
    print('                                                         I______I    I______  ')
    print('                                                         I  \                          I   ')
    print('                                                         I      \                      I     ')
    print('                                                         I          \     _______I        ')
    
    print('1.google')
    print('2.clock')
    print('3.musicplayer')
    print('4.notepad')
    print('5.cricket game')
    print('6.python bank')
    print('7.info')
    print('8.reset')
    print('9.contacts')
    print('10.calculator')
    print('11.settings')
    print('12.pickmyshow')
    print('13.currency convertor')
    try:
        k12=input('enter the option')
        con1(k12)
        k12=int(k12)
        print()
        if k12==1:
            google()
        if k12==2:
            clock()
        if k12==3:
            musicplayer()
        if k12==4:
            notepad()
        if k12==5:
            cricket()
        if k12==6:
            bank()
        if k12==7:
            userinfo()
        if k12==8:
            reset()
        if k12==9:
            contacts()
        if k12==10:
            calc()
        if k12==11:
            settings()
        if k12==12:
            pick_my_show()
        if k12==13:
            cash_conv()
                
        else:
            main()
    except:
    
       print('something went wrong')
       main()
    
def info():
        a=input('enter your name')
        b=input('enter you phno')
        c=input('enter your email id')
        d=input('enter your blood group')
        e=input('enter your emergency contact')
        f=['name-,'+a+'\n','phno-'+b+'\n','email-'+c+'\n','blood_grp-'+d+'\n','emergency_contact-'+e+'\n']
        h=open('myprofile.txt','w')
        h.writelines(f)
        h.close()
def intro():
    
    print('                                                          ______     _______ ')
    time.sleep(0.5)
    print('                                                         I           I    I  ')
    time.sleep(0.5)
    print('                                                         I           I    I ')
    time.sleep(0.5)
    print('                                                         I______I    I______  ')
    time.sleep(0.5)
    print('                                                         I  \                          I   ')
    time.sleep(0.5)
    print('                                                         I      \                      I     ')
    time.sleep(0.5)
    print('                                                         I          \     _______I        ')
    for i in 'TAKING OVER':
        time.sleep(0.7)
        print(i,end='-')
    time.sleep(10)
    print()
    d=open('myprofile.txt','r')
    if d.read()=='':
        info()
    d.close()
    lock_check()
def encrypt(b):
    b=str(b)
    a=''
    for i in b:
        a+=''
        if i==0:
            a+='1hy:#'
        if i=='1':
            a+='jky@#'
        if i=='2':
            a+='ght*#'
        if i=='3':
            a+='s@23#'
        if i=='4':
            a+='f$%!#'
        if i=='5':
            a+=':_+7#'
        if i=='6':
            a+='t:@:#'
        if i=='7':
            a+='h":£#'
        if i=='8':
            a+=':mu%#'
        if i=='9':
            a+='r^:;#'
    return a
def decrypt(x):
    b=x.split('#')
    a=''
    for i in b:
        if i=='1hy:':
            a+='0'
        if i=='jky@':
            a+='1'
        if i=='ght*':
            a+='2'
        if i=='s@23':
            a+='3'
        if i=='f$%!':
            a+='4'
        if i==':_+7':
            a+='5'
        if i=='t:@:':
            a+='6'
        if i=='h":£':
            a+='7'
        if i==':mu%':
            a+='8'
        if i=='r^:;':
            a+='9'
    return int(a)

def cricket():
    pygame.mixer.music.load('cricket.mp3')
    pygame.mixer.music.play()
    ans='y'
    while ans in ['y','yes']:
        

        
        
        

       

        print("                  ________ CRICKET  _________")
        
        
        
        

        

        

        print("1 wicket match")
        print("5 wicket match")
        print("10 wicket match")
        
            
        bb=input("choose number of wickets:")
        conm(bb)
        if bb=='1':
            user=0
            computer=1
            newuser=0
            target=25
            print("you need 26 runs to win the game")
            while user!=computer:
                try:
                    user=input("enter a number between 1 and 6:")
                    conm(user)
                    user=abs(int(user))
                    if user>6 or user<0:
                        print('DOT BALL')
                        user-=user

                    else:
                        pass
                    
                    computer=ran.randint(1,6)
                    print("computer has put",computer)
                    newuser+=user
            
                    if user==computer:
                        if newuser-user>target:
                            break
                        else:
                            break
                    else:
                        if newuser-user>target:
                            print(newuser-user)
                            break

                except:
                    print("something went wrong")            
                
           
            if newuser-user==0:
                    print("DUCKOUT")
            else:
                pass
            
            if newuser-user>target:
                    print("you have scored:")
                    print(newuser-user,"runs")
                    print("YOU WIN")
                    break
            elif newuser-user<target:
                    print("you are out for:")
                    print(newuser-user,"runs")
                    print("YOU LOSE.")
            else:
              print("you are tied with the computer.BETTER LUCK NEXT TIME")
        if bb=='5':
            user1=0
            computer1=1
            newuser1=0
            target1=100
            count=0
            while user1!=computer1 or count<5:
                try:
                    user1=input("enter a number between 1 and 6:")
                    conm(user1)
                    user1=abs(int(user1))
                    if user1>6 or user1<0:
                        print('DOT BALL')
                        user1-=user1

                    else:
                        pass
                    
                    computer1=ran.randint(1,6)
                    print("computer has put",computer1)
                    newuser1+=user1
                
                    if user1==computer1:
                        count+=1
                        print("NEW BATSMEN")
                        print("                     ")
                        newuser1=newuser1-user1
                        if newuser1>target1:
                            break
                        else:
                            pass
                    else:
                        if newuser1>target1:
                            break
                
                except:
                    print("something went wrong")
            
            if newuser1>target1:
              print("you have scored:")
              print(newuser1,"runs")
              print("YOU WIN")
              break
            elif newuser1-user1<target1:
              print("you are out for:")
              print(newuser1-user1,"runs")
              print("YOU LOSE.")
            else:
                print("you are tied with the computer.BETTER LUCK NEXT TIME")
        if bb=='10':
            user2=0
            computer2=0
            newuser2=0
            count1=0
            target2=20
            while user2!=computer2 or count1<10:
                try:
                    user2=input("enter a number between 1 and 6:")
                    conm(user2)
                    user2=abs(int(user2))
                    if user2>6 or user2<0:
                        print('DOT BALL')
                        user2-=user2
                    else:
                        pass
                    computer2=ran.randint(1,6)
                    print("computer has put",computer2)
                    newuser2+=user2
                    if user2==computer2:
                        count1+=1
                        print("NEW BATSMEN")
                        print("                     ")
                        newuser2=newuser2-user2
                        if newuser2>target2:
                            break
                        else:
                            pass
                    else:
                        if newuser2>target2:
                            break
                    
                    
                except:
                    print("something is wrong")
            if newuser2>target2:
                print("you have scored:")
                print(newuser2,"runs")
                print("YOU WIN")
            elif newuser2-user2<target2:
                print("you are out for:")
                print(newuser2-user2,"runs")
                print("YOU LOSE.")
                
            else:
                print("you are tied with the computer.BETTER LUCK NEXT TIME")
       
        ans=input("do you want to play again(y/n):")
    else:
        print("PLEASE RATE THE GAME ON 5 ")
        rayyan=input('PLEASE ENTER YOUR RATING:')
        conm(rayyan)
        print('THANK U FOR THE RATING')
        print('PLEASE DROP ANY SUGGESTION IF YOU HAVE')
        rayyan1=input('enter your suggestions:')
        conm(rayyan1)
    main()    
def musicplayer():
    count(3)
    import pygame
    pygame.mixer.init()
    def music(x):
        if x==0:
            x=input('enter the music u wanna play')
            con1(x)
            try:
                
                pygame.mixer.music.load(x+'.mp3')
                pygame.mixer.music.play()
            except:
                print('NO SUCH MUSIC')
                print()
                print()
                music(0)
        print('1.play another song, 2.exit')
        c=input('enter the option')
        conm(c)
        if int(c)==1:
            pygame.mixer.music.stop()
            return music(0)
        if int(c)==2:
            pygame.mixer.music.stop()
            return main()
    for i in range(7):
        print('\n')
    print('                                               MUSIC PLAYER')
    print()
    print()
    a=open('music.txt')
    print(a.read())
    print()
    print()
    print()
    music(0)
def settings():
    print('1.app usage data')
    print('2.change/set lockscreen pin')
    try:
        a=input('enter your option')
        con1(a)
        a=int(a)
        if a==1:
            data()
        if a==2:
            scrn_lock()
    except:
        print('something went wrong')
        settings()
def data():
    a=open('info1.txt','r')
    b=a.readlines()
    c=[ int(i.rstrip('\n'))for i in b ]
    x=['google','clock','musicplayer','notepad','currency convertor','game','info','contacts','calculator','python bank','currency convertor']
    
    plt.bar(x,c)
    plt.show()
    settings()
def scrn_lock():
    a=open('safe.txt','r')
    if a.read()=='':
        a.close()
        try:
            b=input('enter your password')
            con1(b)
            b=int(b)
            print('your password is set')
        except:
            print('something went wrong')
            scrn_lock
        c=open('safe.txt','w')
        c.write(encrypt(b))
        c.close()
    else:
        try:
            d=input('enter your old password')
            con1(d)
            d=int(d)
        except:
            print('something went wrong')
        h=open('safe.txt','r')
            
        if decrypt(h.read())==d:
            h.close()
            e=input('enter your new password')
            con1(e)
            e=int(e)
            i=open('safe.txt','w')
            i.write(encrypt(e))
            i.close()
        else:
            print('wrong pw')
            scrn_lock()
        
    settings()   

def lock_check():
    a=open('safe.txt','r')
    a.seek(0,0)
    if a.read()=='':
        pass
    else:
        try:
            b=input('enter the pin')
            con1(b)
            b=int(b)
        except:
            print('something went wrong')
            lock_check()
            k=decrypt(a.read())
        c=k
        if c==b:
            main()
        else:
            print('wrong pw')
            lock_check()

def contacts():
    count(9)
    
    print('                                                             CONTACTS')
    print()
    print()
    print('1.new contact')
    print('2.search')
    print('3.display all contacts')
    b=input('enter the option')
    con1(b)
    def newcont():
        try:
            a=open('contacts.txt','a')
            c=input('enter the name')
            con1(c)
            d=input('enter the phone number')
            con1(d)
            e=c+','+d+'\n'
            a.write(e)
            a.close()
        except:
            print('SOMETHING WENT WRONG')
            print()
            newcont()
    def search():
        try:
            f=open('contacts.txt','r')
            g=input('enter the name or number to be searched')
            con1(g)
            print()
            print()
            if g.isdigit():
                h=f.readlines()
                for i in h:
                    j=i.rstrip().split(',')
                    if g in j[1]:
                        for i in j:
                            print(i,end='-')
                        print()
                f.close()
            else:
                h=f.readlines()
                for i in h:
                    j=i.rstrip().split(',')
                    if g in j[0]:
                        for i in j:
                            print(i,end='-')
                        print()
                f.close()
        except:
            print('SOMETHING WENT WRONG')
            search()
    def display():
        try:
            
            f=open('contacts.txt','r')
            print()
            print()
            print()
            h=f.readlines()
            for i in h:
                j=i.rstrip().split(',')
                for i in j:
                    print(i,end='-')
                print()
        except:
            print('SOMETHING WENT WRONG')
            display()
    if int(b)==1:
        newcont()
    if int(b)==2:
        search()
    if int(b)==3:
        display()
    else:
        print()
        print()
        contacts()
def money_transfer1(x):
    conn=sqlite3.connect('banker.db')
    c=conn.cursor()

    a=open('datafile.txt')
    b=a.readline()
    if b=='':
        print('sign in using the bank app and then book')
        bank()
    a.close()
    
    for i in range(3):           
        N=input('ENTER THE 10 DIGIT OTP SENT TO UR MOBILE')
        N=int(N)
        con1(N)
        print('')
        print('')
        print('')
        O='select phno from acctdet where acctno='
        P=str(b)
        Q=O+P
        R=''
        c.execute(Q)
        for i in c:
            R=i
        for j in R:
            R=j
        if int(R)==N:
            print('THE OTP U HAVE ENTERED IS CORRECT : )')
            
            print('')
            print('')
            print('')   

            a9=1
            if a9==1:
                            
                M=x
                M=int(M)
                S='select money from acctdet where acctno='
                T=b
                U=S+T
                V=''
                c.execute(U)
                for i in c:
                    V=i
                for j in V:
                    V=j
                if  int(V)>M:
                    W='update acctdet set money=money-'
                    X=' where acctno='
                    Y=b
                    Z=W+str(M)+X+Y
                    c.execute(Z)
                    b5="'"
                    b6='select transactions from acctdet where acctno='
                    b7=b6+b
                    c.execute(b7)
                    for i in c:
                        b5=str(i)
                    b8=b5[1:len(b5)-3]
                                
                    b1=b8+'//rupees '+str(M)+' was transfered to bookmyshow'+'('+str(date.today())+')'+"'"
                    b2='update acctdet set transactions='
                    b3=b1
                    b4='where acctno='
                    b5=b2+b3+b4+str(b)
                    c.execute(b5)
                    conn.commit()
                    for x in range (0,5):
                        if x==0:
                            h2='TRANSFERING MONEY PLEASE WAIT'
                        else:
                            h2=''
                        time.sleep(0.5)
                        print(h2,'.'*x,end='')
                    print('')
                    print('')
                    time.sleep(5)
                    print('YOU HAVE SUCCESSFULLY TRANSFERED YOUR MONEY')
                    break
                else:
                    print('')   
                    print('YOU DONT HAVE ENOUGH MONEY, TRY AGAIN WITH A SMALLER AMOUNT : (')
            else:
                print('')   
                print('THE ACCOUNT NUMBER DOES NOT EXIST....TRY AGAIN : (')
                            
        else:
            print('')   
            print('THE OTP U ENTERED IS INCORRECT ,TRY AGAIN')
                
    else:
        print('')   
        print('RESTART THE PROGRAM AS U FINISHED 3 TRIES')
    
       
def pick_my_show():
    count(6)
    try:
        
        for i in 'PICK MY SHOW':
            time.sleep(0.2)
            print(' ',i,end='')
        print()
        ans='yes'
        while ans=='yes':


            print(".KOCHI")
            
            print('''           ''')
            op='kochi'
            
            
            if op=='KOCHI' or 'kochi':
                
                print('''    LIST OF MOVIES            ''')
                print("CHOOSE THE MOVIE YOU WANT TO CH")
                print("1.JOKER(ENG)")
                print("2.SPIDER-MAN 2(ENG)")
                print("3.THE ANGRY BIRDS MOVIE 2(ENG)")
                print("4.show which is the most booked movie")
                mo=input("Enter the option of the movie  you want to watch:")
                con1(mo)
                
                print('''
                                ''')


                '''print("THEATERS")
                print('''
                            
                if mo=='1':
                    print("1.PVR(G),EDAPPALLY-----TICKET PRICE:350 ruppees")
                    print("2.Q-CINEMAS,VYTTILA-----TICKET PRICE:250 ruppees")
                    print("3.SARITHA,MG-ROAD-----TICKET PRICE:150 ruppees")
                    to=input("enter the option of the theater you want:")
                    k1=input('enter the number of tickets:')
                    con1(k1)
                    k1=int(k1)
                        
                    if to=='1':
                        k2=k1*350
                        print('TOTAL AMOUNT=',k2)
                        print("TIMINGS")
                        print("1.10:30am")
                        print("2.1:00pm")
                        print("3.6:00pm")
                        x='y'
                        while x=='y':
                            kp=input("enter the option of the time required:")
                            con1(kp)
                            if kp.isalpha():
                                pass
                            else:
                                kp=int(kp)
                                x='k'
                                
                        
                        
                        if kp not in [1,2,3]:
                            print("INVALID OPTION. TRY BOOKING FOR ANOTHER MOVIE")
                            
                        elif kp==1:
                            print("1.pay at theatre")
                            print('2.pay using net banking')
                            b=input('enter the option')
                            con1(b)
                            b=int(b)
                            if b==2:
                                money_transfer1(k2)
                                
                            print("enjoy your movie")
                        elif kp==2:
                            print("pay at theatre")
                            print('pay using net banking')
                            b=input('enter the option')
                            con1(b)
                            b=int(b)
                            if b==2:
                                money_transfer1(k2)
                            print("enjoy your movie")
                        elif kp==3:
                            print("pay at theatre")
                            print('pay using net banking')
                            b=input('enter the option')
                            con1(b)
                            b=int(b)
                            if b==2:
                                money_transfer1(k2)
                            print("enjoy your movie")
            
                        
                    elif to=='2':
                        k3=k1*250
                        print('TOTAL AMOUNT=',k3)
                        print("TIMINGS")
                        print("1.11:30am")
                        print("2.3:00pm")
                        print("3.6:00pm")
                        kp=input("enter the option of time required.")
                        con1(kp)
                        kp=int(kp)
                        if kp not in [1,2,3]:
                                print("INVALID OPTION.TRY BOOKING FOR ANOTHER MOVIE")
                        elif kp==1:
                            print("pay at theatre")
                            print('pay using net banking')
                            b=input('enter the option')
                            con1(b)
                            b=int(b)
                            if b==2:
                                money_transfer1(k3)
                            print("enjoy your movie")
                        elif kp==2:
                            print("pay at theatre")
                            print('pay using net banking')
                            b=input('enter the option')
                            con1(b)
                            b=int(b)
                            if b==2:
                                money_transfer1(k3)
                            print("enjoy your movie")
                        elif kp==3:
                            print("pay at theatre")
                            print('pay using net banking')
                            b=input('enter the option')
                            con1(b)
                            b=int(b)
                            if b==2:
                                money_transfer1(k3)
                            print("enjoy your movie")
                        
                        
                    elif to=='3':
                        k3=k1*150
                        print('TOTAL AMOUNT=',k3)
                        print("TIMINGS")
                        print("1.10:30am")
                        print("2.1:00pm")
                        print("3.10:35pm")
                        kp=input("enter the option of the time required.")
                        con1(kp)
                        kp=int(kp)
                        if kp not in [1,2,3]:
                            print("INVALID OPTION.TRY BOOKING FOR ANOTHER MOVIE")
                        elif kp==1:
                            print("pay at theatre")
                            print('pay using net banking')
                            b=input('enter the option')
                            con1(b)
                            b=int(b)
                            if b==2:
                                money_transfer1(k3)
                            
                            print("enjoy your movie")
                        elif kp==2:
                            print("pay at theatre")
                            print('pay using net banking')
                            b=input('enter the option')
                            con1(b)
                            b=int(b)
                            if b==2:
                                money_transfer1(k3)
                            print("enjoy your movie")
                        elif kp==3:
                            print("pay at theatre")
                            print('pay using net banking')
                            b=input('enter the option')
                            con1(b)
                            b=int(b)
                            if b==2:
                                money_transfer1(k3)
                            print("enjoy your movie")
                        
                    else:
                        print("ERROR")
                        print("check for another movie")
                if mo=='2':
                    print("1.PVR,EDAPPALLY-----TICKET PRICE:280 ruppees")
                    print("2.PAN CINEMAS,VYTTILA-----TICKET PRICE:220 ruppees")
                    print("3.SARITHA,MG-ROAD-----TICKET PRICE:100 ruppees")
                    to=input("enter the option of the theater you want:")
                    k1=input('enter the number of tickets:')
                    con1(k1)
                    k1=int(k1)
                        
                    if to=='1':
                        k2=k1*280
                        print('TOTAL AMOUNT=',k2)
                        print("TIMINGS")
                        print("1.10:30am")
                        print("2.1:00pm")
                        print("3.6:00pm")
                        x='y'
                        while x=='y':
                            kp=input("enter the option of the time required:")
                            con1(kp)
                            if kp.isalpha():
                                pass
                            else:
                                kp=int(kp)
                                x='k'
                                
                        
                        
                        if kp not in [1,2,3]:
                            print("INVALID OPTION. TRY BOOKING FOR ANOTHER MOVIE")
                            
                        elif kp==1:
                            print("1.pay at theatre")
                            print('2.pay using net banking')
                            b=input('enter the option')
                            con1(b)
                            b=int(b)
                            if b==2:
                                money_transfer1(k2)
                                
                            print("enjoy your movie")
                        elif kp==2:
                            print("pay at theatre")
                            print('pay using net banking')
                            b=input('enter the option')
                            con1(b)
                            b=int(b)
                            if b==2:
                                money_transfer1(k2)
                            print("enjoy your movie")
                        elif kp==3:
                            print("pay at theatre")
                            print('pay using net banking')
                            b=input('enter the option')
                            con1(b)
                            b=int(b)
                            if b==2:
                                money_transfer1(k2)
                            print("enjoy your movie")
            
                        
                    elif to=='2':
                        k3=k1*220
                        print('TOTAL AMOUNT=',k3)
                        print("TIMINGS")
                        print("1.11:30am")
                        print("2.3:00pm")
                        print("3.6:00pm")
                        kp=input("enter the option of time required.")
                        con1(kp)
                        kp=int(kp)
                        if kp not in [1,2,3]:
                                print("INVALID OPTION.TRY BOOKING FOR ANOTHER MOVIE")
                        elif kp==1:
                            print("pay at theatre")
                            print('pay using net banking')
                            b=input('enter the option')
                            con1(b)
                            b=int(b)
                            if b==2:
                                money_transfer1(k3)
                            print("enjoy your movie")
                        elif kp==2:
                            print("pay at theatre")
                            print('pay using net banking')
                            b=input('enter the option')
                            con1(b)
                            b=int(b)
                            if b==2:
                                money_transfer1(k3)
                            print("enjoy your movie")
                        elif kp==3:
                            print("pay at theatre")
                            print('pay using net banking')
                            b=input('enter the option')
                            con1(b)
                            b=int(b)
                            if b==2:
                                money_transfer1(k3)
                            print("enjoy your movie")
                        
                        
                    elif to=='3':
                        k3=k1*100
                        print('TOTAL AMOUNT=',k3)
                        print("TIMINGS")
                        print("1.10:30am")
                        print("2.1:00pm")
                        print("3.10:35pm")
                        kp=input("enter the option of the time required.")
                        con1(kp)
                        kp=int(kp)
                        if kp not in [1,2,3]:
                            print("INVALID OPTION.TRY BOOKING FOR ANOTHER MOVIE")
                        elif kp==1:
                            print("pay at theatre")
                            print('pay using net banking')
                            b=input('enter the option')
                            con1(b)
                            b=int(b)
                            if b==2:
                                money_transfer1(k3)
                            
                            print("enjoy your movie")
                        elif kp==2:
                            print("pay at theatre")
                            print('pay using net banking')
                            b=input('enter the option')
                            con1(b)
                            b=int(b)
                            if b==2:
                                money_transfer1(k3)
                            print("enjoy your movie")
                        elif kp==3:
                            print("pay at theatre")
                            print('pay using net banking')
                            b=input('enter the option')
                            con1(b)
                            b=int(b)
                            if b==2:
                                money_transfer1(k3)
                            print("enjoy your movie")
                        
                    else:
                        print("ERROR")
                        print("check for another movie")
                
                if mo=='3':
                    print("1.CARNIVAL,ANGAMALY-----TICKET PRICE:150 ruppees")
                    print("2.CENTRAL TALKIES,VYTTILA-----TICKET PRICE:50 ruppees")
                    print("3.SAVITHA,MG-ROAD-----TICKET PRICE:100 ruppees")
                    to=input("enter the option of the theater you want:")
                    k1=input('enter the number of tickets:')
                    con1(k1)
                    k1=int(k1)
                        
                    if to=='1':
                        k2=k1*150
                        print('TOTAL AMOUNT=',k2)
                        print("TIMINGS")
                        print("1.10:30am")
                        print("2.1:00pm")
                        print("3.6:00pm")
                        x='y'
                        while x=='y':
                            kp=input("enter the option of the time required:")
                            con1(kp)
                            if kp.isalpha():
                                pass
                            else:
                                kp=int(kp)
                                x='k'
                                
                        
                        
                        if kp not in [1,2,3]:
                            print("INVALID OPTION. TRY BOOKING FOR ANOTHER MOVIE")
                            
                        elif kp==1:
                            print("1.pay at theatre")
                            print('2.pay using net banking')
                            b=input('enter the option')
                            con1(b)
                            b=int(b)
                            if b==2:
                                money_transfer1(k2)
                                
                            print("enjoy your movie")
                        elif kp==2:
                            print("pay at theatre")
                            print('pay using net banking')
                            b=input('enter the option')
                            con1(b)
                            b=int(b)
                            if b==2:
                                money_transfer1(k2)
                            print("enjoy your movie")
                        elif kp==3:
                            print("pay at theatre")
                            print('pay using net banking')
                            b=input('enter the option')
                            con1(b)
                            b=int(b)
                            if b==2:
                                money_transfer1(k2)
                            print("enjoy your movie")
            
                        
                    elif to=='2':
                        k3=k1*50
                        print('TOTAL AMOUNT=',k3)
                        print("TIMINGS")
                        print("1.11:30am")
                        print("2.3:00pm")
                        print("3.6:00pm")
                        kp=input("enter the option of time required.")
                        con1(kp)
                        kp=int(kp)
                        if kp not in [1,2,3]:
                                print("INVALID OPTION.TRY BOOKING FOR ANOTHER MOVIE")
                        elif kp==1:
                            print("pay at theatre")
                            print('pay using net banking')
                            b=input('enter the option')
                            con1(b)
                            b=int(b)
                            if b==2:
                                money_transfer1(k3)
                            print("enjoy your movie")
                        elif kp==2:
                            print("pay at theatre")
                            print('pay using net banking')
                            b=input('enter the option')
                            con1(b)
                            b=int(b)
                            if b==2:
                                money_transfer1(k3)
                            print("enjoy your movie")
                        elif kp==3:
                            print("pay at theatre")
                            print('pay using net banking')
                            b=input('enter the option')
                            con1(b)
                            b=int(b)
                            if b==2:
                                money_transfer1(k3)
                            print("enjoy your movie")
                        
                        
                    elif to=='3':
                        k3=k1*100
                        print('TOTAL AMOUNT=',k3)
                        print("TIMINGS")
                        print("1.10:30am")
                        print("2.1:00pm")
                        print("3.10:35pm")
                        kp=input("enter the option of the time required.")
                        con1(kp)
                        kp=int(kp)
                        if kp not in [1,2,3]:
                            print("INVALID OPTION.TRY BOOKING FOR ANOTHER MOVIE")
                        elif kp==1:
                            print("pay at theatre")
                            print('pay using net banking')
                            b=input('enter the option')
                            con1(b)
                            b=int(b)
                            if b==2:
                                money_transfer1(k3)
                            
                            print("enjoy your movie")
                        elif kp==2:
                            print("pay at theatre")
                            print('pay using net banking')
                            b=input('enter the option')
                            con1(b)
                            b=int(b)
                            if b==2:
                                money_transfer1(k3)
                            print("enjoy your movie")
                        elif kp==3:
                            print("pay at theatre")
                            print('pay using net banking')
                            b=input('enter the option')
                            con1(b)
                            b=int(b)
                            if b==2:
                                money_transfer1(k3)
                            print("enjoy your movie")
                        
                    else:
                        print("ERROR")
                        print("check for another movie")
                                
               
                 
                elif mo=='4':
                    import matplotlib.pyplot as pl
                    stream=['JOKER','SPIDER-MAN 2','ANGRY BIRDS MOVIE 2']
                    nst=[55,41,31]
                    colors=['yellow','red','green','gold']
                    explode=(0.1,0,0)
                    pl.pie(nst,labels=stream,explode=explode,colors=colors,shadow=True,startangle=90,autopct="%6.2f%%")
                    pl.show()             
                    
                else:
                    print("enter a valid option number")
                    print("TRY BOOKING ANOTHER MOVIE")
                    
            ans=input("do yo want to check for more movies:(yes/no):")
        else:
            print("BYE...")
            main()
    except:
       print('something went wrong')
       pick_my_show()
    main()
def bank():
    conn=sqlite3.connect('banker.db')

    c=conn.cursor()
   #c.execute('select * from acctdet')
    #for j in c:
        #print(j)'''

         
    def main_yes():
        try:
            
            if count1==1:   
                print('CURRENT ACCOUNT NUMBER IN USE:',d)
                print()
                l1.close()
                print()
                print('1.TO CHANGE EXSISTING DETAILS , 2.TO TRANSFER FUNDS ,3.TO CHECK ACCOUNT DETAILS ,4.INFORMATION ON BANK,5.LOG OUT')
                print('')
                n=input('ENTER YOUR OPTION')
                con2(n)
                n=int(n)
                print('')
                if n==1:
                    detail_change()
                if n==2: #money transfer
                        
                    money_transfer()
                            
                if n==3:#to chek acct det
                        
                    acct_det()
                if n==4:
                            
                    print('HEY GUYS THIS BANK WAS CREATED BY SAM RISHI AND RAYYAN ON ')
                    print('')
                    print('THANKS FOR USING OUR BANK AND APPRECIATE UR TRUST IN US : )')
                    print('')
                    print('YOUR MONEY SHALL BE SAFE IN OUR HANDS ; )')
                if n==5:
                    l3=open('datafile.txt','w').close()
                print('')
                print('')
                bank()
        except:
            print('something went wrong,try again')
            main_yes()


    def detail_change():
        try:
            print('1.CHANGE PHONE NUMBER , 2. CHANGE PIN , 3. CHANGE ADDRESS ........')
            o=input('ENTER YOUR OPTION')
            con2(o)
            o=int(o)
            if o==1:#change phno
                p='update acctdet set phno='
                q=input('ENTER YOUR NEW NUMBER')
                con2(q)
                r=' where acctno='
                s=str(d)
                t=p+q+r+s
                print('')   
                v=input('ENTER Y OR YES IF U R SURE TO CONTINUE:')
                con2(v)
                if v=='y' or v=='Y' or v=='YES' or v=='yes':
                    c.execute(t)
                    conn.commit()
                else:
                    pass
                            
            if o==2:           #change pin
                            
                u='update acctdet set pin='
                w=input('ENTER YOUR NEW PIN')
                
                w=encrypt(w)
                A=' where acctno='
                B=str(d)
                C=u+'"'+w+'"'+A+B
                D=input('ENTER Y OR YES IF U R SURE TO CONTINUE:')
                
                if D=='y' or D=='Y' or D=='YES' or D=='yes':
                    c.execute(C)
                    conn.commit()
                else:
                    pass
            if o==3:      #change address
                            
                E='update acctdet set address='
                F=input('ENTER YOUR NEW ADDRESS')
                con2(F)
                G=' where acctno='
                H=str(d)
                I=E+F+G+H
                print('')   
                J=input('ENTER Y OR YES IF U R SURE TO CONTINUE:')
                con2(J)
                if J=='y' or J=='Y' or J=='YES' or J=='yes':
                    c.execute(I)
                    conn.commit()
                else:
                    print('RESTART THE PROGRAM')
        except:
            print('something went wrong,try again')
            detail_change()


    def acct_det():
        try:
            print('1. TO SEE ACCOUNT STATUS , 2. TO SEE TRANSACTIONS')
            b10=input('ENTER YOUR OPTION')
            con2(b10)
            b10=int(b10)
            if b10==1:
                print('')
                print('ACCOUNT NO: ',d)
                print('')
                c.execute('select name from acctdet where acctno='+str(d))
                b45=''
                for i in c:
                    b45=str(i)
                b45=b45[1:len(b45)-2]
                        
                print('NAME : ',b45)
                print('')
                print('PIN: ',z)
                print('')
                b11='select address from acctdet where acctno='
                b12=b11+str(d)
                c.execute(b12)
                b13=''
                for j in c:
                    b13=str(j)
                b14=b13[1:len(b13)-2]
                print('ADDRESS: ',b14)
                print('')
                b15='select phno from acctdet where acctno='
                b16=b15+str(d)
                c.execute(b16)
                b17=''
                for i in c:
                    b17=str(i)
                b18=b17[1:len(b17)-2]
                print('PHONE NUMBER: ',b18)
                                           
            if b10==2:
                                
                c1='select transactions from acctdet where acctno='
                c2=c1+str(d)
                c.execute(c2)
                c3=''
                for i in c:
                    c3=str(i)
                c4=c3[1:len(c3)-2].split('//')
                print('')   
                print('YOUR TRANSACTIONS ARE: ')
                for i in c4:
                    print('     ',i)
            main_yes()
        except:
            print('something went wrong,try again')
            acct_det()
    def money_transfer():
        try:
            for i in range(3):
                            
                N=input('ENTER THE 10 DIGIT OTP SENT TO UR MOBILE')
                con2(N)
                N=int(N)
                print('')
                print('')
                print('')
                O='select phno from acctdet where acctno='
                P=str(d)
                Q=O+P
                R=''
                c.execute(Q)
                for i in c:
                    R=i
                for j in R:
                    R=j
                if int(R)==N:
                    print('THE OTP U HAVE ENTERED IS CORRECT : )')
                    print('')
                    print('')
                    K=input('ENTER THE ACCOUNT NUMBER OF THE RECIEVING PERSON')
                    con2(K)
                    K=int(K)
                    print('')   
                    L=input('ENTER THE NAME OF THE ACOUNT HOLDER')
                    con2(L)
                    a8=[]
                    c.execute('select acctno from acctdet')
                    for i in c.fetchall():
                        a8.append(i)
                    a9=0
                    for j in range(len(a8)):
                        if K in a8[j]:
                            a9=1
                            break
                    if a9==1:
                                    
                        M=input('ENTER THE AMOUNT OF MONEY TO BE TRANFERED')
                        con2(M)
                        M=int(M)
                        S='select money from acctdet where acctno='
                        T=str(d)
                        U=S+T
                        V=''
                        c.execute(U)
                        for i in c:
                            V=i
                        for j in V:
                            V=j
                        if  int(V)>M:
                            W='update acctdet set money=money-'
                            X=' where acctno='
                            Y=str(d)
                            Z=W+str(M)+X+Y
                            c.execute(Z)
                            a1='update acctdet set money=money+'
                            a2=' where acctno='
                            a3=str(K)
                            a4=a1+str(M)+a2+a3
                            c.execute(a4)
                            b5="'"
                            b6='select transactions from acctdet where acctno='
                            b7=b6+str(d)
                            c.execute(b7)
                            for i in c:
                                b5=str(i)
                            b8=b5[1:len(b5)-3]
                                        
                            b1=b8+'//rupees '+str(M)+' was transfered to account '+str(K)+'('+str(date.today())+')'+"'"
                            b2='update acctdet set transactions='
                            b3=b1
                            b4='where acctno='
                            b5=b2+b3+b4+str(d)
                            c.execute(b5)
                            conn.commit()
                            for x in range (0,5):
                                if x==0:
                                    h2='TRANSFERING MONEY PLEASE WAIT'
                                else:
                                    h2=''
                                time.sleep(0.5)
                                print(h2,'.'*x,end='')
                            print('')
                            print('')
                            time.sleep(5)
                            print('YOU HAVE SUCCESSFULLY TRANSFERED YOUR MONEY')
                            break
                        else:
                            print('')   
                            print('YOU DONT HAVE ENOUGH MONEY, TRY AGAIN WITH A SMALLER AMOUNT : (')
                    else:
                        print('')   
                        print('THE ACCOUNT NUMBER DOES NOT EXIST....TRY AGAIN : (')
                                    
                else:
                    print('')   
                    print('THE OTP U ENTERED IS INCORRECT ,TRY AGAIN')
                        
            else:
                print('')   
                print('RESTART THE PROGRAM AS U FINISHED 3 TRIES')
        except:
            print('something went wrong , try again')
            money_transfer()
    def encrypt(b):
        b=str(b)
        a=''
        for i in b:
            a+=''
            if i=='0':
                a+='1hy:#'
            if i=='1':
                a+='jky@#'
            if i=='2':
                a+='ght*#'
            if i=='3':
                a+='s@23#'
            if i=='4':
                a+='f$%!#'
            if i=='5':
                a+=':_+7#'
            if i=='6':
                a+='t:@:#'
            if i=='7':
                a+='h":£#'
            if i=='8':
                a+=':mu%#'
            if i=='9':
                a+='r^:;#'
        return a
    def decrypt(x):
        b=x.split('#')
        a=''
        for i in b:
            if i=='1hy:':
                a+='0'
            if i=='jky@':
                a+='1'
            if i=='ght*':
                a+='2'
            if i=='s@23':
                a+='3'
            if i=='f$%!':
                a+='4'
            if i==':_+7':
                a+='5'
            if i=='t:@:':
                a+='6'
            if i=='h":£':
                a+='7'
            if i==':mu%':
                a+='8'
            if i=='r^:;':
                a+='9'
        return int(a)

    def dataupdate():

        c.execute('select lastupdated from acctdet where acctno=101010')
        e14=''
        for g in c:
            e15=str(g)
            e16=e15[2:len(e15)-3]
            e14=e16
        f1=str(date.today())
        if f1!=e14:
            c.execute('select acctno from  acctdet')
            c24=[]
            for j in c:
                c22=str(j)
                c23=c22[1:len(c22)-2]
                c24.append(c23)
                

            for i in c24:

                c21='select date from acctdet where acctno='
                c25=c21+i
                c.execute(c25)
                c19=""
                for j in c:
                    c19=str(j)
                c20=c19[2:len(c19)-3]
                c5=str(date.today())
                c7=int(c5[5:7])
                c9=c20
                c8=int(c9[5:7])
                c10=(c8-c7)*30.33#month
                if c10<0:
                    c10*=-1
                c11=int(c5[0:4])
                c12=int(c9[0:4])
                c13=(c12-c11)*364#year
                if c13<0:
                    c13*=-1
                c14=c13+c10
                c15=int(c9[8:11])
                c16=int(c5[8:11])
                c17=c16-c15
                if c17<0:
                    c17=c17*-1
                c18=c17+c14
                d1='update acctdet set dayspassed='
                d3=str(c18)
                d4=' where acctno='
                d2=d1+d3+d4+i
                c.execute(d2)
                d5='select dayspassed from acctdet where acctno='
                d6=d5+i
                c.execute(d6)
                d10=c18   #holds the value of days passed
                d11='select money from acctdet where acctno='
                d12=d11+i
                c.execute(d12)
                d13=''   #holds the integer part of the money
                for f in c:
                    d14=str(f)
                    d15=d14[1:len(d14)-4]
                    d13=int(d15)
                e1=d10/364
                e2=d13*8*e1
                e3=e2//100
                e4=d13+e3   #hold the total after interest rate
                e5='update acctdet set money='
                e6=' where acctno='
                e7=e5+str(e4)+e6+i
                c.execute(e7)
                conn.commit()
                e10='update acctdet set lastupdated='
                e11=str(date.today())

                e12=e10+"'"+e11+"'"
                c.execute(e12)
                conn.commit()
                c.execute('select lastupdated from acctdet where acctno=101010')
            
    dataupdate()

    #                                           ACTUAL PROGRAM FROM HERE : )

    print('                                WELCOME TO PYTHON BANKING : )')
    '''c.execute('select * from acctdet')
    for i in c:
        print(i)'''
    print('')
    h1=''
    for x in range (0,5):
        if x==0:
            h1='LOADING'
        else:
            h1=''
        time.sleep(0.5)
        print(h1,'.'*x,end='')
    print('')
    print('')
    time.sleep(2)
    b=input('DO YOU HAVE A BANK ACCOUNT')
    print('')
    con2(b)
    if b=='yes' or b=='YES' or b=='y' or b=='Y':
        g=[]
        c.execute('select acctno from acctdet')
        for i in c.fetchall():
            g.append(i)
        h=0
        print('')
        count1=''
        d=''
        i=''
        z=''
        l1=open('datafile.txt','r+')
        
        if l1.readline()=='':
            while True:
                try:
                    d=input('ENTER YOUR ACCOUNT NUMBER')
                    con2(d)
                    d=int(d)
                    break
                except:
                    print('something went wrong')
                    
            for j in range(len(g)):
                if d in g[j]:
                    h=1
                    break
            if h==1:
                for i in range(3):
                    e=[]
                    f=''
                    i=input('ENTER YOUR NAME')
                    con2(i)
                    while True:
                        try:
                            z=input('ENTER YOUR PIN')
                            con2(z)
                            z=int(z)
                            break
                        except:
                            print('something went wrong')
                    print('')
                    c.execute('select acctno,pin,name from acctdet')
                    for i in c:
                          e.append(i)
                    for j in range(len(e)):
                          if d in e[j]:
                              f=j
                    l=[]
                    for i in e[f]:
                        l.append(i)
                    count=0
                    count1=0
                    m=decrypt(l[1])
                    
                    if i in l:
                        count+=1
                        
                    if int(m)==z:
                        count+=1
                        
                    if count==2:
                        print('YOU HAVE BEEN SUCCESSFULLY LOGGED IN')
                        l2=[]
                        l2.append(str(d)+'\n')
                        l2.append(i+'\n')
                        l2.append(encrypt(z)+'\n')
                        l1.writelines(l2)
                        l1.close()
                        
                        count1+=1
                        break
                    else:
                        print('YOU HAVE ENTERED THE WRONG PIN OR NAME PLS TRY AGAIN')
                else:
                    print('RESTART THE PROGRAM TO TRY AGAIN AS U HAVE COMPLETED 3 TRIES')
                
            else:
              print('YOUR ACCOUNT NUMBER DOES NOT EXIST')
        else:
            l1.seek(0,0)
            count1=1
            d=int(l1.readline().rstrip('\n'))
            i=l1.readline().rstrip('\n')
            z=int(decrypt(l1.readline().rstrip('\n')))
            
        main_yes()
                    
    if b=='no' or b=='NO' or b=='n' or b=='N':
        try:
            print('START YOUR ACCOUNT NOW .....JUST FILL IN THE DETAILS')
            print('')
            for k in range(5):
                
                g1=input('ENTER AN ACCOUNT NUMBER OF UR WISH')
                con2(g1)
                g1=int(g1)
                g3=0
                c.execute('select acctno from acctdet')
                g8=[]
                for l in c:
                    g9=str(l)
                    g10=g9[1:len(g9)-2]
                    g8.append(int(g10))
                if g1 not in g8:
                    g3=1
                    break
                else:
                    print('THIS NUMBER ALREADY EXISTS TRY AGAIN')
                    
            if g3==1:
                g4=input('ENTER YOUR NAME')
                con2(g4)
                g5=input('ENTER YOUR PIN')
                con2(g5)
                g5=int(g5)
                g6=input('ENTER YOUR ADDRESS')
                con2(g6)
                g7=input('ENTER THE AMOUNT OF MONEY TO BE DEPOSITED')
                con2(g7)
                g7=int(g7)
                g8=str(date.today())
                g9=''
                g10=input('ENTER YOUR PHONE NUMBER')
                con2(g10)
                g10=int(g10)
                c.execute('insert into acctdet(acctno,pin,name,phno,address,money,transactions,date) VALUES(?,?,?,?,?,?,?,?)',(g1,encrypt(g5),g4,g10,g6,g7,g9,g8))

                conn.commit()
        except:
            print('something went wrong')
             
    print('')        
    c.close()
    conn.close()

           
def notepad():
    count(4)
    print('                                       NOTEPAD')
    print()
    print()
    print('1.new , 2.edit')
    k10=input('enter the option')
    con1(k10)
    def con(x):
        if x.isdigit():
            return int(x)
        else:
            return x
    f=open('notepad.txt','r+')
    if con(k10)==1:
        a=input('enter the name of the memo')
        con1(a)
        b=input('enter the no of lines')
        con1(b)
        b=con(b)
        c=[]
        for i in range(b):
            d=input('enter the content')
            con1(d)
            c.append(d+'\n')
        e=open(a+'.txt','w')
        e.writelines(c)
        e.close()
        f.write(a+'.txt\n')
        f.close()
        l=input('press "\c" to go to menu')
        con1(l)
        notepad()
    if con(k10)==2:
        print(f.read())
        g=input('enter the memo name')
        con1(g)
        print('1.to rewrite entire memo , 2.add new lines')
        i=input('enter the option')
        con1(i)
        if con(i)==1:
            b=input('enter the no of lines')
            con1(b)
            b=con(b)
            c=[]
            for i in range(b):
                d=input('enter the content')
                con1(d)
                c.append(d+'\n')
            j=open(g+'.txt','w')
            j.writelines(c)
            j.close()
            l=input('press "\c" to go to menu')
            con1(l)
            notepad()
        if con(i)==2:
            h=open(g+'.txt','r+')
            print(h.read())
            b=input('enter the no of lines')
            con1(b)
            b=con(b)
            c=[]
            for i in range(b):
                d=input('enter the content')
                con1(d)
                c.append(d+'\n')
            h.writelines(c)
            h.close()
            l=input('press "\c" to go to menu')
            con1(l)
            notepad()
def reset():
    print('                                 RESET')
    print()
    print()
    c=input('r u sure u wanna reset y/n')
    if c=='n':
        main()
    else:
        
        con1(c)
        print('reseting.........')
        time.sleep(3)
        a=open('myprofile.txt','w')
        a.write('')
        b=open('safe.txt','w')
        b.write('')
        b.close()
        a.close()
        print('restarting system......!')
        time.sleep(4)
        print()
        print()
        print()
        intro()
        info()
        main()
def calc():
    count(9)
    print('                                                         CALCULATOR')
    print()
    print()
    try:
        a=input('enter the whole combination of operations')
        con1(a)
        b=[]
        c=0
        for i in range(len(a)):
            if a[i] in ['*','%','/','+','-','^']:
                b.append(i)
                if c==0:
                    c=int(a[:i])
        for j in range(len(b)):
            if j<len(b)-1:
                if a[b[j]]=='*':
                    c*=int(a[b[j]+1:b[j+1]])
                if a[b[j]]=='-':
                    c=c-int(a[b[j]+1:b[j+1]])
                if a[b[j]]=='+':
                    c+=int(a[b[j]+1:b[j+1]])
                if a[b[j]]=='/':
                    c=c/int(a[b[j]+1:b[j+1]])
                if a[b[j]]=='%':
                    c=c%int(a[b[j]+1:b[j+1]])
                if a[b[j]]=='^':
                    c=c**int(a[b[j]+1:b[j+1]])
            else:
                if a[b[j]]=='*':
                    c*=int(a[b[j]+1:])
                if a[b[j]]=='-':
                    c=c-int(a[b[j]+1:])
                if a[b[j]]=='+':
                    c+=int(a[b[j]+1:])
                if a[b[j]]=='/':
                    c=c/int(a[b[j]+1:])
                if a[b[j]]=='%':
                    c=c%int(a[b[j]+1:])
                if a[b[j]]=='^':
                    c=c**int(a[b[j]+1:])
        print(c)
        n=input('press "\c" to exit')
        con1(n)
        calc()
    except:
        print('AN ERROR HAS OCCURED TRY AGAIN')
        calc()
def userinfo():
    count(7)
    print('                                        USERINFO')
    print()
    print()
    a=open('myprofile.txt','r')
    print(a.read())
    c=input('press "\c" to go to home screen')
    con1(c)
    userinfo()
def google():
    count(1)
    print('                                         GOOGLE')
    print()
    print()
    a=input('enter what u wanna search')
    con1(a)
    b=a.split()
    c=''
    for i in b:
        c+=i+'+'        
    url = "https://www.google.com/search?q="+c+"&rlz=1C1EJFA_enIN774IN830&oq="+c+"&aqs=chrome.0.0l6.5441j0j7&sourceid=chrome&ie=UTF-8"   
    webbrowser.open(url)
    main()
def cash_conv():
    count(11)
    try:
        a=input("""Select your currency that needs to be converted:
        1.Dirhams
        2.Yen
        3.Rupees
        4.Dollars
        5.Pounds""")
        con1(a)
        a=int(a)
        if a==1:
            b=input("Enter the amount that needs to be coverted:")
            con1(b)
            c=input("""Select the currency you would like to convert to:
        6.Yen
        7.Rupees
        8.Dollars
        9.Pounds""")
            con1(c)
            b=int(b)
            c=int(c)
            if c==6:
                d=b*29
                print(d,"¥")
            elif c==7:
                e=b*20
                print(e,"₹")
            elif c==8:
                f=b*0.3
                print(f,"$")
            elif c==9:
                g=b*0.20
                print(g,"€")
        if a==2:
            b1=input("Enter the amount that needs to be coverted:")
            con1(b1)
            c1=input("""Select the currency you would like to convert to:
        10.Dirhams
        11.Rupees
        12.Dollars
        13.Pounds""")
            con1(c1)
            b1=int(b1)
            c1=int(c1)
            if c1==10:
                d1=b1*0.03
                print(d1,"د.إ")
            elif c1==11:
                d2=b1*0.7
                print(d2,"₹")
            elif c1==13:
                d3=b1*0.007
                print(d3,"€")
            elif c1==12:
                d4=b1*0.009
                print(d4,"$")

        if a==3:
            b2=input("Enter the amount that needs to be coverted:")
            con1(b2)
            b2=int(b2)
            c2=input("""Select the currency you would like to convert to:
        14.Dirhams
        15.Yen
        16.Dollars
        17.Pounds""")
            con1(c2)
            c2=int(c2)
            if c2==14:
                d5=b2*0.051 
                print(d5,"د.إ")
            elif c2==15:
                d6=b2*1.5
                print(d6,"¥")
            elif c3==16:
                d7=b2*0.014
                print(d7,"$")
            elif c4==17:
                d8=b2*0.011
                print(d8,"€")
        if a==4:
            b3=input("Enter the amount that needs to be coverted:")
            con1(b3)
            b3=int(b3)
            c3=input("""Select the currency you would like to convert to:
        18.Dirhams
        19.Yen
        20.Rupees
        21.Pounds""")
            con1(c3)
            c3=int(c3)
            if c3==18:
                d8=b3*3.5
                print(d8,"د.إ")
            elif c3==19:
                d9=b3*107
                print(d9,"¥")
            elif c3==20:
                d10=b3*72
                print(d10,"₹")
            elif c3==21:
                d11=b3*0.80
                print(d11,"€")
        if a==5:
            b4=input("Enter the amount that needs to be coverted:")
            con1(b4)
            b4=int(b4)
            c4=input("""Select the currency you would like to convert to:
        22.Dirhams
        23.Yen
        24.Rupees
        25.Dollars""")
            con1(c4)
            c4=int(c4)
            if c4==22:
                d12=b4*4.5
                print(d12,"د.إ")
            if c4==23:
                d13=b4*132
                print(d13,"¥")
            if c4==24:
                d14=b4*88
                print(d14,"₹")
            if c4==25:
                d15=b4*1.20
                print(d15,"$")
        if a>5 or a<0:
            print("Error occured , please res.")
        cash_conv()
    except:
        print('something went wrong')
        cash_conv()
def clock():
    count(2)
    print('                                      CLOCK')
    print()
    print()
    print('1.clock')
    print('2.timer')
    print('3.alarm')
    k1=input('enter the option')
    con1(k1)
    b=''
    def con(x):
        if x.isdigit():
            return int(x)
        else:
            return x
    if con(k1)==1:
        print(str(datetime.now())[10:20])
    if con(k1)==2:
        k2=input('enter the time limit')
        con1(k2)
    
        k3=con(k2)
        if type(k3)==int:
            time.sleep(k3)
        print('your time is up')
    if con(k1)==3:
        k4=input('enter the time to be set in hh:mm in railway format')
        try:
            int(k4[:2])
            int(k4[3:5])
            if k4[2]!=':':
                print('not the correct format')
                clock()
        except:
            print('not the correct format')
            clock()
            
        con1(k4)
        k5=k4.split(':')
        k6=str(datetime.now())[10:19]
        k10=open('alarm.txt','w')
        k10.write(k4)
        k10.close()
    c=input('press "\c" to go to home screen')
    con1(c)
    clock()
def alarm():
    a=open('alarm.txt','r')
    b=a.read()
    if b!='':
        
        c=str(datetime.now())[11:19]
        if int(b[:2])<=int(c[:2]):
            if int(b[3:6])<=int(c[3:5]):
                print('your alarm is ringing')
                pygame.mixer.music.stop()
                pygame.mixer.music.load('alarm.mp3')
                pygame.mixer.music.play()
                print()
                d=input('press n to stop alarm')
                if d=='n':
                    pygame.mixer.music.stop()
                    d=open('alarm.txt','w')
                    d.write('')
                    d.close()
def count(x):
    a=open('info1.txt','r')
    b=a.readlines()
    b[x-1]=str(int(b[x-1].rstrip('\n'))+1)+'\n'
    a.close()
    c=open('info1.txt','w')
    c.writelines(b)
    c.close()
def con2(x):
    alarm()
    if x=='\c':
        for i in range(10):
            print()
        return main()
    if x=='\c\c':
        sys.exit()
        
    
def con1(x):
    alarm()
    if x=='\c':
        for i in range(10):
            print()
        return main()
    if x=='\c\c':
        sys.exit()
def conm(x):
    import pygame
    pygame.mixer.init()
    if x=='\c':
        for i in range(8):
            print()
        pygame.mixer.music.stop()
        return main()
    if x=='\c\c':
        sys.exit()
intro()
a=open('myprofile.txt','r')
if a.read()=='':
    info()
a.close()
main()



