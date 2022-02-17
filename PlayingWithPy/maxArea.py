#distance is units for bottom if not vertical
#distace from the left if vertical
# work out max area after both lines drawn  
def maxArea( w, h, isVertical, distance ):
    shapes = []
    areas = []
    area = w*h
    
    count =0
    for i in range(len(isVertical)):
        if isVertical[i]==0 and count ==0:
            shapes.append([(h-distance[i]),w,False,distance[i]])
            shapes.append([distance[i],w,False,distance[i]])
            areas.append((h-distance[i])*w)
            areas.append(distance[i]*w)
            print(max(areas))
            areas.clear()

        elif isVertical[i]==1 and count ==0:
            shapes.append([h,(w-distance[i]),True, distance[i]])
            shapes.append([h,distance[i],True, distance[i]])
            areas.append(h*(w-distance[i]))
            areas.append(h*distance[i])
            maxArea = max(areas)
            print(maxArea)
            areas.clear()

        elif isVertical[i]==0 and count ==1:
            if shapes[0][2]==False:

                if distance[i] > shapes[0][3]:
                    if distance[i]<h:
                        areas.append((h-distance[i])*w)
                        areas.append((distance[i]-shapes[0][3])*w)
                        areas.append(shapes[0][3]*w)
                        maxArea = max(areas)
                        areas.clear()
                        

                    else:
                        None
                else:
                    areas.append((h-shapes[0][3])*w)
                    areas.append((shapes[0][3]-distance[i])*w)
                    areas.append(distance[i]*w)
                    maxArea = max(areas)
                    areas.clear()
                
                print(maxArea)


            else:
                bestW = max (shapes[0][3], w-shapes[0][3])

                areas.append(bestW*(distance[i]))
                areas.append(bestW*(h-distance[i]))
                maxArea = max(areas)
                areas.clear()
                print(maxArea)


               
        elif isVertical[i]==1 and count ==1:
        
            if shapes[0][2]==False:

                bestH = max (shapes[0][3], h-shapes[0][3])

                areas.append(bestH*(distance[i]))
                areas.append(bestH*(w-distance[i]))
                maxArea = max(areas)
                print(maxArea)


            else:
                if distance[i] > shapes[0][3]:
                    if distance[i]<w:
                        areas.append((w-distance[i])*h)
                        areas.append((distance[i]-shapes[0][3])*h)
                        areas.append(shapes[0][3]*h)
                        maxArea = max(areas)
                        areas.clear()
                        

                    else:
                        None
                else:
                    areas.append((w-shapes[0][3])*h)
                    areas.append((shapes[0][3]-distance[i])*h)
                    areas.append(distance[i]*h)
                    maxArea = max(areas)
                    areas.clear()
                
                print(maxArea)
        count+=1



if __name__ == '__main__':
    w = 4
    h = 4
    isVertical = [1,0]
    distance = [1,1]

    maxArea(w,h,isVertical,distance)