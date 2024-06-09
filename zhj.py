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
    if file_path == 'q' or file_path == 'Q':  # 如果输入是q或Q就退出
        break
    try:
        f = open(file_path, encoding='utf-8')  # 打开文件
    except FileNotFoundError:
        print('文件不存在！\n')
        continue
    file_contents = ''
    for x in range(10):  # 读取前10行，避免文件过大
        file_contents += f.readline()
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
