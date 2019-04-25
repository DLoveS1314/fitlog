"""
fitlog是一款集成了自动版本管理和自动日志记录两种功能的 Python 包，它可以帮助你在进行实验时方便地保存当前的代码、参数和结果。
fitlog提供给用户的 API 有如下几个：

"""
__all__ = ["commit", "set_log_dir", "finish", "add_best_metric", "add_metric", "add_loss", "add_hyper", "add_other",
           "add_hyper_in_file"]
from .fastlog import logger as _logger
from typing import Union


def commit(file: str, fit_msg: str = None):
    """
    用户用此命令进行自动 commit, 期望的使用方法如下::
        
        import fitlog
        
        fitlog.commit(__file__)
        \"\"\"
        Your training code
        \"\"\"
        fitlog.finish()

    :param file: 以该路径往上寻找.fitlog所在文件夹。一般传入__file__即可
    :param fit_msg: 针对该实验的说明
    """
    _logger.commit(file, fit_msg)


def set_log_dir(log_dir: str):
    """
    设定log 文件夹的路径(在进行其它操作前必须先指定日志路径)。如果你已经顺利执行了 fitlog.commit()命令，
    log 文件夹会自动设定为.fitconfig 文件中的 default_log_dir 字段的值

    :param log_dir: log 文件夹的路径
    """
    _logger.set_log_dir(log_dir)


def finish():
    """
    使用此方法告知 fitlog 你的实验已经顺利结束。你可以使用此方法来筛选出中途关闭的实验。
    """
    _logger.finish()


def add_metric(value: Union[int, str, float, dict], step: int, name: str = None, epoch: int = None):
    """
    用于添加 metric 。用此方法添加的值不会显示在表格中，但可以在单次训练的详情曲线图中查看。

    :param value: 类型为 int, float, str, dict中的一种。如果类型为 dict，它的键的类型只能为 str，
            它的键值的类型可以为int, float, str 或符合同样条件的 dict
    :param step: 用于和 loss 对应的 step
    :param name: 如果你传入 name 参数，你传入的 value 参数会被看做形如 {name:value} 的字典
    :param epoch: 前端显示需要记录 epoch
    :return:
    """
    _logger.add_metric(value, step, name, epoch)


def add_loss(value: Union[int, str, float, dict], step: int, name: str = None, epoch: int = None):
    """
    用于添加 loss。用此方法添加的值不会显示在表格中，但可以在单次训练的详情曲线图中查看。

    :param value: 类型为 int, float, str, dict中的一种。如果类型为 dict，它的键的类型只能为 str，
            它的键值的类型可以为int, float, str 或符合同样条件的 dict
    :param step: 用于和 loss 对应的 step
    :param name: 如果你传入 name 参数，你传入的 value 参数会被看做形如 {name:value} 的字典
    :param epoch: 前端显示需要记录 epoch
    :return:
    """
    _logger.add_loss(value, step, name, epoch)


def add_best_metric(value: Union[int, str, float, dict], name: str = None):
    """
    用于添加最好的 metric 。用此方法添加的值，会被显示在表格中的 metric 列及其子列中。

    :param value: 类型为 int, float, str, dict中的一种。如果类型为 dict，它的键的类型只能为 str，
            它的键值的类型可以为int, float, str 或符合同样条件的 dict
    :param name: 如果你传入 name 参数，你传入的 value 参数会被看做形如 {name:value} 的字典

    .. warning ::
        如果你在同时记录多个数据集上的performance, 请注意使用不同的名称进行区分

    """
    _logger.add_best_metric(value, name)


def add_hyper(value: Union[int, str, float, dict], name=None):
    """
    用于添加超参数。用此方法添加到值，会被放置在表格中的 hyper 列及其子列中

    :param value: 类型为 int, float, str, dict中的一种。如果类型为 dict，它的键的类型只能为 str，
            它的键值的类型可以为int, float, str 或符合同样条件的 dict
    :param name: 如果你传入 name 参数，你传入的 value 参数会被看做形如 {name:value} 的字典
    :return:
    """
    _logger.add_hyper(value, name)


def add_hyper_in_file(file_path: str):
    """
    从文件读取参数。如demo.py所示，两行"#######hyper"之间的参数会被读取出来，并组成一个字典。
    每个变量最多只能出现在一行中，如果多次出现，只会记录第一次出现的值。demo.py::

        from numpy as np
        # do something

        ############hyper
        lr = 0.01 # some comments
        char_embed = word_embed = 300

        hidden_size = 100
        ....
        ############hyper

        # do something
        model = Model(xxx)
  
    如果你把 demo.py 的文件路径传入此函数，会转换出如下字典，并添加到参数中::

        {
            'lr': '0.01',
            'char_embed': '300'
            'word_embed': '300'
            'hidden_size': '100'
        }


    :param file_path: 文件路径
    """
    _logger.add_hyper_in_file(file_path)


def add_other(value: Union[int, str, float, dict], name: str = None):
    """
    用于添加其它参数。用此方法添加到值，会被放置在表格中的 hyper 列及其子列中

    :param value: 类型为 int, float, str, dict中的一种。如果类型为 dict，它的键的类型只能为 str，
            它的键值的类型可以为int, float, str 或符合同样条件的 dict
    :param name: 如果你传入 name 参数，你传入的 value 参数会被看做形如 {name:value} 的字典
    """
    _logger.add_other(value, name)
