# 数值分析

Jiaqi Z.

## 课程介绍
数值分析是研究各种数学问题求解的数值计算方法. 在电子计算机称为数值计算的主要工具以后, 人们迫切要求研究适合于计算机使用的数值计算方法. 通常在计算机解决科学计算问题的过程中, 根据数学模型提出求解的数值计算方法, 直到编写程序上机算出结果, 这一过程是数值分析的研究对象. 因此, 数值分析就是**研究使用计算机解决数学问题的数值方法及其理论**, 它的内容包括函数的数值逼近, 数值微分与数值积分, 非线性方程数值解, 数值线性代数, 微分方程数值解等. 与纯数学不同, 数值分析是将理论与计算密切联系起来, 着重研究数学问题的数值方法及其理论.

概括来说, 数值分析具有如下四个特点:

- **面向计算机**, 要根据计算机特点提供实际可行的有效算法, 即算法只能包括四则运算和逻辑运算.
- **有可靠的理论分析, 能任意逼近并达到精度要求**, 对近似算法要保证收敛性和数值稳定性, 还要对误差进行分析, 这些都是建立在数学基础上.
- **有好的计算复杂性**, 通常包括**时间复杂性**与**空间复杂性**, 即节省时间和存储量, 它关系到算法能否在计算机上实现.
- **有数值实验**, 即任何一个算法都需要通过数值实验证明它是行之有效的.

因此, 在学习时, 还应当有适当的理论分析和计算练习. 同时, 考虑到学习内容, 还应当提前学习有关**微积分**, **线性代数**, **常微分方程**的基本内容.

## 目录

- [X] 第一章 绪论
  - 误差
  - 数值计算的误差估计
  - 算法数值稳定性
  - 数值计算中应该注意的一些原则
- [X] 第二章 插值法
  - 引言
  - Lagrange插值法
  - Newton插值(演示程序暂缺)
  - 等距节点差商公式
  - Hermite插值
  - 分段低次插值
  - 三次样条插值
- [X] 第三章 函数逼近与计算
  - 引言
  - 最佳一致逼近
  - 最佳平方逼近
  - 正交多项式
  - 函数按正交多项式展开
  - 曲线拟合的最小二乘法
- [X] 第四章 数值积分
  - 引言
  - 插值型求积公式
  - Newton-Cotes公式
  - Romberg算法
  - Gauss型求积公式
- [X] 第五章 线性方程组的直接解法
  - Gauss消去法
  - 解三对角方程组的追赶法
  - 矩阵的三角分解法
  - Gauss消去法变形
  - 线性方程组的性态和解的误差估计
- [X] 第六章 线性方程组的迭代解法
  - 一般迭代法
  - Jacobi迭代法
  - Gauss-Seidel迭代法
  - Jacobi迭代法和Gauss-Seidel迭代法收敛性
  - 超松弛法
- [ ] 第七章 非线性方程组求根
- [X] 第八章 常微分方程数值解法
  - 引言
  - Euler方法
  - Runge-Kutta方法
- [X] 附录A 矩阵分析基础
  - 向量范数
  - 矩阵范数
  - 初等矩阵
- [X] 附录B 常见RUnge-Kutta公式
  - 二阶Runge-Kutta方法
  - 三阶Runge-Kutta方法
  - 四阶Runge-Kutta方法

## 关于程序语言

考虑到数值分析是**面向计算机**的课程, 因此在笔记适当地方, 我们添加了一些程序代码以供参考. 这些代码都是已经经过测试的, 目前本笔记所使用的编程语言是**Python**, 这是一个开源的程序语言. 你可以在[Python官网](https://www.python.org/)下载. 

除此之外, 本笔记的后续更新计划也将会考虑以下编程语言:
- C/C++
- MATLAB

注: 程序设计语言种类太多, 我们不可能全面涉及到. 因此, 在这里只选择特定的几个具有代表性的编程语言(数值分析所研究的算法是通用的).

同时, 由于精力有限, 难以全面顾及到. 因此, 如果你愿意基于其他编程语言修改笔记, 欢迎在GitHub上创建分支并提交相应的程序版本(程序名称都已在main分支给定). 根据情况, 将考虑编写其他版本的笔记.

## 关于笔记内的定理证明

由于本人水平有限, 部分定理难以证明(相关证明对于后续学习没有影响), 若你有完善的想法, 请**直接pull requests**


## 参考教材
- 李庆扬,王能超,易大义.数值分析(第5版)[M].武汉:华中科技大学出版社,2018.4
- 孙志忠,袁慰平,闻震初.数值分析(第3版)[M].南京:东南大学出版社,2010.12

## 反馈问题
若发现笔记中有任何问题, 可通过以下任意一种方式联系:
- GitHub的Issue, 这是最直接的方式;
- email, 请发送邮件至zhangjq00@sdust.edu.cn

## 关于本笔记的版权使用说明

- 本笔记可**免费用于学习, 科研等非商业活动**;
- 可以以**非商业目的进行传播**, 但在传播过程中**必须保证笔记内容的完整性**(截止到最新发布时, "笔记"包括但不限于仓库内笔记Latex源码, pdf文件, 演示程序代码等. 下同), 需**保证作者信息完整**, 不得进行修改;
- 本笔记**不可用于任何商业用途**(如确有需要, 需联系作者);
- 除在GitHub仓库以pull request形式进行编辑修改外, **不允许对笔记进行修改并公开传播私自修改版本**(以GitHub仓库版本为标准版本);
- 本笔记著作权归作者(Jiaqi Z.)所有, 对本笔记进行创作的人员也可获得著作权, 其他著作权所有者不得违反上述版权说明;
- 本笔记**如因违反上述说明传播而造成不良影响, 与作者和其他创作者无关**, 特此声明;
- 以上说明解释权归Jiaqi Z.所有, 且如有后续更新, 以GitHub仓库最新版说明为准.

Copyright © 2023 Jiaqi Z. All rights reserved.