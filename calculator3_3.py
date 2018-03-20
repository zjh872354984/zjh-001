import sys
import csv
class Args(object):
    
    def __init__(self):
        self.args = sys.argv[1:]
    def para_read(self):
        dic_config = {}
        try:
            if len(self.args) != 6:
                print("Para Error")
            index = self.args.index('-c')
            #print(index)
            configfile = self.args[index+1]
            dic_config.update({'-c':configfile}) 
            index = self.args.index('-d')
            #print(index)
            configfile = self.args[index+1]
            dic_config.update({'-d':configfile}) 
            index = self.args.index('-o')
            #print(index)
            configfile = self.args[index+1]
            dic_config.update({'-o':configfile}) 
            ##print(configfile)
            return dic_config
        except:
            print("Parameter error")

class Config(object):
    def __init__(self, configpath):
        self.config = configpath
    def get_config(self, x):
        config = {}
        with open(self.config) as file:
            for line in file:
                #print(line)
                line_re = line.replace(" ","") 
                #print(line_re)
                line_st = line_re.strip()
                #print(line_st)
                line_sp = line_st.split('=')
                #print(line_sp)
                config.update({line_sp[0]:line_sp[1]})
            #print(config)
        return config[x]
    def tax_calc(self):
        jishul = float(self.get_config('JiShuL'))
        jishuh = float(self.get_config('JiShuH'))
        yanglao = float(self.get_config('YangLao'))
        yiliao = float(self.get_config('YiLiao'))
        shiye = float(self.get_config('ShiYe'))
        gongshang = float(self.get_config('GongShang'))
        shengyu = float(self.get_config('ShengYu'))
        gongjijin = float(self.get_config('GongJiJin'))
        tax_total = yanglao + yiliao + shiye + gongshang + shengyu + gongjijin
        #print(tax_total)
        return tax_total

class UserData(object):
    def __init__(self, userdatapath):
        self.userdata = userdatapath
    def get_user_data(self,y):
        userdata = {}
        with open(self.userdata) as file:
            for line in file:
                #print(line)
                line_re = line.replace(" ","") 
                #print(line_re)
                line_st = line_re.strip()
                #print(line_st)
                line_sp = line_st.split(',')
                #print(line_sp)
                userdata.update({line_sp[0]:line_sp[1]})
        print(userdata)
        return userdata[y]  

    def calculator(self):
        shebao_dict = {}
        tax_dict = {}
        salary_dict = {}
        income_dict = {}
        baobiao_list = []
        for key_u,value_u in userdata.items():
            ud_k = int(key_u)
            salary = float(value_u)
            if salary < jishul:
                jishu = jishul
            elif salary > jishuh:
                jishu = jishuh
            else:
                jishu = salary 
            
            shebao = jishu * tax_total
            tax0 = salary - shebao -3500
            if tax0<=0:
                tax0 = 0
                tax = 0
            elif tax0<=1500:
                tax = tax0 * 3/100 - 0
            elif tax0<=4500:
                tax = tax0 * 10/100 - 105
            elif tax0<=9000:
                tax = tax0 * 20/100 - 555
            elif tax0<=35000:
                tax = tax0 * 25/100 - 1005
            elif tax0<=55000:
                tax = tax0 * 30/100 - 2755
            elif tax0<=80000:
                tax = tax0 * 35/100 - 5505
            else:
                tax = tax0 * 45/100 - 13505
            shebao_dict[ud_k] = format(shebao,'0.2f')
            tax_dict[ud_k] = format(tax,'0.2f')
            income = salary - tax - shebao
            income_dict[ud_k] = format(income, '0.2f')
            salary_dict[ud_k] = format(salary, '0.2f')
           
            baobiao_list.append(ud_k,salary_dict[ud_k],shebao_dict[ud_k],
                                tax_dict[ud_k],income_dict[ud_k])
        print(baobiao_list)

  
            

if __name__ == '__main__':
    args = Args()
    configfile = args.para_read()
    #print(configfile)
    #print(type(configfile))
    config_c = configfile['-c']
    config_d = configfile['-d']
    config_o = configfile['-o']
    #print(config_c)
    config = Config(config_c)
    config_r = config.get_config('JiShuL')
    print(config_r)
    tax_total = config.tax_calc()
    print(tax_total)
    userdata = UserData(config_d)
    userdata_r = userdata.get_user_data('101')
    print(userdata_r)
    baobiao = userdata.calculator()
