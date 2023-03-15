from urllib import parse
import os


def Url():
    try:
        print('——————————————————————————————————————————————————————————————————————————————')
        print('选择了URL转换')
        print('——————————————————————————————————————————————————————————————————————————————')
        d = int(input('选择转换的方式: 1.URL解码 2.日志文件转换:'))
        try:
            if d == 1:
                url = input('请输入待解码的数据:')
                print(parse.unquote(url)) 
            if d == 2:
                # 待转换日志文件的位置
                h = input('请输入待转换日志的绝对路径:')
                u = open(h, "r")
                f = u.read()
                url = parse.unquote(f)
                u.close()
                # 转换完成后日志保存位置
                os.chdir('super_tools\save')
                r = input('请输入需要保存的日志名称:')
                r = '{}{}'.format('../save/', r)
                f = open(r, "w+")
                f.write(url)
                f.close()
        except:
            print('请输入正确的数据!')
    except:
        print('请选择正确的编号!')
