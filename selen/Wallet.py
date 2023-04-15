"""
InsufficientAmount - класс - который содержит исключение

 pass - не описано
 связь с внутренним api
 """
class InsufficientAmount(Exception):
   pass



"""
    __balance - кошелька
    - узнаем баланс
    - зачисляем деньги
    - списываем деньги
        - проверка на отрицательность баланс
"""
class Wallet:
   def __init__(self, balance=0):# balance = 0 - если изначельно деньги не засчительна
       self.__balance = balance # инкапсуляция - __balance - закрываем внешний доступ

   def get_balance(self):# узнаем баланс
       return self.__balance

   def add_cash(self, amount):# зачисляем деньги amount - сумма зачисления
       self.__balance = self.__balance + amount
       print("Баланс карты: ", self.__balance)

   def spend_cash(self, spend_sum):# тратим деньги spend_sum - сумма списания
       if spend_sum < self.__balance:# достаточно ли денег на балансе?
           self.__balance = self.__balance - spend_sum
           print("Баланс карты: ",  self.__balance)
       else:# денег не достаточно
           raise InsufficientAmount("Недостаточно средств на счету.")
