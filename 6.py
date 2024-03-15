first_team,second_team=map(int,input().split(':'))
if first_team>second_team:
    print(1)
elif first_team<second_team:
    print(2)
else:
    print(0)