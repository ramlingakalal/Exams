from area_cir import Are_cirf

def test():
    Area, circle = Are_cirf(2)
    assert round(Area, 2) == 12.57   
    assert round(circle, 2) == 12.57