# Python Tutorial- Generator & Yield 

# Especially useful for memory sensitive application

in python 2.x, range(3) create a list  consumes memory
in python 3.x, range(3) create a generator object that does not have a len(), members are calculated using yield on the fly

EG:

>>> print(next(the_generator))	 	 
generator started	 	 
Fritz Pythonmann 128-256-512	 	 


# ������ def �����壬 ����Ҫʹ�� next ��ִ��
def buffered_read():
    while True:
        buffer = fetch_big_chunk()
        for small_chunk in buffer:
            yield small_chunk

