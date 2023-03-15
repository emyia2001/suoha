import re


# 转轮机解密
def Rotor():
    print('——————————————————————————————————————————————————————————————————————————————')
    print('选择了转轮机密码解密')
    print('——————————————————————————————————————————————————————————————————————————————')
    l = input('请输入密码文件路径: ')
    f = open(l, 'r', encoding='utf-8')
    text = f.readlines()


    # 将轮子提取出来放入data列表里面
    data = []
    for i in text:
        code = str(re.findall(r'<(.*?) <', i))
        code = code.strip('\'[]')
        data.append(code)


    c = input('请输入密文: ')
    key = input('请输入密钥: ')
    key = key.split(',') # 将key中的数字存入成为列表


    print('旋转后:')
    a = 0 # 用于指定密文位置
    for i in key:
        number = data[int(i)-1].index(c[a]) # 索引密文在对应行数的位置
        a += 1
        data[int(i)-1] = data[int(i)-1][number:] + data[int(i)-1][:number] # 将指定行数中的密文提取首行
        print(data[int(i)-1])


    print('\n按列读取:')
    for i in range(len(data[0])):
        print('第{}列:'.format(i), end='')
        strd = ''
        for j in key:
            strd+=data[int(j)-1] # 提取指定行数中的指定字符串
        print(strd.lower())
