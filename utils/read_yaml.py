import yaml
import os

def read_yaml(test_data_path):
    case = [] #存储测试用例名称
    http = [] #存储请求对象
    expected = [] #存储预期结果
    if os.name == 'posix':#返回当前操作系统的类型，当前只注册了3个值：分别是posix , nt , java， 对应linux/windows/java虚拟机
        #获取测试文件
        file = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + test_data_path.replace('../','/')#os.path.abspath(__file__) 获取脚本完整路径
        print(">>>>>>>>>>>>>>>>>>"+file)
        with open(file,encoding='utf-8') as f:
            dat = yaml.load(f.read(),yaml.SafeLoader)
            test = dat['tests']
            for td in test:
                case.append(td.get('case',''))#如果键不在字典中返回设置的默认值
                http.append(td.get('http',{}))
                expected.append(td.get('expected',{}))
    else:
        with open(test_data_path,encoding='utf-8') as f:
            dat = yaml.load(f.read(),yaml.SafeLoader)
            test = dat['tests']
            for td in test:
                case.append(td.get('case',''))
                http.append(td.get('http',{}))
                expected.append(td.get('expected',{}))


    paramters = zip(http,expected)
    return case,paramters
# if __name__ == '__main__':
#     case,params=read_yaml("data/encodeApi.yaml")
#     print(case)
#     print(list(params))