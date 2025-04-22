# def group_st(a):
#     group_list=a.split(',')
#     int_list=list(map(lambda x:int(x),group_list))
#     kichik=[]
#     katta=[]
#     for i in int_list:
#         if i<=20:
#             kichik.append(i)
#         else:
#             katta.append(i)
#     if len(katta)>len(kichik):
#         javob=f'Kattalar kop soni {len(katta)} {katta}'
#     else:
#         javob=f'Kichik kop soni {len(kichik)} {kichik}'
#     max_yosh=max(int_list)
#     min_yosh=min(int_list)
#     dif=max_yosh-min_yosh
#     yosh_set=set(int_list)
#     return javob,dif,yosh_set


# user_answer=input('jamoalarni yozinga 12,19,15,23')
# answer=group_st(user_answer)
# print(f"""
# javob:
# yoshi cat:{answer[0]}
# yoshi farq:{answer[1]}
# yoshi toifa:{answer[2]}      """)


# try:
#     son1=int(input("Son yozing: "))
#     son2=int(input("Son yozing: "))
#     print(son1/son2)
# except ZeroDivisionError:
#     print("Siz Zero devisionga uchradingiz")
# except ValueError:
#     print(' int str amal bajarmang')


# try:
#     son1=int(input("Son yozing: "))
#     son2=int(input("Son yozing: "))
#     print(son1/son2)
# except Exception as e:
#     print(f"Siz {e} hatoligiga uchradingiz")


# try:
#     son1=int(input("Son yozing: "))
#     son2=int(input("Son yozing: "))
#     print(son1/son2)
# except Exception as e:
#     print(f"Siz {e} hatoligiga uchradingiz")
# else: print("xammasi yaxshi")

# finally: print('Dastur tugadi')


# def set_age(negativ):
#     if negativ > 0: 
#         raise ValueError("Negativ cannot be plus")
#     print(f"Negative set to {negativ}")


# try:
#     set_age(5)
#     n = 5
# except ValueError as e:
#     print(e)


def devide (x,y):
    try:
         result = x//y
         print("Natija: ", result)
    except ZeroDivisionError as a: 
         print(f"Xatolik. notga bolish mumkinmas{a}")

devide(5,3)