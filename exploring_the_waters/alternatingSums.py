def alternatingSums(a):
    team_1 = a[0::2]
    team_2 = a[1::2]
    team_1_weight = sum(team_1)
    team_2_weight = sum(team_2)
    return [team_1_weight, team_2_weight]
