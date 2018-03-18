import sys
class Args(object):
    
    def __init__(self):
        self.args = sys.argv[1:]
    def para_read(self):
        dic_config = {}
        try:
            if len(self.args) != 6:
                print("Para Error")
            index = self.args.index('-c')
            print(index)
            configfile = self.args[index+1]
            dic_config.update({index:configfile}) 
            index = self.args.index('-d')
            print(index)
            configfile = self.args[index+1]
            dic_config.update({index:configfile}) 
            index = self.args.index('-o')
            print(index)
            configfile = self.args[index+1]
            dic_config.update({index:configfile}) 
            print(configfile)
            type(configfile)
            return dic_config
        except:
            print("Parameter error")

if __name__ == '__main__':
    args = Args()
    configfile = args.para_read()
    print(configfile)
    print(type(configfile))
