def PID(c,controlValue,dt):
    # Aktualnie nie wykorzystywane
    # print c.e
    # c.e=c.ref-controlValue
    # print c.e

    # ograniczenie calki
    if abs(c.u)==c.u_max:
        pass
    else:
        c.calka+=c.e*dt;

    c.u=c.FF+c.K*c.e + c.Ti*c.calka - c.Td*(c.v)

    if c.u>c.u_max:
        c.u=c.u_max
    elif c.u<c.u_min:
        c.u=c.u_min

    c.e_old=c.e

