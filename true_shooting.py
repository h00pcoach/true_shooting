def true_shooting_percentage(points,fga,fta):     
    ts = points / (2*(fga + 0.44 * fta))    
    return(ts)

print true_shooting_percentage(100,75,10)


