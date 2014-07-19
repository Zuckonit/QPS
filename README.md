#QPS
>    a python qps context manager wrapper

#Usuage
>	```
>	from qps import QPS
>	
>	def add(a, b):
>	    return a+b
>	
>	with QPS(1000, add, 1, 2) as qps:
>	    print qps.qps
>	```


