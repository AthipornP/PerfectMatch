# https://docs.python.org/3/tutorial/errors.html
# https://realpython.com/python-exceptions/
# https://www.datacamp.com/community/tutorials/exception-handling-python
# https://www.youtube.com/watch?v=NIWwJbo-9_8

class NotAllowFileError(Exception):
    def __init__(self, filename):
        self.message = filename + '  is not allowed.'
        super().__init__(self.message)

try:
    # open a file, returns an error if the file does not exist
    f1 = open('neis0736.txt')    
    # create a file, returns an error if the file exist
    f2 = open('abc.txt','x')    
    # Custom exception
    f3 = open('def.txt')
    if f3.name == 'def.txt':
        raise NotAllowFileError(f3.name)
    # general exception
    var = bad_var
except FileNotFoundError as e:
    print(e)
except FileExistsError as e:
    print(e)
except NotAllowFileError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f1.read())
    f1.close()
finally:
    print('End process')