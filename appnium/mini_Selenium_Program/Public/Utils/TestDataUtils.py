import json
import pandas as pd


class DataController:
    """
       读取excel文件的内容并转化为json格式
    """
    @staticmethod
    def read_excel(filename):
        list_ = []
        data_ = pd.read_excel(filename)
        for i in range(data_.size):
            for j in data_.loc[:, [data_.columns[i]]].values:
                json_ = {data_.columns[i]: j.tolist()}
                data___ = json.dumps(json_)
                list_.append(data___)

        return list_
    """
      读取json里面值
    """
    @staticmethod
    def read_json(list_, columnsName):
        for i in list_:
            da = json.loads(i)
            for j in da.keys():
                if j == columnsName:
                    return da.get(columnsName)


