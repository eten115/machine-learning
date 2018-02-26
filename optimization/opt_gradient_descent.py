# coding=utf-8
#

"""
参考代码
http://blog.csdn.net/u014403897/article/details/45246781


梯度下降

输入

n: 特征数
m: 样本数
a: 学习率
t: 迭代次数

2 10 0.01 10

2104 3 399900
1600 3 329900
2400 3 369000
1416 2 232000
3000 4 539900
1985 4 299900
1534 3 314900
1427 3 198999
1380 3 212000
1494 3 242500



输出

t行, 每轮迭代后的 J 值
第 t+1 行,  特征 w0 w1 w2


53052890086.237
51993904900.868
50956770155.817
49941026552.120
48946224657.273
47971924687.609
47017696295.619
46083118362.109
45167778793.089
44271274321.262
30014.457 8183.543 4763.016

"""
import math


def feature_normalization(init_samples):
    """
    特征归一化

    使用标准差法归一化
    """
    avgs = []
    standard_deviation = []
    for i in xrange(len(init_samples[0][1])):
        # avg
        fea_avg = float(sum([features[i] for _, features in init_samples])) / float(len(init_samples))
        avgs.append(fea_avg)

        # standard_deviation
        tmp_sdev = math.sqrt(float(sum([math.pow(features[i] - fea_avg, 2) for _, features in init_samples])) / float(len(init_samples)))
        standard_deviation.append(tmp_sdev)

    print avgs
    print standard_deviation

    ret_samples = []
    norm = lambda x, u, delta: (x - u)/delta

    for y, features in init_samples:
        ret_samples.append([y, [norm(fea, avgs[pos], standard_deviation[pos]) for pos, fea in enumerate(features)]])

    print ret_samples
    return ret_samples


def calc_gradient(alpha):
    """
    计算梯度

    theta = theta - alpha * gradient

    """
    pass


def main(init_samples):
    """
    计算梯度

    最优化问题

    参数迭代

    1. theta = theta - alpha * gradient
    2. loss = sum(math.pow(theta * xi - yi, 2))


    """

    norm_samples = feature_normalization(init_samples)

    # 初始化 w 为 0 向量
    w = [0 for i in xrange(len(norm_samples[0][1]))]

    for iter_i in xrange(100000):

        # loss
        loss = sum(math.pow(sum([x*y for x, y in zip(w, feai)]) - yi, 2) for yi, feai in norm_samples)
        print "iter ", iter_i, w, loss

        # calc gradient
        #
        gradient = []
        sample_num = len(norm_samples)
        for i in xrange(len(norm_samples[0][1])):
            gradient_i = sum([(sum([x*y for x, y in zip(w, feai)]) - yi) * feai[i] for yi, feai in norm_samples]) / sample_num
            gradient.append(gradient_i)

        # change w
        alpha = 0.01
        w = [w - alpha * gradient for w, gradient in zip(w, gradient)]

    pass


if __name__ == '__main__':

    samples = [
        [399900, [2104, 3]],
        [329900, [1600, 3]],
        [369000, [2400, 3]],
        [232000, [1416, 2]],
        [539900, [3000, 4]],
        [299900, [1985, 4]],
        [314900, [1534, 3]],
        [198999, [1427, 3]],
        [212000, [1380, 3]],
        [242500, [1494, 3]]
    ]

    # feature_normalization(samples)

    main(samples)

