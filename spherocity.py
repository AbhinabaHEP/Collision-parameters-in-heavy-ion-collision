import numpy as np


#a=0

def sph(par_array_px,par_array_py,eta_array,npart):
    npart=len(eta_array)
    if(len(par_array_px)!=npart or len(par_array_py)!=npart or len(eta_array)!=npart):
        print ("unequal array length, exiting the code")
        print (len(par_array_px),len(par_array_py),len(eta_array),npart)
        return -100
    if(len(par_array_px)==0 or len(par_array_py)==0 or len(eta_array)==0 or npart==0):
        print("No entries, unable to calculate spherocity")
        return -404
        
    #a=npart_array[0]
    list_of_ptVector=[]
    list_of_unitVector=[]
    spherocity=0
    sum_pt=0
    
    for i in range(0,npart):
        #global spherocity
        pt_value = np.sqrt(float(par_array_px[i]**2) + float(par_array_py[i]**2))
        if(pt_value >= 0.15 and abs(eta_array[i]) < 0.8):
            values = [par_array_px[i], par_array_py[i], 0]
            unit_values = [par_array_px[i]/pt_value, par_array_py[i]/pt_value, 0]
            list_of_ptVector.append(values)
            list_of_unitVector.append(unit_values)
            #print("px",par_array_px[i],"py",par_array_py[i],"eta",eta_array[i])
            #global sum_pt
            sum_pt = sum_pt + pt_value
            #print ("pt",pt_value)
    sphero=99999
    s=float(0)
    print("npart",npart,"length of unit vector array",len(list_of_unitVector),"length of pt vector array",len(list_of_ptVector))
    for i in range (0,len(list_of_unitVector)):
        vect1 = (list_of_unitVector[i])
        #print("vect1",vect1)
        s = float(0)
        for j in range (0,len(list_of_ptVector)):
            vect2 =(list_of_ptVector[j])
            #print("vect2",vect2)
            #s = s + fabs(vect2.Cross(vect1).Mag())
            s = s + abs(np.linalg.norm(np.cross(vect2,vect1)))
            #s1=np.cross(vect2,vect1)
            #print("s1",s1)
            #s = s + (np.sqrt(s1[0]**2 + s1[1]**2 +s1[2]**2))
            #print("s",s)
            #print ("sphero_1", sphero)
        if(s < sphero):
            sphero = s
            #print ("sphero", sphero)
    if(sum_pt !=0):
        spherocity = 0.25 * 3.14 * 3.14 * sphero * sphero / (sum_pt* sum_pt)
        #print("spherocity",spherocity)
    return spherocity

'''px=[0.1, -0.14, -0.14, 0.16]
py=[.1,.15,-.13,.13]
eta=[0.2,0,0.5,0.7]
npart=4
print (sph(px,py,eta,npart))'''



        
