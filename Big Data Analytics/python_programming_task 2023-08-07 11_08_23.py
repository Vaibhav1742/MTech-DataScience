# Databricks notebook source
n = 4
if n ==2:
    print("prime")
elif

# COMMAND ----------

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


# COMMAND ----------

is_prime(6)

# COMMAND ----------


