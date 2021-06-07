class logit(object):

    _logfile = 'out.log'

    def __init__(self, function):
        self.function = function

    def __call__(self, *args):
        log_string = self.function.__name__ + " was called"
        print(log_string)

        with open(self.__logfile, 'a') as opened_file:
            opened_file.write(log_string + '\n')
        self.notify()

        return self.function(*args)


    def notify(self):
        pass

logit.__logfile = 'out2.log'
@logit
def myfunction():
    pass

myfunction()