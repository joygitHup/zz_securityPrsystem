import random


class randum_pr_account_number():
    def __init__(self):
        self.constat=str('test')
    def produce_account(self):
        new_account=self.constat+str(random.randint(10,99))
        return new_account
if __name__=="__main__":
    op=randum_pr_account_number()
    print(op.produce_account())
