import base64
import base36
import base91
import os

def Base():
    try:
        print('——————————————————————————————————————————————————————————————————————————————')
        print('选择了base家族的编码与解码, 目前有: base64, base32, base16, base85, base36, base91')
        print('——————————————————————————————————————————————————————————————————————————————')
        s = int(input('1.编码 2.解码 3.指定编码进行反复解码 4.将base64以字节流方式写入文件:'))


        if s == 1:
            M = input('输入明文:')
            print('——————————————————————————————————————————————————————————————————————————————')
            base64_en = base64.b64encode(M.encode('utf-8'))
            print('base64后的编码:', str(base64_en, 'utf-8'))
            print('——————————————————————————————————————————————————————————————————————————————')
            base32_en = base64.b32encode(M.encode('utf-8'))
            print('base32后的编码:', str(base32_en, 'utf-8'))
            print('——————————————————————————————————————————————————————————————————————————————')
            base16_en = base64.b16encode(M.encode('utf-8'))
            print('base16后的编码:', str(base16_en, 'utf-8'))
            print('——————————————————————————————————————————————————————————————————————————————')
            base85_en = base64.b85encode(M.encode('utf-8'))
            print('base85后的编码:', str(base85_en, 'utf-8'))
            print('——————————————————————————————————————————————————————————————————————————————')
            base36_en = base36.loads(M)
            print('base36后的编码:', base36_en)
            print('——————————————————————————————————————————————————————————————————————————————')
            base91_en = base91.encode(M.encode('utf-8'))
            print('base91后的编码:', base91_en)
            print('——————————————————————————————————————————————————————————————————————————————')
        if s == 2:
            c = input('请输入密文:')
            print('——————————————————————————————————————————————————————————————————————————————')
            try:
                base64_de = base64.b64decode(c)
                print('base64后的明文:', str(base64_de, 'utf-8'))
            except:
                print('该编码不为base64')
            try:
                print('——————————————————————————————————————————————————————————————————————————————')
                base32_de = base64.b32decode(c)
                print('base32后的明文:', str(base32_de, 'utf-8'))
            except:
                print('该编码不为base32')
            try:
                print('——————————————————————————————————————————————————————————————————————————————')
                base16_de = base64.b16decode(c)
                print('base16后的明文:', str(base16_de, 'utf-8'))
            except:
                print('该编码不为base16')
            try:
                print('——————————————————————————————————————————————————————————————————————————————')
                base85_de = base64.b85decode(c)
                print('base85后的明文:', str(base85_de, 'utf-8'))
            except:
                print('该编码不为base85')
            try:
                print('——————————————————————————————————————————————————————————————————————————————')
                base36_de = base36.dumps(int(c))
                print('base536后的明文:', base36_de)
            except:
                print('该编码不为base36')
            try:
                print('——————————————————————————————————————————————————————————————————————————————')
                base91_de = base91.decode(c).decode()
                print('base91后的明文:', base91_de)
            except:
                print('该编码不为base91')
        if s == 3:
            swb = int(input('输入编号指定编码: 1.base16 2.base64 3.base85 4.base91: '))
            print('——————————————————————————————————————————————————————————————————————————————')
            c = input('请输入密文:')
            n = 0
            print('——————————————————————————————————————————————————————————————————————————————')
            print('——————————————————————————————————————————————————————————————————————————————')
            print('——————————————————————————————————————————————————————————————————————————————')
            print('——————————————————————————————————————————————————————————————————————————————')
            if swb == 1:
                while True:
                    try:
                        c = base64.b16decode(c)
                        n += 1
                    except:
                        print('Base16共decode了{0}次, 最终解码结果:'.format(n), end='')
                        print(str(c))
                        break
            if swb == 2:
                while True:
                    try:
                        c = base64.b64decode(c)
                        n += 1
                    except:
                        print('Base64共decode了{0}次, 最终解码结果:'.format(n), end='')
                        print(str(c))
                        break
            if swb == 3:
                while True:
                    try:
                        c = base64.b85decode(c)
                        n += 1
                    except:
                        print('Base85共decode了{0}次, 最终解码结果:'.format(n), end='')
                        print(str(c))
                        break
            if swb == 4:
                while True:
                    try:
                        c = base91.decode(c).decode()
                        n += 1
                    except:
                        print('Base91共decode了{0}次, 最终解码结果:'.format(n), end='')
                        print(str(c))
                        break
        if s == 4:
            c = input('请输入密文:')
            name = input('输入新的文件名:')
            byte_s = base64.b64decode(c)
            os.chdir('super_tools\save')
            f = open(name, 'wb').write(byte_s)
            f.close()
            print('文件保存在:super_tools\save')
            print('请手动根据文件头修改后缀名')
        if s == 5:
            strs = input('请输入密文:')     
            imgdata=base64.b64decode(strs)
            file=open('../1.jpg','wb')
            file.write(imgdata)
            file.close()
            
        if s != 1 and s != 2 and s != 3 and s != 4 and s != 5:
            print('请输入正确的数值')
    except:
        print('请输入正确的数值')

