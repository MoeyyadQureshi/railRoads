# remove warnings
import warnings
warnings.filterwarnings("ignore")

from sklearn.cluster import KMeans
from collections import Counter

def prediction(user_decisions):  
    #IMPORTANT: Number of clusters
    k = 2
    
    #DATA
    clf = KMeans(n_clusters = k, n_init=100)
    data_stats = [[1,1,1],[1,2,1],[2,1,1],[2,2,1],[7,7,7],[7,8,7],[8,7,7]]
    data_decisions = [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [3, 3, 3, 3], [1,1,3,3], [1,1,3,3]]
    
    #Fits classifer wuth the status
    clf.fit(data_stats)
    
    #Creates clusters
    groups = clf.predict(data_stats)
    
    #Temp variables to be used in calculations
    stats_temp = []
    decisions_temp = []
    
    group_stats = []
    group_decisions = []
    temp_list = []
    temp_list2 = []
    temp_mean = 0
    
    for i in range(k): #For each cluster.....
        for j in range(len(groups)): #Place the stats and decisions of one cluster into temp lists
            if (groups[j] == i):
                stats_temp.append(data_stats[j])
                decisions_temp.append(data_decisions[j])
        
        for j in range(len(stats_temp[0])): #Calculate average stats of one cluster and append to group_stats
            for k in range(len(stats_temp)):
                   temp_mean = temp_mean + stats_temp[k][j]
            temp_list.append(temp_mean / len(stats_temp))
            temp_mean = 0
        group_stats.append(temp_list)
        temp_list = []
        
        for j in range(len(decisions_temp[0])): #Calculates mode of decisions of one cluster and append to group_decisions
            for k in range(len(decisions_temp)):
                temp_list.append(decisions_temp[k][j])
            
            temp_mode = Counter(temp_list)
            temp_list2.append(temp_mode.most_common(1)[0][0])
            
            temp_list = []
        group_decisions.append(temp_list2)
        
        #Clears variables so that they can be reused for next cluster calculations
        temp_list2 = []    
        decisions_temp = []
        stats_temp = []
        temp_list = []
    
    #PRINTS CLUSTER MODE OF DECISIONS AND AVERAGE STATS
    #print group_stats
    #print group_decisions
    
    #List to store user predictions
    user_pred = []
    
    #Creates list to be used to match user decisions to a cluster
    compare = []
    for i in range (len(group_decisions)):
        compare.append(0)
    
    #Looks for most similar mode of decisions of a cluster 
    for i in range (len(user_decisions)):
        for j in range (len(group_decisions)):
            if (user_decisions[i] == group_decisions[j][i]):
                compare[j] = compare[j] + 1
    
    #Finds most similar mode of decisions and stats that the average stats of that cluster as the user stats prediction         
    m = max(compare)
    for i in range (len(compare)):
            if (compare[i] == m):
                user_pred.append(group_stats[i])
                break

    return user_pred

            
