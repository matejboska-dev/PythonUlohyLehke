import datetime

inp_day = input("V ciselne podobe zadejte den vaseho narozeni: ")
inp_month = input("V ciselne podobe zadejte mesic vaseho narozeni: ")
inp_year = input("V ciselne podobe zadejte rok vaseho narozeni: ")

x = datetime.datetime(inp_year, inp_month, inp_day)

print(x)

print(inp_day + ".", inp_month + ".", inp_year)