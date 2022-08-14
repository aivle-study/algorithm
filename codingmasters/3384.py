n = int(input())
square = [list(map(int, input().split())) for _ in range(n)]

area = -1
n1, n2 = 0, 0

for i in range(n-1):
    inter_area, union_area = 0, 0
    min_x1, min_y1 = square[i][0], square[i][1]
    max_x1, max_y1 = square[i][0]+square[i][2], square[i][1]+square[i][3]
    
    for j in range(i+1,n):
        
        min_x2, min_y2 = square[j][0], square[j][1]
        max_x2, max_y2 = square[j][0]+square[j][2], square[j][1]+square[j][3]
        
        intersection_x = min(max_x1, max_x2) - max(min_x1, min_x2)
        intersection_y = min(max_y1, max_y2) - max(min_y1, min_y2)
        
        if intersection_x >= 0 and intersection_y >= 0:
            inter_area = intersection_x * intersection_y
        else:
            inter_area = 0
        
        union_area = (max_x1-min_x1)*(max_y1-min_y1) + (max_x2-min_x2)*(max_y2-min_y2) - inter_area
        area_temp = inter_area / union_area

        if area_temp > area: 
            area = area_temp
            n1, n2 = i+1, j+1
            
print(n1, n2)