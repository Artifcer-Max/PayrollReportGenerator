class Employee:
  def __init__(self, empid, name, title, pay):
    self.empid = empid
    self.name = name
    self.title = title
    self.pay = pay
  
  def __str__(self):
    return f"{self.empid} {self.name} {self.title} {self.pay}"

def getEmployeeInfo():
  count = 0  
  employees = []
  for x in file:
    if count == 0:
      empid = x.strip('\n')
      count = count +1
    elif count == 1:
      name = x.strip('\n')
      count = count +1
    elif count == 2:
      title = x.strip('\n')
      count = count +1
    else:
      pay = x.strip("\n")
      emp = Employee(empid, name, title, pay)
      employees.append(emp)
      count = 0
  return employees

def getAllPay(employees):
  index = 0
  pay = 0
  for x in employees:
    pay = pay + float(employees[index].pay)
    index = index + 1
  print(f"Total Payroll: ${pay:,}")
  return pay

def totalRecords(employees):
  total = 0
  for x in employees:
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
    if employees[index].title == "Manager":
      manager = float(format(float(manager) + float(employees[index].pay), '.2f'))
      index = index + 1
    elif employees[index].title == "Sales":
      sales = float(format(float(sales) + float(employees[index].pay), '.2f'))
      index = index + 1
    else:
      admin = float(format(float(admin) + float(employees[index].pay), '.2f'))
      index = index + 1
  print("Total pay for:")  
  print(f"Managers: ${manager:,}")
  print(f"Sales: ${sales:,}")
  print(f"Admin: ${admin:,}")
  return manager, sales, admin

def createReport(totalpay, record, avg, individualpay):
  file = open("PayrollReport.txt", "x")
  text = [f"Total Payroll: ${totalpay:,}", f"\nNumber on payroll: {record}", f"\nAverage pay: ${avg:,}", f"\n", f"\nTotal pay for:", f"\nManagers: ${individualpay[0]:,}", f"\nSales: ${individualpay[1]:,}", f"\nAdmin: ${individualpay[2]:,}"]
  file.writelines(text)
  file.close()

file = open("Employees_(1).txt", "r")
employees = getEmployeeInfo()
totalpay = getAllPay(employees)
record = totalRecords(employees)
avg = avgPay(totalpay, record)
print()
individualpay = indivPay(employees)
createReport(totalpay, record, avg, individualpay)
file.close()