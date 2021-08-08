def knapsack(item,tot,n):
    for i in range(n):
        item[i].append(item[i][-1]/item[i][0])
    item.sort(key=lambda x:x[-1],reverse=True)
    sum=0
    for i in range(n):
        if tot<=0:
            break
        if tot>item[i][0]:
            tot-=item[i][0]
            sum+=item[i][1]
        else:
            sum+=((tot/item[i][0])*item[i][1])
            break
    print(sum)
        
    
        
