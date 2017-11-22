const minIndex = [];
const queue = [];

class SmallestStack
{

	static EeQueue(queueValue)
	{
		queue.push(queueValue);
		if (minIndex.length == 0)
		{
			minIndex.push(queue.length - 1);
		}
		else
		{
			let i = minIndex.length - 1;
			for (i; i >= 0; i--)
			{
				if (i > 0 && queue[minIndex[i]] < queueValue && queue[minIndex[i - 1]] >= queueValue)
				{
					minIndex.splice(i - 1, 0, queue.length - 1);
				}
				else if (queue[minIndex[i]] >= queueValue)
				{
					minIndex.splice(i + 1, 0, queue.length - 1);
					break;
				}
				else if (i == 0)
				{
					minIndex.splice(0, 0, queue.length - 1);
				}
			}
		}
	}

	static DeQueue(queueValue)
	{
		if (queue.length <= 0) return;
		const index = queue.indexOf(queueValue);
		if (index >= 0)
		{
			queue.splice(index, 1);
			let i = minIndex.length - 1;
			for (i; i >= 0; i--)
			{
				if (minIndex[i] > index)
				{
					minIndex[i] = minIndex[i] - 1;
				}
				else if (minIndex[i] == index)
				{
					minIndex.splice(i, 1);
				}
			}
		}
	}

	static get Min()
	{
		if (minIndex.length <= 0) return null;
		const index = minIndex.length - 1;
		const minValue = queue[minIndex[index]];
		SmallestStack.DeQueue(minValue);
		return minValue;
	}

	static get Max()
	{
		if (minIndex.length <= 0) return null;
		const index = 0;
		const maxValue = queue[minIndex[index]];
		SmallestStack.DeQueue(maxValue);
		return maxValue;
	}
}

SmallestStack.EeQueue(2);
SmallestStack.EeQueue(3);
SmallestStack.EeQueue(1);
SmallestStack.EeQueue(5);
console.info(SmallestStack.Min);
console.info(SmallestStack.Min);
console.info(SmallestStack.Min);
console.info(SmallestStack.Min);