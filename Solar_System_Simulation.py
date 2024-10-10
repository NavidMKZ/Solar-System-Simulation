#Navid Markazi,Isfahan University of Technology,December 2020
from vpython import *
import math
import datetime

scene = canvas(width=1300, height=500)
scene.forward = vector(0,0.5,-0.5)

choose={"choose":0}
graph_choose={"selected":0}
def program_mode(m):
    choose["choose"]=m.index
def graph_planets(m):
    graph_choose["selected"]=m.index
scene.append_to_caption("program modes:")
menu(text="program modes",choices=['','The first four planets','The last five planets','All'],bind=program_mode)
scene.append_to_caption("----Control the page by right-clicking and scroll wheel---\n")
scene.append_to_caption("\t\t\t\t\t\t\t---To change the program mode, close it and run it again---\n")
scene.append_to_caption("Do you want to draw graphs? ")
menu(text="graph",choices=['','Yes','No'],bind=graph_planets)
scene.append_to_caption("\n")
while True:
    rate(1)
    if choose["choose"]!=0 and graph_choose['selected']!=0:
        break
    else:
        pass
scene.append_to_caption("\n")
def runner(r):
    global run
    run=r.checked
checkbox(bind=runner,text='Start',checked=False)
run=False

def Julian_Date(time):          #Calculate the Julian century
    Y,m,D=time.year,time.month,time.day
    J=(365.25*Y)+(30.6001*(m+1))+D+1720994.5+(2-((Y/100)+(Y/400)))
    t=(J-2451545)
    T=t/36525
    list2=POE(T)
    return list2

time=datetime.datetime.now()
def scene_title(time):
    scene.title='Time: '+str(time.year)+'/'+str(time.month)+'/'+str(time.day)

list1=["L","ϖ","Ω"]

def POE(T):          #calculate Planetary Orbital Elements
    g=(4.8481368*0.000001*180/math.pi)
    Mercury_D,Venus_D,Earth_D,Mars_D,Jupiter_D,Saturn_D,Uranus_D,Neptune_D,Pluto_D=0,0,0,0,0,0,0,0,0
    Mercury_D={"a":0.38709893+0.00000066*T,
                "e":0.20563069+0.00002527*T,
                "i":7.00487-23.5*T*g,
                "Ω":48.33167-446.30*T*g,
                "ϖ":77.45645+573.57*T*g,
                "L":252.25084+538101628.29*T*g}
    Venus_D={"a":0.72333199+0.00000092*T,
            "e":0.00677323-0.00004938*T,
            "i":3.39471-2.86*T*g,
            "Ω":76.68069-996.89*T*g,
            "ϖ":131.53298-108.80*T*g,
            "L":181.97973+210664136.06*T*g}
    Earth_D={"a":1.00000011-0.00000005*T,
            "e":0.01671022-0.00003804*T,
            "i":0.00005-46.94*T*g,
            "Ω":-11.26064-18.228*T*g,
            "ϖ":102.94719+1198.28*T*g,
            "L":100.46435+129597740.63*T*g}
    Mars_D={"a":1.82366231-0.00007221*T,
            "e":0.09341233+0.00011902*T,
            "i":1.85061-25.47*T*g,
            "Ω":49.57854-1020.19*T*g,
            "ϖ":336.04084+1560.78*T*g,
            "L":355.45332+68905103.78*T*g}
    Jupiter_D={"a":5.20336301+0.00060737*T,
            "e":0.04839266-0.00012880*T,
            "i":1.30530-4.15*T*g,
            "Ω":100.5615+1217.17*T*g,
            "ϖ":14.75385+839.93*T*g,
            "L":34.40438+10925078.35*T*g}
    Saturn_D={"a":9.53707032-0.00301530*T,
            "e":0.05415060-0.00036762*T,
            "i":2.48446+6.11*T*g,
            "Ω":113.71504-1591.05*T*g,
            "ϖ":92.43194-1948.89*T*g,
            "L":49.94432+4401052.95*T*g}
    Uranus_D={"a":19.9126393+0.00152025*T,
            "e":0.04716771-0.00019150*T,
            "i":0.76986-2.09*T*g,
            "Ω":74.22988+1681.40*T*g,
            "ϖ":170.96424+1312.56*T*g,
            "L":313.23218+1542547.79*T*g}
    Neptune_D={"a":30.06896348-0.00125196*T,
            "e":0.00858587+0.00002514*T,
            "i":1.76917-3.64*T*g,
            "Ω":131.72169-151.25*T*g,
            "ϖ":44.97135-844.43*T*g,
            "L":304.88003+786449.21*T*g}
    Pluto_D={"a":39.48168677-0.00076912*T,
            "e":0.24880766+0.00006465*T,
            "i":17.14175+11.07*T*g,
            "Ω":110.30347-37.33*T*g,
            "ϖ":224.06676-132.25*T*g,
            "L":238.92881+522747.90*T*g}
    list2=[Mercury_D,Venus_D,Earth_D,Mars_D,Jupiter_D,Saturn_D,Uranus_D,Neptune_D,Pluto_D]
    return list2

list_name=["mer","ven","ear","mar","jup","sat","ura","nep","plu"]

pos_d={"mer":{'x':0,'y':0,'z':0},
       "ven":{'x':0,'y':0,'z':0},
       "ear":{'x':0,'y':0,'z':0},
       "mar":{'x':0,'y':0,'z':0},
       "jup":{'x':0,'y':0,'z':0},
       "sat":{'x':0,'y':0,'z':0},
       "ura":{'x':0,'y':0,'z':0},
       "nep":{'x':0,'y':0,'z':0},
       "plu":{'x':0,'y':0,'z':0}}

distance_d={"mer":0,"ven":0,"ear":0,"mar":0,
            "jup":0,"sat":0,"ura":0,"nep":0,"plu":0}

def planet_fun(time):          #Calculate the coordinates of the planets relative to the plane of the zodiac
    list3=Julian_Date(time)
    Mercury_D=list3[0]
    Venus_D=list3[1]
    Earth_D=list3[2]
    Mars_D=list3[3]
    Jupiter_D=list3[4]
    Saturn_D=list3[5]
    Uranus_D=list3[6]
    Neptune_D=list3[7]
    Pluto_D=list3[8]
    list2=[Mercury_D,Venus_D,Earth_D,Mars_D,Jupiter_D,Saturn_D,Uranus_D,Neptune_D,Pluto_D]

    H=0
    for planet in list2:
        for i in list1:
            if planet[i]<0:
                planet[i]=planet[i]+360

        M=(planet["L"]-planet["ϖ"])*(math.pi/180)
        E1=M
        while True:
            E=M+planet["e"]*math.sin(E1)
            if round(E,4)==round(E1,4):
                break
            E1=E

        X1=planet["a"]*(math.cos(E)-planet["e"])
        Y1=planet["a"]*(math.sqrt(1-math.pow(planet["e"],2)))*math.sin(E)
        r=math.sqrt(X1**2+Y1**2)
        distance_d[list_name[H]]=r
        f=math.atan2(Y1,X1)*(180/math.pi)
        ω=planet["ϖ"]-planet["Ω"]

        if f<0:
            f=f+360
        if ω<0:
            ω=ω+360

        I=f+ω
        N1=math.sin(planet["i"]*(math.pi/180))*math.sin(I*(math.pi/180))
        β=math.asin(N1)*(180/math.pi)
        N2=math.cos(planet["i"]*(math.pi/180))*math.tan(I*(math.pi/180))
        N2=math.atan(N2)*(180/math.pi)

        if I>180 and I<360 or I>540 and I<720:          #Find the position of an object in a trigonometric circle
            R=planet["Ω"]+180
            λ=N2+R
            if λ<R:
                λ=λ+180
        else:
            λ=N2+planet["Ω"]
            if λ<planet["Ω"]:
                λ=λ+180    

        pos_d[list_name[H]]['x']=r*math.cos(λ*(math.pi/180))*math.cos(β*(math.pi/180))
        pos_d[list_name[H]]['y']=r*math.sin(λ*(math.pi/180))*math.cos(β*(math.pi/180))
        pos_d[list_name[H]]['z']=r*math.sin(β*(math.pi/180))
        H+=1

planet_fun(time)
lamp = local_light(pos=vector(0,0,0),color=color.yellow)

if choose["choose"]==1 or choose["choose"]==3:          #Make objects and graphs of the first four planets of the solar system
    if choose["choose"]==1:
        speed_time=1
        speed=30
        s1,mr,v,e,m=0.2,0.03,0.08,0.09,0.08
        path={"mer":60,"ven":160,"ear":220,"mar":400}
        sun=sphere(pos=vector(0,0,0),radius=s1,texture='sun.jpg')
    elif choose["choose"]==3:
        speed_time=2
        speed=45
        s1,mr,v,e,m=0.28,0.03,0.08,0.09,0.08
        path={"mer":20,"ven":50,"ear":50,"mar":50}
        sun=sphere(pos=vector(0,0,0), radius=s1,texture='sun.jpg')
    if graph_choose["selected"]==1:
        graph1=graph(title="Graph of Mercury's distance from the Sun.",
                     xtitle='Time[day]', ytitle='distance[au]')
        graph_mercury=gcurve(color=color.orange)
        graph2=graph(title="Graph of Venus's distance from the Sun.",
                     xtitle='Time[day]', ytitle='distance[au]')
        graph_venus=gcurve(color=color.yellow)
        graph3=graph(title="Graph of Earth's distance from the Sun.",
                     xtitle='Time[day]', ytitle='distance[au]')
        graph_earth=gcurve(color=color.blue)
        graph4=graph(title="Graph of Mars's distance from the Sun.",
                     xtitle='Time[day]', ytitle='distance[au]')
        graph_mars=gcurve(color=color.red)

    mercury=sphere(pos=vector(pos_d["mer"]['x'],pos_d["mer"]['y'],pos_d["mer"]['z']),radius=mr
    ,texture='mercury.jpg',make_trail=True,interval=1,retain=path["mer"])

    venus=sphere(pos=vector(pos_d["ven"]['x'],pos_d["ven"]['y'],pos_d["ven"]['z']),radius=v
    ,texture='venus.jpg',make_trail=True,interval=1,retain=path["ven"])

    earth=sphere(pos=vector(pos_d["ear"]['x'],pos_d["ear"]['y'],pos_d["ear"]['z']),radius=e,
    make_trail=True,interval=1,retain=path["ear"],texture="earth.jpg")

    mars=sphere(pos=vector(pos_d["mar"]['x'],pos_d["mar"]['y'],pos_d["mar"]['z']),radius=m,
    texture="mars.jpg",make_trail=True,interval=1,retain=path["mar"])

if choose["choose"]==2 or choose["choose"]==3:          #Make objects and graphs of the last five planets of the solar system
    if choose["choose"]==2:
        speed_time=30
        speed=60
        s2,j,sa,ri,u,n,p,thickness_ring=2.5,0.9,0.7,1.5,0.7,0.6,0.4,0.05
        path={"jup":25,"sat":35,"ura":60,"nep":130,"plu":250}
        sun=sphere(pos=vector(0,0,0), radius=s2,texture='sun.jpg')
    elif choose["choose"]==3:
        j,sa,ri,u,n,p,thickness_ring=0.2,0.1,0.2,0.2,0.2,0.2,0.01
        path={"jup":250,"sat":350,"ura":600,"nep":1300,"plu":2500}
    if graph_choose["selected"]==1:
        graph5=graph(title="Graph of Jupiter's distance from the Sun.",
                     xtitle='Time[day]', ytitle='distance[au]')
        graph_jupiter=gcurve(color=color.red)
        graph6=graph(title="Graph of Saturn's distance from the Sun.",
                     xtitle='Time[day]', ytitle='distance[au]')
        graph_saturn=gcurve(color=color.yellow)
        graph7=graph(title="Graph of Uranus's distance from the Sun.",
                     xtitle='Time[day]', ytitle='distance[au]')
        graph_uranus=gcurve(color=color.cyan)
        graph8=graph(title="Graph of Neptune's distance from the Sun.",
                     xtitle='Time[day]', ytitle='distance[au]')
        graph_neptune=gcurve(color=color.blue)
        graph9=graph(title="Graph of Pluto's distance from the Sun.",
                     xtitle='Time[day]', ytitle='distance[au]')
        graph_pluto=gcurve(color=color.blue)

    jupiter=sphere(pos=vector(pos_d["jup"]['x'],pos_d["jup"]['y'],pos_d["jup"]['z']),radius=j,
    texture='jupiter.png',make_trail=True,interval=2,retain=path["jup"])

    saturn=sphere(pos=vector(pos_d["sat"]['x'],pos_d["sat"]['y'],pos_d["sat"]['z']),radius=sa,
    texture='saturn.jpg',make_trail=True,interval=2,retain=path["sat"])

    ring_s=ring(pos=vector(pos_d["sat"]['x'],pos_d["sat"]['y'],pos_d["sat"]['z']),axis=vector(0,0,1)
    ,radius=ri, thickness=thickness_ring,texture='saturn.jpg')

    uranus=sphere(pos=vector(pos_d["ura"]['x'],pos_d["ura"]['y'],pos_d["ura"]['z']),radius=u,
    texture='uranus.jpg',make_trail=True, interval=3,retain=path["ura"])

    neptune=sphere(pos=vector(pos_d["nep"]['x'],pos_d["nep"]['y'],pos_d["nep"]['z']),radius=n,
    texture='neptune.jpg',make_trail=True,interval=5,retain=path["nep"])

    pluto=sphere(pos=vector(pos_d["plu"]['x'],pos_d["plu"]['y'],pos_d["plu"]['z']),radius=p,
    texture='pluto.jpg',make_trail=True,interval=5,retain=path["plu"])

days_added = datetime.timedelta(days=speed_time )
scene_title(time)
delta_t=0
while True:          #Show the motion of the planets and draw their graphs
    rate(speed)
    if run:
        delta_t=delta_t+speed_time
        time=time+days_added
        scene_title(time)
        planet_fun(time)
        if choose["choose"]==1 or choose["choose"]==3:
            mercury.pos.x,mercury.pos.y,mercury.pos.z=pos_d["mer"]['x'],pos_d["mer"]['y'],pos_d["mer"]['z']

            venus.pos.x,venus.pos.y,venus.pos.z=pos_d["ven"]['x'],pos_d["ven"]['y'],pos_d["ven"]['z']

            earth.pos.x,earth.pos.y,earth.pos.z=pos_d["ear"]['x'],pos_d["ear"]['y'],pos_d["ear"]['z']

            mars.pos.x,mars.pos.y,mars.pos.z=pos_d["mar"]['x'],pos_d["mar"]['y'],pos_d["mar"]['z']

            if graph_choose["selected"]==1:
                graph_mercury.plot(delta_t,distance_d["mer"])
                graph_venus.plot(delta_t,distance_d["ven"])
                graph_earth.plot(delta_t,distance_d["ear"])
                graph_mars.plot(delta_t,distance_d["mar"])
        if choose["choose"]==2 or choose["choose"]==3:
            jupiter.pos.x,jupiter.pos.y,jupiter.pos.z=pos_d["jup"]['x'],pos_d["jup"]['y'],pos_d["jup"]['z']

            saturn.pos.x,saturn.pos.y,saturn.pos.z=pos_d["sat"]['x'],pos_d["sat"]['y'],pos_d["sat"]['z']

            ring_s.pos.x,ring_s.pos.y,ring_s.pos.z=pos_d["sat"]['x'],pos_d["sat"]['y'],pos_d["sat"]['z']

            uranus.pos.x,uranus.pos.y,uranus.pos.z=pos_d["ura"]['x'],pos_d["ura"]['y'],pos_d["ura"]['z']

            neptune.pos.x,neptune.pos.y,neptune.pos.z=pos_d["nep"]['x'],pos_d["nep"]['y'],pos_d["nep"]['z']

            pluto.pos.x,pluto.pos.y,pluto.pos.z=pos_d["plu"]['x'],pos_d["plu"]['y'],pos_d["plu"]['z']

            if graph_choose["selected"]==1:
                graph_jupiter.plot(delta_t,distance_d["jup"])
                graph_saturn.plot(delta_t,distance_d["sat"])
                graph_uranus.plot(delta_t,distance_d["ura"])
                graph_neptune.plot(delta_t,distance_d["nep"])
                graph_pluto.plot(delta_t,distance_d["plu"])