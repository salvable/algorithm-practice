def solution(dirs):
    position = [0,0]
    dataset = set()
    #U,D,R,L
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    for x in dirs:
        if(x == "U"):
            if position[1] + dy[0] <= 5 and position[1] + dy[0] >= -5:
                position[1] += dy[0]
                #갔다가 되돌아오는 양방향을 고려하여 추가 
                dataset.add((position[0],position[1]-dy[0],position[0],position[1]))
                dataset.add((position[0],position[1],position[0],position[1]-dy[0]))
        if(x == "D"):
            if position[1] + dy[1] <= 5 and position[1] + dy[1] >= -5:
                position[1] += dy[1]
                dataset.add((position[0],position[1]-dy[1],position[0],position[1]))
                dataset.add((position[0],position[1],position[0],position[1]-dy[1]))
        if(x == "R"):
            if position[0] + dx[2] <= 5 and position[0] + dx[2] >= -5:   
                position[0] += dx[2]
                dataset.add((position[0]-dx[2],position[1],position[0],position[1]))
                dataset.add((position[0],position[1],position[0]-dx[2],position[1]))
        if(x == "L"):
            if position[0] + dx[3] <= 5 and position[0] + dx[3] >= -5:
                position[0] += dx[3]
                dataset.add((position[0]-dx[3],position[1],position[0],position[1]))
                dataset.add((position[0],position[1],position[0]-dx[3],position[1]))

    #양방향성을 고려해서 나누기2
    return len(dataset)/2
