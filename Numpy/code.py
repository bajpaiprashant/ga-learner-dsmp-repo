# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data_file=path
data=np.genfromtxt(data_file, delimiter=",", skip_header=1)
print("\nData: \n\n", data)
print("\nType of data: \n\n", type(data))

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census=np.concatenate((data,new_record),axis=0)
print(census)
#Code starts here



# --------------
#Code starts here
#print(census)
age=np.asarray(census[:,0])
print(age)
max_age=age.max()
min_age=age.min()
age_mean=age.mean()
age_std=np.std(age)
print(max_age  , min_age , age_mean,age_std)




# --------------
#Code starts here
mask_0=(census[:,2].astype(int)==0)
mask_1=(census[:,2]==1)
mask_2=(census[:,2]==2)
mask_3=(census[:,2]==3)
mask_4=(census[:,2]==4)

race_0=census[mask_0]
race_1=census[mask_1]
race_2=census[mask_2]
race_3=census[mask_3]
race_4=census[mask_4]
print(race_0)

len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

print(len_0, len_1,len_2,len_3,len_4)
minority_race=min(len_0,len_1,len_2,3,len_4)
print(minority_race)
#print(census[:,2])

#print(race_0,race_1,race_2,race_3,race_4,len_0)


# --------------
#Code starts here
senior_citizens=census[census[:,0]>60]
senior_citizens_len=len(senior_citizens)

working_hours_sum=sum(senior_citizens[:,6])
print(len(senior_citizens))

avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high=census[census[:,1]>10]
low=census[census[:,1]<=10]

avg_pay_high=(high[:,7]).mean()
avg_pay_low=(low[:,7]).astype(float).mean()

print(avg_pay_high)
print(avg_pay_low)


