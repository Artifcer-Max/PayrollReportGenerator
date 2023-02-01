import csv

def getAllPay(rows):
  index = 0
  pay = 0
  for x in rows:
    pay = pay + float(rows[index][3])
    index = index + 1
  print(f"Total Payroll: ${pay:,}")
  return pay

def totalRecords(rows):
  total = 0
  for x in rows:
    total = total + 1
  print(f"Number on payroll: {total}")
  return total

def avgPay(pay, record):
  avg = float(format(pay / record, '.2f'))
  print(f"Average pay: ${avg:,}")
  return avg

def indivPay(employees):
  manager = 0
  sales = 0
  admin = 0
  index = 0
  for x in employees:
    if employees[index][2] == "Manager":
      manager = float(format(float(manager) + float(employees[index][3]), '.2f'))
      index = index + 1
    elif employees[index][2] == "Sales":
      sales = float(format(float(sales) + float(employees[index][3]), '.2f'))
      index = index + 1
    else:
      admin = float(format(float(admin) + float(employees[index][3]), '.2f'))
      index = index + 1
  print("Total pay for:")  
  print(f"Managers: ${manager:,}")
  print(f"Sales: ${sales:,}")
  print(f"Admin: ${admin:,}")
  return manager, sales, admin

def createReport(totalpay, record, avg, individualpay):
  with open("PayrollReport.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Total Payroll", totalpay])
    writer.writerow(["Number on Payroll", record])
    writer.writerow(["Average Pay", avg])
    writer.writerow(["Total pay for:"])
    writer.writerow(["Managers", individualpay[0]])
    writer.writerow(["Sales", individualpay[1]])
    writer.writerow(["Admin", individualpay[2]])







rows = []
with open("employees_(1).csv", "r") as file:
  csvreader = csv.reader(file)
  header = next(csvreader)
  for row in csvreader:
    rows.append(row)
totalpay = getAllPay(rows)
record = totalRecords(rows)
avg = avgPay(totalpay, record)
print()
individualpay = indivPay(rows)
createReport(totalpay, record, avg, individualpay)
