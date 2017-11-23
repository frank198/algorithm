'''
Aho–Corasick (AC 算法， AC自动机): 多模式匹配算法，字符窜搜索算法
例如：
	出 k 个单词，再给出一段文章（长度是 n），让你找出有多少个单词在文章里出现过。
'''

class Node:
	"""docstring for Node"""
	def __init__(self, nodeValue):
		self.nodeValue = nodeValue #节点值
		self.fail = None             # fail 值
		self.tail = 0
		self.child = []
		self.childValue = []      # 子节点的值

class Tree(object):
	"""docstring for Tree"""
	def __init__(self, arg):
		super(Tree, self).__init__()
		self.arg = arg


class AcMation:
	"""docstring for AcMation """
	def __init__(self):
		self.root = Node("") # 创建字典树根节点
		self.count = 0 # 初始化 模式字符窜个数

	'''
	插入模式字符窜
	'''
	def Insert(self, strKey):
		self.count += 1
		root = self.root
		for i in strKey:
			if i not in root.childValue:
				child = Node(i)
				root.child.append(child)
				root.childValue.append(i)
				root = child
			else:
				root = root.child[root.childValue.index(i)]
		root.tail = self.count

	def AcAutoMation(self):
		queueList = [self.root]
		while len(queueList):
			temp = queueList[0]
			queueList.remove(temp)
			for i in temp.child:
				if temp == self.root:
					i.fail = self.root
				else:
					p = temp.fail
					while p:
						if i.nodeValue in p.childValue:
							i.fail = p.child[p.childValue.index(i.nodeValue)]
							break;
						p = p.fail
					if not p:
						i.fail = self.root
				queueList.append(i)

	def RunkMP(self, strMode):
		p = self.root  
		cnt = {}                                    #使用字典记录成功匹配的状态                               
		for i in strMode:                           #遍历目标串  
		    while i not in p.childValue and p is not self.root:  
		        p = p.fail  
		    if i in p.childValue:                   #若找到匹配成功的字符结点，则指向那个结点，否则指向根结点  
		        p = p.child[p.childValue.index(i)]  
		    else :                                    
		        p = self.root  
		    temp = p  
		    while temp is not self.root:              
		           if temp.tail:                    #尾标志为0不处理           
		               if temp.tail not in cnt:  
		                   cnt.setdefault(temp.tail)  
		                   cnt[temp.tail] = 1  
		               else:  
		                   cnt[temp.tail] += 1  
		           temp = temp.fail  
		return cnt                                  #返回匹配状态  
		
key = ["殷俊","王志青","dai","qww"]        #创建模式串  
acp = AcMation()  
  
for i in key:  
    acp.Insert(i)                           #添加模式串  
import datetime  
  
acp.AcAutoMation()  
  
start = datetime.datetime.now()             #开始时间 
text = "殷王青dahiqwwqww wwqww"
d = acp.RunkMP(text)
print (d)
''''' 
    print (d)                               #打印 
    for i in d.keys(): 
        print(key[i-1],d[i])                #将子串匹配的数量显示 
'''  
end  = datetime.datetime.now()              #结束时的时间  
print ('总共花费时间是:',end - start)       #打印出总共花费时间  