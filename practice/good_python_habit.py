=========================1 one=======================
def is_an_adult(age: int, has_id: bool) -> bool:
    return age >= 21 and has_id


def is_bob(name: str) -> bool:
    return name.lower() == 'bob'


def enter_club(name: str, age: int, has_id: bool) -> None:
    if is_bob(name):
        print("Get out of here Bob")
        return

    if is_an_adult(age, has_id):
        print('you may enter the clud')
    else:
        print('you may not enter the club')
        
        
# #DO not dot that below code practice not good, we need to write function like above
# def enter_club(name: str, age: int, has_id: bool) -> None:
#     if name.lower() == 'bob':
#         print("Get out of here Bob")
#         return
# 
#     if age >=21 and has_id:
#         print('you may enter the clud')
#     else:
#         print('you may not enter the club')

def main() -> None:
  enter_club('Bob', 29, has_id=True)
  enter_club('James', 29, has_id=True)
  enter_club('Russel', 29, has_id=False)
  enter_club('Arish', 9, has_id=True)


if __name__ == '__main__':
    main()
============================end========================
===============2 two===================================
===========Do not do==========================
# def upper_all(elements):
#   return [e.upper() for e in elements]
===========Do it below==============================
def upper_all(ele: list[str]) -> list[str]:
  return [e.upper() for e in ele]
============================end========================
===============3 three=================================
# people = ['arish', 'momo', 'arshan', 'dulal', 'moriom', 'nazrul']
# long_name = []
# for person in people:
#     if len(person) > 5:
#         long_name.append(person)
==================List comprehensive===================
long_name2 = [p for p in people if len(p) > 5]
print(long_name2)
============================end========================
