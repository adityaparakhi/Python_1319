# Data Types in Python

# # int ->> it is one fundamental data types. Values without decimal point is nothing but int. It represents whole no as well as negative numbers.
# price = 100
# runs = 40
# wickets = 0
# temperature = -20


# print("The price is ", price)
# print(type(price))  # print he data type of price of the console, the output is <Class 'int'>
# print(id(price))
# print("The runs are ", runs)
# print(type(runs))  # print he data type of runs of the console, the output is <Class 'int'>
# print(id(runs))
# print("The wickets are ", wickets)
# print(type(wickets))  # print he data type of wickets of the console, the output is <Class 'int'>
# print(id(wickets))
# print("The temperature is ", temperature)
# print(type(temperature))   # print he data type of temperature of the console, the output is <Class 'int'>
# print(id(temperature))





# # float ->> It is fundamental data types. Values with decimal point nothing but float
# petrol_price = 104.56
# overs = 20.2
# balance = 100.4

# print("The petrol price is ", petrol_price)
# print(type(petrol_price))  # print he data type of petrol_price of the console, the output is <Class 'float'>
# print(id(petrol_price))
# print("The overs are ", overs)
# print(type(overs))  # print he data type of overs of the console, the output is <Class 'float'>
# print(id(overs))
# print("The balance is ", balance)
# print(type(balance))  # print he data type of balance of the console, the output is <Class 'float'>
# print(id(balance))






# bool data type (boolean)->> bool is one of fundamental data type. For logical representation of data we use boolean. Values are True and False.  To check the flags  

is_present = True
is_secure = True

print(is_present)
print(type(is_present))
print(id(is_present))
print(is_secure)
print(type(is_secure))
print(id(is_secure))


res = is_present + is_secure    # check that how it get output 2
print(res)   # internal value of True is -> 1 and internal value of False is -> 0 
print(type(res))
print(id(res))

data = float(True)
print(data)