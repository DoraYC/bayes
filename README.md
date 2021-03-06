
# 基于概率论的分类方法： 朴素贝叶斯


## 基于贝叶斯决策理论的分类方法

### 朴素贝叶斯的优缺点

* 优点
  在数据较少的情况下仍然有效，可以处理多类问题
* 缺点
  对于输入的数据的准备方式比较敏感
* 适用数据类型
  标称型数据

### 贝叶斯决策理论

**贝叶斯决策理论的核心思想：选择具有最高概率的决策**

贝叶斯概率引入先验知识和逻辑推理来处理不确定命题。另一种概率解释称为频数概率(frequency probability)，它只从数据本身获得结论，并不考虑逻辑推理及先验知识。

## 条件概率


## 使用条件概率来分类


## 使用朴素贝叶斯进行文档分类

机器学习的一个重要应用就是**文档的自动分类**。
朴素贝叶斯是贝叶斯分类器的一个扩展，是用于文档分类的常用算法。
### 朴素贝叶斯的一般过程

1. 收集数据：可以使用任何方法
2. 准备数据：需要数值型或者布尔型数据
3. 分析数据：有大量特征时，绘制特征作用不大，此时使用**直方图**效果更好
4. 训练算法：计算不同的独立特征的条件概率
5. 测试算法：计算错误率
6. 使用过算法：一个常见的朴素贝叶斯应用是文档分类。可以在任意的分类场景中使用朴素贝叶斯分类器，不一定非要是文本。

  
**我们称之为“朴素”，是因为整个形式化过程只做最原始、最简单的假设。**

“朴素”的含义：假设特征之间相互独立。朴素贝叶斯分类器中的另一个假设是每个特征同等重要。

