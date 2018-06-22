def growingPlant(upSpeed, downSpeed, desiredHeight):
    days_planted = 0
    plant_height = 0
    while plant_height < desiredHeight:
        plant_height += upSpeed
        if plant_height < desiredHeight:
            plant_height -= downSpeed
        days_planted+=1
    return days_planted
