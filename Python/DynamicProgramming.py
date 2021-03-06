'''
动态规划： 最优化原理(principle of optimality)，把多阶段过程转化为一系列单阶段问题，利用各阶段之间的关系，逐个求解，
	- 线性动规
	- 区域动规
	- 树形动规
	- 背包动规
动态规划求解的一般思路
	判断问题的子结构（也可看作状态），当具有最优子结构时，动态规划可能适用。
　　求解重叠子问题。一个递归算法不断地调用同一问题，递归可以转化为查表从而利用子问题的解。分治法则不同，每次递归都产生新的问题。
　　重新构造一个最优解。
备忘录法
1.硬币找零
　　扩展1：单路取苹果
　　扩展2：装配线调度
2.字符串相似度/编辑距离（edit distance）
　　应用1：子串匹配
　　应用2：最长公共子序列
3.最长公共子序列(Longest Common Subsequence,lcs)
　　扩展1：输出所有lcs
　　扩展2：通过LCS获得最长递增自子序列
4.最长递增子序列（Longest Increasing Subsequence,lis）
　　扩展：求解lis的加速
5.最大连续子序列和/积
　　扩展1：正浮点数数组求最大连续子序列积
　　扩展2：任意浮点数数组求最大连续子序列积
6.矩阵链乘法
　　扩展：矩阵链乘法的备忘录解法（伪码）
7.0-1背包问题
8.有代价的最短路径
9.瓷砖覆盖（状态压缩DP）
10.工作量划分
11.三路取苹果
'''