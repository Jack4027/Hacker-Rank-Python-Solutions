def maxArea(w,h,isVertical,distance):
    count =0
    editedH = False

    for i in range (len(isVertical)):
        if isVertical[i]==True and count==0:
            maxArea = h * max(w-distance[i],distance[i])
            Vline = distance[i]
        elif isVertical[i]==False and count ==0:
            maxArea = w * max(h-distance[i],distance[i])
            editedH=True
            Hline = distance[i]
        elif isVertical[i]==True and count ==1:
            if editedH ==True:
                bestW = max(w-distance[i],distance[i])
                maxArea = bestW * max(h-Hline,Hline)
            else:
                lesser, larger = min(Vline,distance[i]),max(Vline,distance[i])
                maxArea = h * max(w-larger,larger-lesser,lesser)

        elif isVertical[i]==False and count ==1:
            if editedH ==True:
                lesser, larger = min(Hline,distance[i]),max(Hline,distance[i])
                maxArea = w * max(h-larger,larger-lesser,lesser)
            else:
                bestW = max(w-Vline,Vline)
                maxArea = bestW * max(h-distance[i],distance[i])
        print(maxArea)
        count+=1

if __name__=='__main__':
    w = 4
    h = 4
    isVertical = [1,0]
    distance = [1,2]

    maxArea(w,h,isVertical,distance)