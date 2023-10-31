def abbr(state):
    d = {
        'Alab':'AL', 'Alas':'AK', 'Ari':'AZ', 'Arka':'AR', 'Cal':'CA', 'Columbia':'DC',
        'Con':'CT', 'Del':'DE', 'Flo':'FL', 'Geo':'GA', 'Haw':'HI', 'Ida':'ID',
        'Ill':'IL', 'Indi':'IN', 'Iow':'IA', 'Kan':'KS', 'Ken':'KY', 'Lou':'LA',
        'Main':'ME', 'Mary':'MD', 'Mas':'MA', 'Mich':'MI', 'Minn':'MN', 'Misso':'MO',
        'Missi':'MS', 'Mon':'MT', 'Neb':'NE', 'Nev':'NV', 'New H':'NH', 'New J':'NJ',
        'New M':'NM', 'New Y':'NY', 'North C':'NC', 'North D':'ND', 'Ohio':'OH',
        'Okl':'OK', 'Ore':'OR', 'Penn':'PA', 'Rho':'RI', 'South C':'SC', 'South D':'SD',
        'Tenn':'TN', 'Tex':'TX', 'Uta':'UT', 'Ver':'VT', 'Virgin Islands':'VI',
        'Virgi':'VA', 'Wash':'WA', 'West':'WV', 'Wis':'WI', 'Wyo':'WY',
        'American':'AS', 'Gua':'GU', 'Nort':'MP', 'Puer':'PR'
    }
    for k in d.keys():
        if k in state:
            return d[k]
    return "US"


# Examples
print(abbr("Texas")) # Output should be 'TX'