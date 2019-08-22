final_result = {}
#子生成器
def sales_sum(pro_name):
	total = 1
	nums = []
	while True:
		#不停的从外界接收值并保存
		x = yield
		print(pro_name+'销量',x)
		if not x:#如果接收到None就结束
			break
		total += x
		nums.append(x)
	return total,nums
	#这个值返回到final_result[key]

#委托生成器
def middle(key):
	while True:
		final_result[key] = yield from sales_sum(key)
		#这里使用yield from 使调用方和被调用方之间启动了一个双向通道
		print(key + '销售统计完成！')

#调用方
def main():
	data_sets = {
		'pr1s0n牌手机':[1899,2210,3321,2314],
		'pr1s0n牌大衣':[123,321,3234],
		'pr1s0n牌冰箱':[1231,3421,432,4231,423]

	}
	for key,data_set in data_sets.items():
		print('Start key:',key)
		m = middle(key)
		m.send(None)#预激
		for value in data_set:
			m.send(value)
		m.send(None)
	print('final_result: ',final_result)	
if __name__ == '__main__':
	main()