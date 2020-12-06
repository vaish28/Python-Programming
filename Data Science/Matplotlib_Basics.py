
import matplotlib.pyplot as plt
import csv


gold = [] #list for gold medals
silver = [] #list for silver medals
bronze=[] #list for bronze medals
country=[] #list for the names of country

with open('MedalData.csv','r') as csvfile: #reading data from the csvfile
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        countryvar= row[0] #variable for country name
        goldvar = row[1] #variable for value of gold medal
        silvervar = row[2] #variable for value of silver medal
        bronzevar = row[3] #variable for value of bronze medal
        gold.append(goldvar) 
        silver.append(silvervar)
        bronze.append(bronzevar)
        country.append(countryvar)


for i in range(0, len(gold)): #converting string value of gold medals to integer type
    gold[i] = int(gold[i])

for i in range(0, len(silver)): #converting string value of silver medals to integer type
    silver[i] = int(silver[i])

for i in range(0, len(bronze)): #converting string value of bronze medals to integer type
    bronze[i] = int(bronze[i])


sum=[] # sum list for total number of medals earned by country
length=len(country)
for i in range(0,length):
    sum.append(gold[i]+silver[i]+bronze[i]) #calculating total number of medals by specific country


ans='y'
while ans=='y' :

    print(" ")
    print ("------------------")
    choice=int(input("1)Line Plot \n2)Scatter Plot \n3)Bar Plot \n4)Total medals earned by each country \n5)Display max medal \n6)Display min medal \n7)Search by country for the number of medals \n"))
    print ("------------------")
    if choice==1:
        plt.xticks(range(6),country)
        plt.plot(gold ,'r-', label= "Gold medals", marker='o',linewidth=3.5,markersize=10) # plot of gold medals
        plt.plot(silver ,'b-', label= "Silver medals", marker ='X',linewidth=3.5,markersize=10) # plot of silver medals
        plt.plot(bronze ,'g-', label= "Bronze medals", marker= 'D',linewidth=3.5,markersize=10) # plot of bronze medals
        plt.legend(loc= 'best') # location of legend
        plt.xlabel('Country') # naming the x axis
        plt.ylabel('Medal') # naming the y axis
        plt.title('Country-wise Medal Count') # giving a title to my graph
        plt.show() # function to show the plot

    if choice == 2:
        plt.scatter(country, gold, label= "gold medals", color= "green", marker= "*",alpha=0.99,linewidth=7) # plot of gold medals
        plt.scatter(country, silver, label= "silver medals", color= "blue", marker= ".",alpha=0.99,linewidth=7) # plot of silver medals
        plt.scatter(country, bronze, label= "bronze medals", color= "red", marker= "+",alpha=0.99,linewidth=7) # plot of bronze medals
        plt.legend(loc='best')  # location of legend
        plt.xlabel('Country') # naming the x axis
        plt.ylabel('Medal') # naming the y axis
        plt.show() # function to show the plot

    if choice ==3:
        plt.bar(country,gold,label="gold medals",color="blue",width=0.5,alpha=0.5) # plot of gold medals
        plt.bar(country,silver,label="silver medals",color="green",width=0.5,alpha=0.5) # plot of silver medals
        plt.bar(country,bronze,label="bronze medals",color="red",width=0.5,alpha=0.5) # plot of bronze medals
        plt.legend(loc="best") # location of legend
        plt.xlabel('Country') # naming the x axis
        plt.ylabel('Medal') # naming the y axis
        plt.show() # function to show the plo

    if choice==4:
        length=len(country) # length of the country list
        for i in range(0,length): # sum of the medal count
            print("For country: ",country[i]," : the sum of the medals is ",sum[i])

    if choice ==5:
        print("The maximum number of medals won by country is : ",max(sum))  # max number of medal count
        j=sum.index(max(sum)) #index of the country having maximum number of medals 
        print("Country : ", country[j])

    if choice ==6:
        #print(sum)
        print("The minimum number of medals won by country is : ",min(sum)) #min number of the medal count
        j=sum.index(min(sum)) #index of the country having minimum number of medals
        print("Country : ", country[j])

    if choice == 7:
        print("The countries are : \n", country, " \n Select one country :")
        name = input("Enter the name of the country : ") #name of the country for displaying the number of medals
        j = country.index(name)
        medal=input("Enter the name of the medal (gold,silver,bronze) : ") # gold silver or bronze for the number of the medals category
        if medal=='gold':
            print("The number of gold medals are : ",gold[j])
        elif medal=='silver':
            print ("The number of silver medals are : ",silver[j])
        elif medal=='bronze':
            print ("The number of bronze medals are : ",bronze[j])

    ans=input("\nDo you want to continue? y/n : ") # loop for displaying other data
     

      
