open_file = open('CupcakeInvoices.csv')

sumTotal = 0
for line in open_file:
    line = line.rstrip('/n').split(',')
    n = float(line[3])
    p = float(line[4])
    q = n * p
    sumTotal += q
  
   
   
print(sumTotal)





open_file.close()