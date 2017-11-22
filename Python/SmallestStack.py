
queue = []
minIndex = []

def EeQueue(queueValue):
	queue.append(queueValue)
	if len(minIndex) == 0:
		minIndex.insert(0, len(queue) - 1)
	else:
		i = len(minIndex)-1;
		while (i >= 0):
			if i > 0 and queue[minIndex[i]] < queueValue and queue[minIndex[i - 1]] >= queueValue:
				minIndex.insert(i - 1, len(queue) - 1)
				break
			elif queue[minIndex[i]] >= queueValue:
				minIndex.insert(i + 1, len(queue) - 1)
				break
			elif i == 0:
				minIndex.insert(0, len(queue) - 1)
				break
			i = i - 1

def DeQueue(queueValue):
	if len(queue) <= 0:
		return
	index = queue.index(queueValue);
	if index >= 0:
		queue.remove(queueValue);
		minIndex.remove(index);
		i = len(minIndex)-1;
		while (i >= 0):
			if minIndex[i] > index:
				minIndex[i] = minIndex[i] - 1
			i = i - 1

def Min():
	if len(minIndex) <= 0:
		return
	index = minIndex[len(minIndex) - 1]
	minValue = queue[index]
	DeQueue(minValue)
	return minValue;

def Max():
	if len(minIndex) <= 0:
		return
	index = minIndex[0]
	maxValue = queue[index]
	DeQueue(maxValue)
	return maxValue;


EeQueue(2);
print (queue);
EeQueue(3);
EeQueue(1);
EeQueue(5);
print (queue);
print (Min());
print (Min());
print (Min());
print (Min());
print (Min());
