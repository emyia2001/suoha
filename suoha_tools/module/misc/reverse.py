#!/usr/bin/env python    
#encoding: utf-8  

# 倒序转换
def Re():
    try:
        print('——————————————————————————————————————————————————————————————————————————————')
        print('选择了倒序转换')
        print('——————————————————————————————————————————————————————————————————————————————')
        d = int(input('选择转换的方式: 1.十六进制反转 2.文件反转:'))
        try:
            if d == 1:
                re1 = input('请输入待反转的数据:')
                reversed_hex_data = re1[::-1]
                print(reversed_hex_data)
            if d == 2:
                # 打开输入文件和输出文件
                h = input("请输入待反转文件的绝对路径:")
                d1 = open(h , 'rb')
                d1.close
                # 读取数据
                data = d1.read()
                # 将数据转换为十六进制字符串
                hex_data = data.hex()
                # 将字符串倒序
                reversed_hex_data = hex_data[::-1]
                # 将倒序的十六进制字符串转换回字节数组
                reversed_data = bytes.fromhex(reversed_hex_data)

                r = input('请输入需要保存的文件名称:')
                r = '{}{}'.format('./save/', r)
                f = open(r , "wb")
                f.write(reversed_data)
                f.close()
                print('——————————————————————————————————————————————————————————————————————————————')

        except:
            print('请输入正确的数据!')
    except:
        print('请选择正确的编号!')

