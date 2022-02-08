#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from main3 import *
import numpy as np

def test():
    # Teste Relationen i^2=-1, j^2=-1, i*j=k
    assert Quaternion(0,1,0,0)*Quaternion(0,1,0,0)==Quaternion(-1,0,0,0)
    assert Quaternion(0,0,1,0)*Quaternion(0,0,1,0)==Quaternion(-1,0,0,0)
    assert Quaternion(0,1,0,0)*Quaternion(0,0,1,0)==Quaternion(0,0,0,1)
    
    # Teste Assoiziativität
    for i1 in range(4):
        for i2 in range(4):
            for i3 in range(4):
                u = np.zeros((3,4))
                u[0,i1]=1.
                u[1,i2]=1.
                u[2,i3]=1.
                a = Quaternion(u[0,0],u[0,1],u[0,2],u[0,3])
                b = Quaternion(u[1,0],u[1,1],u[1,2],u[1,3])
                c = Quaternion(u[2,0],u[2,1],u[2,2],u[2,3])
                assert (a*b)*c==a*(b*c)

