import os 
import csv

# Set the path for the csv file where the data set is laid

csvpath = os.path.join('.','Resources','budget_data.csv')

# Opens up the file for that path utilizing "," as a delimeter for each column and skips the header

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    header = next(csvreader)

# This first loop appends all of the months in the dataset to then print its length to have the total amount of months

    months = []
    total_profit_and_losses = 0

    for row in csvreader:
        months.append(row[0])

# The second loop calculates the net total amount of "Profit/Losses" over the entire period

        total_profit_and_losses += int(row[1])

# The third loop calculates the changes in "Profit/Losses" for each month and append them into a list
        
# Reopens the file once again to utilize a different loop
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    header = next(csvreader)

    change_per_period = 0
    previous_row = 0
    change_list = []
    total = 0

    for row in csvreader:
        if previous_row != 0:
            change_per_period = int(row[1]) - int(previous_row)
            change_list.append(change_per_period)
            previous_row = row[1]

        else: 
            previous_row = row[1]   
     
# The fourth loop adds all the items in the list that stores the changes for each period 
# and then calculates the average for the whole period
            
    for number in change_list:
        total += int(number)
        
    average = round((total/len(change_list)),2)

# The fifth loop creates a dictionary for each month (Keys) and its corresponding change in profit (Values) 
# and then finds the greatest increase and greatest decrease in profit with its corresponding period
    
    greatest_increase = 0
    greatest_decrease = 0
    month_greatest_increase = ''
    month_greatest_decrease = ''

# Creates a dictionary by fusing the list of months and the list of change in profits
    months_and_changes = dict(zip(months[1:], change_list)) 

    for month, change in months_and_changes.items():
        if change > greatest_increase:
            greatest_increase = change
            month_greatest_increase = month

        if change < greatest_decrease:
            greatest_decrease = change
            month_greatest_decrease = month

# Printing
            
print("Financial Analysis")

print("-----------------------")

# Print total months calculated in the first loop
print(f"Total Months: {len(months)}")

# Print net total amount of profit/losses calculated in the second loop 
print(f"Total: ${total_profit_and_losses}")

# Print the changes in profit/losses over the entire period and the average of those changes calculated in the third and fourth loop
print(f"Changes in profit/losses over the entire period: ${total}")
print(f"Average Change: ${average}")

# Print the greatest increase and greatest decrease in profit for its corresponding period calculated in the fifth loop
print(f"Greatest Increase in Profits: {month_greatest_increase} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {month_greatest_decrease} (${greatest_decrease})")



# Exporting Results

# Set path for output file
output_txt = os.path.join(".","Analysis","Analysis.txt")

# Open the output file
with open(output_txt,'w') as txtfile:

    # Printing
                
    txtfile.write("Financial Analysis\n")

    txtfile.write("-----------------------\n")

    # Print total months calculated in the first loop
    txtfile.write(f"Total Months: {len(months)}\n")

    # Print net total amount of profit/losses calculated in the second loop 
    txtfile.write(f"Total: ${total_profit_and_losses}\n")

    # Print the changes in profit/losses over the entire period and the average of those changes calculated in the third and fourth loop
    txtfile.write(f"Changes in profit/losses over the entire period: ${total}\n")
    txtfile.write(f"Average Change: ${average}\n")

    # Print the greatest increase and greatest decrease in profit for its corresponding period calculated in the fifth loop
    txtfile.write(f"Greatest Increase in Profits: {month_greatest_increase} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {month_greatest_decrease} (${greatest_decrease})\n")

