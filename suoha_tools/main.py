from module.crypto.qwe import QWE
from module.crypto.rotor import Rotor
from module.misc.base import Base
from module.crypto.mosi import Mos
from module.misc.converter import Converter
from module.misc.url import Url
from module.misc.reverse import Re
from module.misc.ascii import Ascii

if __name__ == '__main__':
    print('\n用于编码、解码、解密, 目前有: Base家族、转轮机密码、QWE密码、摩斯密码、进制转换器、Url编码、倒序转换、ascii转字符串')
    print('\n#####################################################################################')
    sw = ''
    while sw != 'q':
        sw = input('请选择类型:1.杂项 2.密码学 q.退出程序:')
        print('——————————————————————————————————————————————————————————————————————————————')
        if sw == '1':
            s = input('请选择编码类型:1.base家族 2.进制转换器 3.Url编码 4.倒序转换 5.ascii转字符串:')
            if s == '1':
                Base()
            if s == '2':
                Converter()
            if s == '3':
                Url()
            if s == '4':
                Re()
            if s == '5':
                Ascii()

        if sw == '2':
            s = input('请选择密码类型:1.QWE密码 2.转轮机加密 3.摩斯密码:')
            if s == '1':
                QWE()
            if s == '2':
                Rotor()
            if s == '3':
                Mos()
    print('退出')
