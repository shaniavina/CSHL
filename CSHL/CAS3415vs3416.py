import csv

matrix1 = []
with open ("/Users/shanshanli/Desktop/CAS3415.CAS3416.exome_snp_nosy.csv") as f:
    reader1 = csv.reader(f)
    for row1 in reader1:
        matrix1.append(row1)

matrix2 = []
with open ("/Users/shanshanli/Desktop/CAS3415.CAS3417.exome_snp_nosy.csv") as g:
    reader2 = csv.reader(g)
    for row2 in reader2:
        matrix2.append(row2)

with open ("/Users/shanshanli/Desktop/CAS3415.CAS3416.exome_snp_nosyFilter.csv", "wb") as f:
    with open ("/Users/shanshanli/Desktop/CAS3415.CAS3417.exome_snp_nosyFilter.csv", "wb") as g:
        writer1 = csv.writer(f)
        writer2 = csv.writer(g)
        for i in range(len(matrix1)):
            for j in range(len(matrix2)):
                if matrix1[i][21] == matrix2[j][21] and (matrix1[i][22] == matrix2[j][22] or matrix1[i][22] == matrix2[j][23] or matrix1[i][23] == matrix2[j][23] or matrix1[i][23] == matrix2[j][22]):
                    writer1.writerow(matrix1[i])
                    writer2.writerow(matrix2[j])
        
        