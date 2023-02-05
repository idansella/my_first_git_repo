
def my_first_repo():
    file = open('data.txt', 'w')
    file.write('My first Git repository in out')
    file = open('data.txt', 'r')
    print(file.read())


def dont_call_me_local():
    file = open('whyyyy.txt', 'w')
    file.write('Why you dont obey?!')
    file = open('whyyyy.txt', 'r')
    print(file.read())


my_first_repo()
dont_call_me_local()
