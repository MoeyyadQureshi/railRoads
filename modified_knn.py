#Data
db_stats = [[5, 3, 8, 9, 4], [3, 4, 8, 9, 9], [4, 4, 5, 4, 2,], [6, 7, 3, 9, 3], [4, 6, 8, 3, 5]]
db_decisions = [[2, 2, 2, 2], [1, 3, 2, 1], [1, 3, 4, 2], [3, 1, 1, 1], [2, 3, 2, 1]]
user_decisions = [3, 1, 4, 2]
user_stats_pred = []

### IMPORTANT: Value of k for k-NN ### 
k = 3

#Lists to be used to find k-NNs
compare = []
nn = []

#Establishes the list to be used for comparing user decisions to previous players
for i in range (len(db_decisions)):
    compare.append(0)

#Compares user decisions to previous players
for i in range (len(user_decisions)):
    for j in range (len(db_decisions)):
        if (user_decisions[i] == db_decisions[j][i]):
            compare[j] = compare[j] + 1


#Finds most similar decision(s) from previous players 
m = max(compare)

#finds k number of NNs
k_count = 0
while (k_count < k):
    for i in range (len(compare)):
        if (compare[i] == m):
            nn.append(i)
            k_count = k_count + 1
    m = m-1

temp = 0 
for i in range(len(db_stats[0])):
    for j in range(k_count):
        temp = temp + db_stats[nn[j]][i]
    user_stats_pred.append(temp/k_count)
    temp = 0

print user_stats_pred
    
    
            
            
            