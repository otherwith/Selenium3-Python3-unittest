import os,configparser

def project_path():
    """
    获取项目路径
    :return:
    """
    return os.path.split(os.path.realpath(__file__))[0].split('Common')[0]

def config_url():
    """
    获取config.ini文件中的testUrl
    :return:
    """
    config = configparser.ConfigParser()
    config.read(project_path() + 'config.ini')
    return config.get('testUrl','url')

if __name__ == '__main__':
    print(project_path())
    print(config_url())