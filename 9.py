y='да'
n='нет'
ans_1=input('Собака короткошерстной породы? ')
if ans_1==y:
    ans_2=input('Рост собаки менее 50 см? ')
    if ans_2==y:
        ans_3=input('У собаки короткий хвост? ')
        if ans_3==y:
            print('английский бульдог')
        else:
            ans_4=input('У собаки длинные уши? ')
            if ans_4==y:
                print('гончая')
            else:
                ans_5=input('У собаки короткое тело? ')
                if ans_5==y:
                    print('мопс')
                else:
                    print('чихуахуа')
    else:
        ans_6=input('Собака весит более 50 кг? ')
        if ans_6==y:
            print('датский дог')
        else:
            print('фоксхаунд')
else:
    ans_2=input('Рост собаки менее 50 см? ')
    if ans_2==y:
        ans_7=input('У собаки доброжелательный характер? ')
        if ans_7==y:
            print('кокер-спаниэль')
        else:
            print('ирландский сеттер')
    else:
        ans_8=input('У собаки рост менее 70 см? ')
        if ans_8==y:
            ans_4=input('У собаки длинные уши? ')
            if ans_4==y:
                print('большой вандейский грифон')
            else:
                print('колли')
        else:
            ans_9=input('Окрас рыжий с белыми отметинами? ')
            if ans_9==y:
                print('сенбернар')
            else:
                ans_10=input('Белоснежный окрас? ')
                if ans_10==y:
                    print('ирландский волкодав')
                else:
                    print('ньюфаундленд')
