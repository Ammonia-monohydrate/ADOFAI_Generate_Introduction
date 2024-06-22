import datetime
import re

p_artist_part = re.compile(r'"artist": ".*"')
p_song_part = re.compile(r'"song": ".*"')
p_author_part = re.compile(r'"author": ".*"')
p_removeHTML = re.compile(r'<.*?>')
print(f'''将按照以下格式输出：

曲师：
歌曲：
谱师：
等级：
击破时间：
下载链接：

''')
while True:
    file_path = input('输入q可以退出\n'  # 获取文件路径
                      '请拖入adofal文件：')
    if len(file_path) >= 2 and file_path[0] == '"' and file_path[-1] == '"':
        file_path = file_path[1:-1]
    if file_path == 'q' or file_path == 'Q':  # 如果输入是q或Q就退出
        break
    try:
        f = open(file_path, encoding='utf-8')  # 打开文件
    except FileNotFoundError:
        print('文件不存在！\n')
        continue
    except PermissionError:
        print('您可能没有权限打开该文件！\n')
        continue
    except OSError:
        print('发生了一些不该发生的错误！\n'
              '1：\n'
              '您给出的文件路径中包含非法字符！\n'
              '应该说，正常的文件路径不应该包含非法字符！\n'
              '2：\n'
              '文件已被占用！\n'
              )
        continue
    except UnicodeDecodeError:
        print('发生了一些不该发生的错误！\n'
              '文件编码错误！\n'
              '有可能，您给出的文件不是adofai文件\n'
              )
        continue
    except Exception:
        print('未知错误！\n')
        continue

    file_contents = ''
    for x in range(10):  # 读取前10行，避免文件过大
        try:
            file_contents += f.readline()
        except UnicodeDecodeError:
            print('在逐行读取时编码错误！\n'
                  '有可能，您给出的文件不是adofai文件\n'
                  )
            continue
    try:  # 获取字段
        song_part = p_song_part.search(file_contents).group()
        artist_part = p_artist_part.search(file_contents).group()
        author_part = p_author_part.search(file_contents).group()
    except AttributeError:
        print('无法在文件中找到相关字段！\n')
        continue
    # 获取字段中的内容，并去除HTML标签
    song = p_removeHTML.sub('', song_part[9:-1])
    artist = p_removeHTML.sub('', artist_part[11:-1])
    author = p_removeHTML.sub('', author_part[11:-1])
    if not any((song, artist, author)):  # 如果内容有的为空，则提示
        print('关卡作者可能未填写部分信息！')
    f.close()
    print(f'曲师：{artist}\n'
          f'歌曲：{song}\n'
          f'谱师：{author}\n'
          f'等级：\n'
          f'击破时间：{datetime.datetime.now().date()}\n'
          f'下载链接：\n'
          )
