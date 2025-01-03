
# 字符串变成字典
def dict_(string):
    s_dist = {}
    i = 0
    for s in string:
        s_dist[i] = s
        i += 1
    # # 将键值对序列转换为列表字典  要是集合字典此处参数为set
    # for k, v in s_dist.items():
    #     print(k)
    return s_dist
