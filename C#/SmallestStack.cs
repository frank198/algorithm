public class SmallestStack 
{
	private List<int> minIndex = new List<int>();
	private List<float> queue = new List<float>();

	public void EeQueue(float queueValue)
	{
		queue.add(queueValue);
		if (minIndex.count == 0)
		{
			minIndex.Insert(0, queue.Count - 1);
		}
		else
		{
			int i = minIndex.Count-1;
			for (; i >= 0; i--) 
			{
				if (i > 0 && queue[minIndex[i]] < queueValue && queue[minIndex[i - 1]] >= queueValue)
				{
					minIndex.Insert(i - 1, queue.Count - 1);
					break;
				}
				else if (queue[minIndex[i]] >= queueValue)
				{
					minIndex.Insert(i + 1, queue.Count - 1);
					break;
				}
				else if (i == 0)
				{
					minIndex.Insert(0, queue.Count - 1);
					break;
				}

			}
		}
	}

	public void DeQueue(float queueValue)
	{
		if (queue.Count <= 0) return;
		int index = queue.findIndex(queueValue);
		if (index >= 0)
		{
			queue.Remove(queueValue);
			minIndex.Remove(index);
			int i = minIndex.length - 1;
			for (i; i >= 0; i--)
			{
				if (minIndex[i] > index)
				{
					minIndex[i] = minIndex[i] - 1;
				}
			}
		}
	}

	public float Min
	{
		get{
			if (queue.Count <= 0) return null;
			int index = minIndex[minIndex.length - 1];
			float minValue = queue[index];
			DeQueue(minValue);
			return minValue;
		}
	}

	public float Max
	{
		get{
			if (queue.Count <= 0) return null;
			int index = minIndex[0];
			float maxValue = queue[index];
			DeQueue(maxValue);
			return maxValue;
		}
	}
}