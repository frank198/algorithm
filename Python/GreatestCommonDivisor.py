'''
最大公约数


欧几里德算法（Euclidean algorithm） 碾转相除法：
	这条算法基于一个定理：两个正整数a和b（a>b），它们的最大公约数等于a除以b的余数c和b之间的最大公约数。
	比如10和25，25除以10商2余5，那么10和25的最大公约数，等同于10和5的最大公约数。
更相减损术: 两个正整数a和b（a>b），它们的最大公约数等于a-b的差值c和较小数b的最大公约数。
	比如10和25，25减去10的差是15,那么10和25的最大公约数，等同于10和15的最大公约数。
'''

def Euclidean(a, b):
	num1 = a if a >= b else b
	num2 = b if a > b else a
	return EuclideanGCD(num1, num2)

def EuclideanGCD(a, b):
	if a%b == 0:
		return b
	return EuclideanGCD(b, a%b)

'''
更相减损术与移位结合
避免了取模运算, 时间复杂度为O(log(max(a, b)))
'''
def MoreSubtractiveSurgery(a, b):
	if a == b or b == 0:
		return a
	if a == 0:
		return b
	if a < b:
		return MoreSubtractiveSurgery(b, a)
	if a%b == 0:
		return b
	if (not a&1) and (not b&1):
		return MoreSubtractiveSurgery(a>>1, b>>1) << 1
	elif (not a&1) and b&1:
		return MoreSubtractiveSurgery(a>>1, b)
	elif a&1 and (not b&1):
		return MoreSubtractiveSurgery(a, b>>1)
	return MoreSubtractiveSurgery(b, a-b)

print (MoreSubtractiveSurgery(250, 100))

print (MoreSubtractiveSurgery(1000, 1001))