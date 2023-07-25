import pandas as pd
import os
from pandasql import sqldf
data =pd.read_csv('G:\Downloads\\transaction.csv', skipfooter=2, engine='python')

#where clause - records with transaction_amount>3000
task1="select * from data where transaction_amount>3000"
print(sqldf(task1, globals()))

#group by clause - sum of transaction amount per transaction type
task2="select transaction_type,sum(transaction_amount) from data group by transaction_type"
print(sqldf(task2, globals()))

#case statement
task3="select *, transaction_type,case when transaction_type ='DEPOSIT' then 'D' else 'W' end as t_type from data "
print(sqldf(task3, globals()))