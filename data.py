# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 10:45:21 2023

@author: Francisco
"""
import statistics

Q1S1P1=[9,5,5,8,7,5,5,5,3,6,6,6,8,7,5,7,7,4,7,7,1,6,6,5,6,5,6,2,4,7,5,5,6,6,5,5,6,10,5,6,5,5,6,7,5,5,7,8,3,2,1,3,9,6,7,6,10,10,7,9,9,6,5,7,2,9,5,5,5,8,6,5,5,6,7,8]
Q1S1P2=[10,8,7,8,6,5,6,2,7,8,6,10,6,7,8,3,7,6,5,1,9,6,5,5,7,4,7,6,5,7,7,5,5,7,7,6,5,1,9,7,9,6,5,8,3,5,10,5,8,7,6,4,6,7,9,7,5,8,10,4,6,5,10,9,8,5,6,1,5]
Q1S1P3=[7,10,5,6,10,5,5,6,6,9,7,10,7,9,5,5,6,2,4,6,4,5,7,7,5,5,8,3,6,8,5,3,7,7,5,5,8,2,2,8,1,5,7,8,6,7,4,7,9,5,10,6,7,8,7,3,10,10,10,9,6,8,10,6,1,5,7,7,6,5,8,6,7]
Q1S2P1=[8,5,6,9,6,6,5,5,8,10,7,5,5,7,8,5,5,7,2,8,8,5,6,8,7,5,5,5,6,10,5,5,5,7,7,5,5,6,6,7,6,5,5,6,8,4,5,7,3,8,8,9,10,7,8,7,8,7,2,9,7,5,8,8,7,5,5,8,8,5,5,5,7,8,7,5,6,9,6]
Q1S2P2=[9,1,5,6,7,5,5,7,8,5,6,5,10,6,10,5,4,5,5,6,7,1,4,7,6,6,7,6,6,5,8,1,5,6,7,5,5,7,4,5,5,6,8,6,6,6,6,6,3,5,10,9,10,9,8,6,7,5,2,7,10,9,5,7,8,6,7,7,3,6,5,5,10,6,7,5,5,7,2,5]
Q1S2P3=[7,1,10,7,9,5,5,5,3,6,8,5,6,9,5,7,9,8,4,6,1,5,8,6,5,5,9,2,6,5,1,5,8,7,5,5,6,3,7,8,1,5,7,7,6,7,4,5,10,10,10,8,6,8,6,7,7,10,10,9,8,6,7,10,2,8,5,1,10,8,5,5,7,7,3,3]
Q1S3P1=[7,1,5,7,8,5,5,8,9,6,5,1,6,6,7,5,6,7,6,5,7,5,5,6,5,5,5,5,7,5,6,1,5,8,7,5,5,6,10,2,5,5,5,6,8,5,5,2,6,5,3,6,5,5,2,2,4,7,10,8,4,5,3,2,7,6,5,5,0,6,5,5,7,9,5]
Q1S3P2=[6,5,5,7,6,5,5,6,3,1,6,9,10,6,8,5,5,2,2,7,5,7,7,5,5,5,6,1,1,7,1,5,8,6,5,5,6,4,1,8,1,5,8,5,5,5,6,2,3,6,1,10,8,8,5,5,6,3,7,9,9,6,6,6,6,3,8,6,1,5,6,5,5,5,6,2,6]
Q1S3P3=[9,3,5,8,6,5,5,8,3,6,6,10,5,6,7,5,5,7,1,5,6,1,5,7,5,5,4,2,7,5,1,5,7,7,5,5,5,2,5,5,5,5,5,5,5,5,6,2,6,6,5,10,6,7,5,6,6,1,6,9,9,5,5,5,6,1,10,8,1,5,9,5,5,5,2,7,5]

Q1S1P1_Paper=[9,5,5,8,7,5,5,5,3,6]
Q1S1P1_Fabrics=[6,6,8,7,5,7,7,4,7]
Q1S1P1_Cup=[7,1,6,6,5,6,5,6,2,4]
Q1S1P1_Dough=[7,5,5,6,6,5,5,6,10,5]
Q1S1P1_Strawberry=[6,5,5,6,7,5,5,7,8,3]
Q1S1P1_Raspberry=[2,1,3,9,6,7,6,10]
Q1S1P1_Cable=[10,7,9,9,6,5,7,2,9]
Q1S1P1_Prism=[5,5,5,8,6,5,5,6,7,8]

Q1S1P2_Paper=[7,10,8,7,8,6,5,6,2,7]
Q1S1P2_Fabrics=[8,6,10,6,7,8,3,7]
Q1S1P2_Cup=[6,5,1,9,6,5,5,7,4,7]
Q1S1P2_Dough=[6,5,7,7,5,5,7,7,6]
Q1S1P2_Strawberry=[5,1,9,7,9,6,5,8,3,5]
Q1S1P2_Raspberry=[10,5,8,7,6,4,6]
Q1S1P2_Cable=[7,9,7,5,8,10,4]
Q1S1P2_Prism=[6,5,10,9,8,5,6,1,5]

Q1S1P3_Paper=[7,10,5,6,10,5,5,6,6,9]
Q1S1P3_Fabrics=[7,10,7,9,5,5,6,2,4]
Q1S1P3_Cup=[6,4,5,7,7,5,5,8,3,6]
Q1S1P3_Dough=[8,5,3,7,7,5,5,8,2,2]
Q1S1P3_Strawberry=[8,1,5,7,8,6,7,4,7]
Q1S1P3_Raspberry=[9,5,10,6,7,8,7,3]
Q1S1P3_Cable=[10,10,10,9,6,8,10]
Q1S1P3_Prism=[6,1,5,7,7,6,5,8,6,7]

Q1S2P1_Paper=[8,5,6,9,6,6,5,5,8,10]
Q1S2P1_Fabrics=[7,5,5,7,8,5,5,7,2,8]
Q1S2P1_Cup=[8,5,6,8,7,5,5,5,6,10]
Q1S2P1_Dough=[5,5,5,7,7,5,5,6,6,7]
Q1S2P1_Strawberry=[6,5,5,6,8,4,5,7,3,8]
Q1S2P1_Raspberry=[8,9,10,7,8,7,8,7,2,9]
Q1S2P1_Cable=[7,5,8,8,7,5,5,8,8]
Q1S2P1_Prism=[5,5,5,7,8,7,5,6,9,6]

Q1S2P2_Paper=[9,1,5,6,7,5,5,7,8,5]
Q1S2P2_Fabrics=[6,5,10,6,10,5,4,5,5,6]
Q1S2P2_Cup=[7,1,4,7,6,6,7,6,6,5]
Q1S2P2_Dough=[8,1,5,6,7,5,5,7,4,5]
Q1S2P2_Strawberry=[5,6,8,6,6,6,6,6,3,5]
Q1S2P2_Raspberry=[10,9,10,9,8,6,7,5,2,7]
Q1S2P2_Cable=[10,9,5,7,8,6,7,7,3,6]
Q1S2P2_Prism=[5,5,10,6,7,5,5,7,2,5]

Q1S2P3_Paper=[7,1,10,7,9,5,5,5,3,6]
Q1S2P3_Fabrics=[8,5,6,9,5,7,9,8,4]
Q1S2P3_Cup=[6,1,5,8,6,5,5,9,2,6]
Q1S2P3_Dough=[5,1,5,8,7,5,5,6,3,7]
Q1S2P3_Strawberry=[8,1,5,7,7,6,7,4,5]
Q1S2P3_Raspberry=[10,10,10,8,6,8,6,7,7]
Q1S2P3_Cable=[10,10,9,8,6,7,10,2,8]
Q1S2P3_Prism=[5,1,10,8,5,5,7,7,3,3]

Q1S3P1_Paper=[7,1,5,7,8,5,5,8,9,6]
Q1S3P1_Fabrics=[5,1,6,6,7,5,6,7,6,5]
Q1S3P1_Cup=[7,5,5,6,5,5,5,5,7,5]
Q1S3P1_Dough=[6,1,5,8,7,5,5,6,10,2]
Q1S3P1_Strawberry=[5,5,5,6,8,5,5,2,6]
Q1S3P1_Raspberry=[5,3,6,5,5,2,2,4]
Q1S3P1_Cable=[7,10,8,4,5,3,2,7]
Q1S3P1_Prism=[6,5,5,0,6,5,5,7,9,5]

Q1S3P2_Paper=[6,5,5,7,6,5,5,6,3,1]
Q1S3P2_Fabrics=[6,9,10,6,8,5,5,2,2]
Q1S3P2_Cup=[7,5,7,7,5,5,5,6,1,1]
Q1S3P2_Dough=[7,1,5,8,6,5,5,6,4,1]
Q1S3P2_Strawberry=[8,1,5,8,5,5,5,6,2,3]
Q1S3P2_Raspberry=[6,1,10,8,8,5,5,6,3,7]
Q1S3P2_Cable=[9,9,6,6,6,6,3,8]
Q1S3P2_Prism=[6,1,5,6,5,5,5,6,2,6]

Q1S3P3_Paper=[9,3,5,8,6,5,5,8,3,6]
Q1S3P3_Fabrics=[6,10,5,6,7,5,5,7,1,5]
Q1S3P3_Cup=[6,1,5,7,5,5,4,2,7]
Q1S3P3_Dough=[5,1,5,7,7,5,5,5,2,5]
Q1S3P3_Strawberry=[5,5,5,5,5,5,5,6,2,6]
Q1S3P3_Raspberry=[6,5,10,6,7,5,6,6,1,6]
Q1S3P3_Cable=[9,9,5,5,5,6,1,10]
Q1S3P3_Prism=[8,1,5,9,5,5,5,2,7,5]


Q2S1P1=[2,1,2,0,0,1,0,2,1,0,1,1,0,0,0,0,3,2,1,1,1,2,0,0,0,3,2,1,1,3,1,0,0,1,2,1,1,1,1,1,0,0,5,1,1,1,2,5,7,0,1,5,6,1,1,0,0,0,0,0,1,2,0,1,0,0,0,0,0,3,2]
Q2S1P2=[0,1,0,1,0,0,0,0,2,2,0,1,0,1,0,0,0,0,2,1,1,1,3,4,0,0,0,1,1,3,1,1,3,3,1,0,0,2,2,1,1,3,0,1,0,0,3,4,1,3,8,5,2,4,7,2,1,1,0,0,0,0,2, 1,1,1,0,0,0,0,0,2,1]
Q2S1P3=[1,1,1,0,0,0,0,6,1,0,1,2,0,0,0,0,2,0,1,1,2,0,0,0,1,1,2,1,1,1,4,2,1,0,2,2,1,2,1,10,3,0,1,0,0,4,1,7,10,10,3,4,0,2,10,8,3,1,1,1,1,0,0,0,1,1,1,1,1,0,0,0,5,1]
Q2S2P1=[1,1,0,3,0,0,0,0,6,1,0,1,0,0,0,0,0,0,2,0,2,1,0,2,0,0,0,1,2,3,0,1,0,2,3,1,0,1,3,4,1,1,0,2,2,0,0,0,3,4,7,1,3,2,2,0,3,5,7,9,1,1,0,1,0,0,0,4,2,1,1,0,0,1,0,0,0,2,1]
Q2S2P2=[3,1,1,0,0,0,0,5,2,0,1,0,0,0,0,0,5,1,1,1,2,0,0,1,0,5,3,1,1,3,4,1,1,2,2,2,2,1,1,1,0,0,0,6,2,10,10,4,5,0,5,8,2,5,1,1,1,1,0,0,0,2,0,0,1,1,1,0,0,0,5,2]
Q2S2P3=[2,1,2,0,0,0,0,3,6,0,1,1,0,0,0,0,6,4,1,1,3,0,0,1,1,2,6,1,1,4,2,1,1,1,2,7,1,2,1,0,0,0,3,5,6,10,1,2,1,1,6,8,7,1,1,1,0,0,0,0,1,8,0,1,1,0,0,0,0,1,3]
Q2S3P1=[2,1,0,2,0,0,0,0,6,2,0,1,0,1,0,0,0,0,5,1,2,1,0,3,0,0,0,0,6,2,2,1,1,3,0,1,0,3,5,2,2,1,1,1,1,0,0,0,4,1,10,10,3,1,3,0,1,0,8,0,1,0,1,0,0,0,6,3,0,1,0,0,1,0,0,0,2,2]
Q2S3P2=[0,1,0,2,0,0,0,0,3,1,0,1,0,0,0,0,0,0,2,2,2,1,0,1,0,0,0,1,4,1,2,1,0,2,3,1,0,1,3,2,1,1,0,2,0,0,0,0,1,1,7,1,7,8,2,0,1,0,8,4,1,1,0,0,0,0,0,5,4,1,0,1,0,0,0,0,0,0,2,0]
Q2S3P3=[2,1,0,4,0,0,0,0,3,0,0,1,0,1,0,0,0,0,1,2,2,1,0,2,0,0,1,3,2,2,1,0,3,2,1,0,7,4,2,2,1,0,1,0,0,0,0,7,3,2,1,5,3,3,1,2,7,4,2,1,1,0,0,0,0,0,4,3,0,1,0,1,0,0,0,0,1,3]

Q2S1P1_Paper=[2,1,2,0,0,1,0,2,1]
Q2S1P1_Fabrics=[0,1,1,0,0,0,0,3,2]
Q2S1P1_Cup=[1,1,1,2,0,0,0,3,2]
Q2S1P1_Dough=[1,1,3,1,0,0,1,2]
Q2S1P1_Strawberry=[1,1,1,1,1,0,0,5,1]
Q2S1P1_Raspberry=[1,1,2,5,7,0,1,5,6]
Q2S1P1_Cable=[1,1,0,0,0,0,0,1,2]
Q2S1P1_Prism=[0,1,0,0,0,0,0,3,2]
 
Q2S1P2_Paper=[0,1,0,1,0,0,0,0,2,2]
Q2S1P2_Fabrics=[0,1,0,1,0,0,0,0,2,1]
Q2S1P2_Cup=[1,1,3,4,0,0,0,1,1,3]
Q2S1P2_Dough=[1,1,3,3,1,0,0,2,2]
Q2S1P2_Strawberry=[1,1,3,0,1,0,0,3,4]
Q2S1P2_Raspberry=[1,3,8,5,2,4,7,2]
Q2S1P2_Cable=[1,1,0,0,0,0,2,]
Q2S1P2_Prism=[1,1,1,0,0,0,0,0,2,1]
 
Q2S1P3_Paper=[1,1,1,0,0,0,0,6,1]
Q2S1P3_Fabrics=[0,1,2,0,0,0,0,2,0]
Q2S1P3_Cup=[1,1,2,0,0,0,1,1,2]
Q2S1P3_Dough=[1,1,1,4,2,1,0,2,2,1]
Q2S1P3_Strawberry=[2,1,10,3,0,1,0,0,4,1]
Q2S1P3_Raspberry=[7,10,10,3,4,0,2,10,8,3]
Q2S1P3_Cable=[1,1,1,1,0,0,0,1]
Q2S1P3_Prism=[1,1,1,1,0,0,0,5,1]
 
Q2S2P1_Paper=[1,1,0,3,0,0,0,0,6,1]
Q2S2P1_Fabrics=[0,1,0,0,0,0,0,0,2,0]
Q2S2P1_Cup=[2,1,0,2,0,0,0,1,2,3]
Q2S2P1_Dough=[0,1,0,2,3,1,0,1,3,4]
Q2S2P1_Strawberry=[1,1,0,2,2,0,0,0,3,4]
Q2S2P1_Raspberry=[7,1,3,2,2,0,3,5,7,9]
Q2S2P1_Cable=[1,1,0,1,0,0,0,4,2]
Q2S2P1_Prism=[1,1,0,0,1,0,0,0,2,1]

Q2S2P2_Paper=[3,1,1,0,0,0,0,5,2]
Q2S2P2_Fabrics=[0,1,0,0,0,0,0,5,1,]
Q2S2P2_Cup=[1,1,2,0,0,1,0,5,3,]
Q2S2P2_Dough=[1,1,3,4,1,1,2,2,2,]
Q2S2P2_Strawberry=[2,1,1,1,0,0,0,6,2,]
Q2S2P2_Raspberry=[10,10,4,5,0,5,8,2,5,]
Q2S2P2_Cable=[1,1,1,1,0,0,0,2,0,]
Q2S2P2_Prism=[0,1,1,1,0,0,0,5,2]
 
Q2S2P3_Paper=[2,1,2,0,0,0,0,3,6]
Q2S2P3_Fabrics=[0,1,1,0,0,0,0,6,4]
Q2S2P3_Cup=[1,1,3,0,0,1,1,2,6]
Q2S2P3_Dough=[1,1,4,2,1,1,1,2,7]
Q2S2P3_Strawberry=[1,2,1,0,0,0,3,5]
Q2S2P3_Raspberry=[6,10,1,2,1,1,6,8,7]
Q2S2P3_Cable=[1,1,1,0,0,0,0,1,8]
Q2S2P3_Prism=[0,1,1,0,0,0,0,1,3]
 
Q2S3P1_Paper=[2,1,0,2,0,0,0,0,6,2]
Q2S3P1_Fabrics=[0,1,0,1,0,0,0,0,5,1]
Q2S3P1_Cup=[2,1,0,3,0,0,0,0,6,2]
Q2S3P1_Dough=[2,1,1,3,0,1,0,3,5,2]
Q2S3P1_Strawberry=[2,1,1,1,1,0,0,0,4,1]
Q2S3P1_Raspberry=[10,10,3,1,3,0,1,0,8]
Q2S3P1_Cable=[0,1,0,1,0,0,0,6,3]
Q2S3P1_Prism=[0,1,0,0,1,0,0,0,2,2]

Q2S3P2_Paper=[0,1,0,2,0,0,0,0,3,1]
Q2S3P2_Fabrics=[0,1,0,0,0,0,0,0,2,2]
Q2S3P2_Cup=[2,1,0,1,0,0,0,1,4,1]
Q2S3P2_Dough=[2,1,0,2,3,1,0,1,3,2]
Q2S3P2_Strawberry=[1,1,0,2,0,0,0,0,1,1]
Q2S3P2_Raspberry=[7,1,7,8,2,0,1,0,8,4]
Q2S3P2_Cable=[1,1,0,0,0,0,0,5,4,1]
Q2S3P2_Prism=[0,1,0,0,0,0,0,0,2,0]

Q2S3P3_Paper=[2,1,0,4,0,0,0,0,3,0]
Q2S3P3_Fabrics=[0,1,0,1,0,0,0,0,1,2]
Q2S3P3_Cup=[2,1,0,2,0,0,1,3,2]
Q2S3P3_Dough=[2,1,0,3,2,1,0,7,4,2]
Q2S3P3_Strawberry=[2,1,0,1,0,0,0,0,7,3]
Q2S3P3_Raspberry=[2,1,5,3,3,1,2,7,4,2]
Q2S3P3_Cable=[1,1,0,0,0,0,0,4,3]
Q2S3P3_Prism=[0,1,0,1,0,0,0,0,1,3]

TS1P1=[832.9505,659.6968,493.1067,359.8346]
TS1P2=[766.3145,992.1367,466.4523,451.6443]
TS1P3=[629.3404,566.4064,644.1484,673.0241]
TS2P1=[313.1894,406.4799,466.4523,206.5717]
TS2P2=[826.2870,508.0998,429.4323,439.7979]
TS2P3=[479.1870,666.3604,546.4156,366.4982]
TS3P1=[299.8622,249.8852,513.0975,226.5626]
TS3P2=[626.3788,416.4753,466.4523,273.9482]
TS3P3=[346.5074,326.5166,339.8438,236.9282]

TS1P1_Paper=[]
TS1P1_Fabrics=[]
TS1P1_Cup=[]
TS1P1_Dough=[]
TS1P1_Strawberry=[]
TS1P1_Raspberry=[]
TS1P1_Cable=[]
TS1P1_Prism=[]

TS1P2_Paper=[]
TS1P2_Fabrics=[]
TS1P2_Cup=[]
TS1P2_Dough=[]
TS1P2_Strawberry=[]
TS1P2_Raspberry=[]
TS1P2_Cable=[]
TS1P2_Prism=[]

TS1P3_Paper=[]
TS1P3_Fabrics=[]
TS1P3_Cup=[]
TS1P3_Dough=[]
TS1P3_Strawberry=[]
TS1P3_Raspberry=[]
TS1P3_Cable=[]
TS1P3_Prism=[]

TS2P1_Paper=[]
TS2P1_Fabrics=[]
TS2P1_Cup=[]
TS2P1_Dough=[]
TS2P1_Strawberry=[]
TS2P1_Raspberry=[]
TS2P1_Cable=[]
TS2P1_Prism=[]

TS2P2_Paper=[]
TS2P2_Fabrics=[]
TS2P2_Cup=[]
TS2P2_Dough=[]
TS2P2_Strawberry=[]
TS2P2_Raspberry=[]
TS2P2_Cable=[]
TS2P2_Prism=[]

TS2P3_Paper=[]
TS2P3_Fabrics=[]
TS2P3_Cup=[]
TS2P3_Dough=[]
TS2P3_Strawberry=[]
TS2P3_Raspberry=[]
TS2P3_Cable=[]
TS2P3_Prism=[]

TS3P1_Paper=[]
TS3P1_Fabrics=[]
TS3P1_Cup=[]
TS3P1_Dough=[]
TS3P1_Strawberry=[]
TS3P1_Raspberry=[]
TS3P1_Cable=[]
TS3P1_Prism=[]

TS3P2_Paper=[]
TS3P2_Fabrics=[]
TS3P2_Cup=[]
TS3P2_Dough=[]
TS3P2_Strawberry=[]
TS3P2_Raspberry=[]
TS3P2_Cable=[]
TS3P2_Prism=[]

TS3P3_Paper=[]
TS3P3_Fabrics=[]
TS3P3_Cup=[]
TS3P3_Dough=[]
TS3P3_Strawberry=[]
TS3P3_Raspberry=[]
TS3P3_Cable=[]
TS3P3_Prism=[]



print("Total succes rate: ",((len(Q1S1P1)+len(Q1S1P2)+len(Q1S1P3)+len(Q1S1P1)+len(Q1S2P2)+len(Q1S2P3)+len(Q1S3P1)+len(Q1S3P2)+len(Q1S3P3))/720))
print("Succes rate paper: ",round(90/90,2))
print("Succes rate fabrics: ",round(86/90,2))
print("Succes rate cup: ",round(89/90,2))
print("Succes rate dough: ",round(89/90,2))
print("Succes rate strawberry: ",round(88/90,2))
print("Succes rate raspberry: ",round(81/90,2))
print("Succes rate cable: ",round(76/90,2))
print("Succes rate prism: ",round(89/90,2))




print("=======================Q1======================")
print("S1P1 mean: ",  round(statistics.mean(Q1S1P1),2))
print("S1P1 stddev: ",round(statistics.stdev(Q1S1P1),2))
print("S1P2 mean: ",  round(statistics.mean(Q1S1P2),2))
print("S1P2 stddev: ",round(statistics.stdev(Q1S1P2),2))
print("S1P3 mean: ",  round(statistics.mean(Q1S1P3),2))
print("S1P3 stddev: ",round(statistics.stdev(Q1S1P3),2))
print("S2P1 mean: ",  round(statistics.mean(Q1S2P1),2))
print("S2P1 stddev: ",round(statistics.stdev(Q1S2P1),2))
print("S2P2 mean: ",  round(statistics.mean(Q1S2P2),2))
print("S2P2 stddev: ",round(statistics.stdev(Q1S2P2),2))
print("S2P3 mean: ",  round(statistics.mean(Q1S2P3),2))
print("S2P3 stddev: ",round(statistics.stdev(Q1S2P3),2))
print("S3P1 mean: ",  round(statistics.mean(Q1S3P1),2))
print("S3P1 stddev: ",round(statistics.stdev(Q1S3P1),2))
print("S3P2 mean: ",  round(statistics.mean(Q1S3P2),2))
print("S3P2 stddev: ",round(statistics.stdev(Q1S3P2),2))
print("S3P3 mean: ",  round(statistics.mean(Q1S3P3),2))
print("S3P3 stddev: ",round(statistics.stdev(Q1S3P3),2))
print("===============================================")

print("=======================Q2======================")
print("S1P1 mean: ",  round(statistics.mean(Q2S1P1),2))
print("S1P1 stddev: ",round(statistics.stdev(Q2S1P1),2))
print("S1P2 mean: ",  round(statistics.mean(Q2S1P2),2))
print("S1P2 stddev: ",round(statistics.stdev(Q2S1P2),2))
print("S1P3 mean: ",  round(statistics.mean(Q2S1P3),2))
print("S1P3 stddev: ",round(statistics.stdev(Q2S1P3),2))
print("S2P1 mean: ",  round(statistics.mean(Q2S2P1),2))
print("S2P1 stddev: ",round(statistics.stdev(Q2S2P1),2))
print("S2P2 mean: ",  round(statistics.mean(Q2S2P2),2))
print("S2P2 stddev: ",round(statistics.stdev(Q2S2P2),2))
print("S2P3 mean: ",  round(statistics.mean(Q2S2P3),2))
print("S2P3 stddev: ",round(statistics.stdev(Q2S2P3),2))
print("S3P1 mean: ",  round(statistics.mean(Q2S3P1),2))
print("S3P1 stddev: ",round(statistics.stdev(Q2S3P1),2))
print("S3P2 mean: ",  round(statistics.mean(Q2S3P2),2))
print("S3P2 stddev: ",round(statistics.stdev(Q2S3P2),2))
print("S3P3 mean: ",  round(statistics.mean(Q2S3P3),2))
print("S3P3 stddev: ",round(statistics.stdev(Q2S3P3),2))
print("===============================================")

print("======================TIME=====================")
print("S1P1 mean: ",  round(statistics.mean(TS1P1),2))
print("S1P1 stddev: ",round(statistics.stdev(TS1P1),2))
print("S1P2 mean: ",  round(statistics.mean(TS1P2),2))
print("S1P2 stddev: ",round(statistics.stdev(TS1P2),2))
print("S1P3 mean: ",  round(statistics.mean(TS1P3),2))
print("S1P3 stddev: ",round(statistics.stdev(TS1P3),2))
print("S2P1 mean: ",  round(statistics.mean(TS2P1),2))
print("S2P1 stddev: ",round(statistics.stdev(TS2P1),2))
print("S2P2 mean: ",  round(statistics.mean(TS2P2),2))
print("S2P2 stddev: ",round(statistics.stdev(TS2P2),2))
print("S2P3 mean: ",  round(statistics.mean(TS2P3),2))
print("S2P3 stddev: ",round(statistics.stdev(TS2P3),2))
print("S3P1 mean: ",  round(statistics.mean(TS3P1),2))
print("S3P1 stddev: ",round(statistics.stdev(TS3P1),2))
print("S3P2 mean: ",  round(statistics.mean(TS3P2),2))
print("S3P2 stddev: ",round(statistics.stdev(TS3P2),2))
print("S3P3 mean: ",  round(statistics.mean(TS3P3),2))
print("S3P3 stddev: ",round(statistics.stdev(TS3P3),2))
print("===============================================")

print("==================Q1_PAPER=====================")
print("S1P1 mean: ",  round(statistics.mean(Q1S1P1_Paper),2))
print("S1P1 stddev: ",round(statistics.stdev(Q1S1P1_Paper),2))
print("S1P2 mean: ",  round(statistics.mean(Q1S1P2_Paper),2))
print("S1P2 stddev: ",round(statistics.stdev(Q1S1P2_Paper),2))
print("S1P3 mean: ",  round(statistics.mean(Q1S1P3_Paper),2))
print("S1P3 stddev: ",round(statistics.stdev(Q1S1P3_Paper),2))
print("S2P1 mean: ",  round(statistics.mean(Q1S2P1_Paper),2))
print("S2P1 stddev: ",round(statistics.stdev(Q1S2P1_Paper),2))
print("S2P2 mean: ",  round(statistics.mean(Q1S2P2_Paper),2))
print("S2P2 stddev: ",round(statistics.stdev(Q1S2P2_Paper),2))
print("S2P3 mean: ",  round(statistics.mean(Q1S2P3_Paper),2))
print("S2P3 stddev: ",round(statistics.stdev(Q1S2P3_Paper),2))
print("S3P1 mean: ",  round(statistics.mean(Q1S3P1_Paper),2))
print("S3P1 stddev: ",round(statistics.stdev(Q1S3P1_Paper),2))
print("S3P2 mean: ",  round(statistics.mean(Q1S3P2_Paper),2))
print("S3P2 stddev: ",round(statistics.stdev(Q1S3P2_Paper),2))
print("S3P3 mean: ",  round(statistics.mean(Q1S3P3_Paper),2))
print("S3P3 stddev: ",round(statistics.stdev(Q1S3P3_Paper),2))
print("===============================================")

print("=================Q1_FABRICS====================")
print("S1P1 mean: ",  round(statistics.mean(Q1S1P1_Fabrics),2))
print("S1P1 stddev: ",round(statistics.stdev(Q1S1P1_Fabrics),2))
print("S1P2 mean: ",  round(statistics.mean(Q1S1P2_Fabrics),2))
print("S1P2 stddev: ",round(statistics.stdev(Q1S1P2_Fabrics),2))
print("S1P3 mean: ",  round(statistics.mean(Q1S1P3_Fabrics),2))
print("S1P3 stddev: ",round(statistics.stdev(Q1S1P3_Fabrics),2))
print("S2P1 mean: ",  round(statistics.mean(Q1S2P1_Fabrics),2))
print("S2P1 stddev: ",round(statistics.stdev(Q1S2P1_Fabrics),2))
print("S2P2 mean: ",  round(statistics.mean(Q1S2P2_Fabrics),2))
print("S2P2 stddev: ",round(statistics.stdev(Q1S2P2_Fabrics),2))
print("S2P3 mean: ",  round(statistics.mean(Q1S2P3_Fabrics),2))
print("S2P3 stddev: ",round(statistics.stdev(Q1S2P3_Fabrics),2))
print("S3P1 mean: ",  round(statistics.mean(Q1S3P1_Fabrics),2))
print("S3P1 stddev: ",round(statistics.stdev(Q1S3P1_Fabrics),2))
print("S3P2 mean: ",  round(statistics.mean(Q1S3P2_Fabrics),2))
print("S3P2 stddev: ",round(statistics.stdev(Q1S3P2_Fabrics),2))
print("S3P3 mean: ",  round(statistics.mean(Q1S3P3_Fabrics),2))
print("S3P3 stddev: ",round(statistics.stdev(Q1S3P3_Fabrics),2))
print("===============================================")

print("====================Q1_CUP=====================")
print("S1P1 mean: ",  round(statistics.mean(Q1S1P1_Cup),2))
print("S1P1 stddev: ",round(statistics.stdev(Q1S1P1_Cup),2))
print("S1P2 mean: ",  round(statistics.mean(Q1S1P2_Cup),2))
print("S1P2 stddev: ",round(statistics.stdev(Q1S1P2_Cup),2))
print("S1P3 mean: ",  round(statistics.mean(Q1S1P3_Cup),2))
print("S1P3 stddev: ",round(statistics.stdev(Q1S1P3_Cup),2))
print("S2P1 mean: ",  round(statistics.mean(Q1S2P1_Cup),2))
print("S2P1 stddev: ",round(statistics.stdev(Q1S2P1_Cup),2))
print("S2P2 mean: ",  round(statistics.mean(Q1S2P2_Cup),2))
print("S2P2 stddev: ",round(statistics.stdev(Q1S2P2_Cup),2))
print("S2P3 mean: ",  round(statistics.mean(Q1S2P3_Cup),2))
print("S2P3 stddev: ",round(statistics.stdev(Q1S2P3_Cup),2))
print("S3P1 mean: ",  round(statistics.mean(Q1S3P1_Cup),2))
print("S3P1 stddev: ",round(statistics.stdev(Q1S3P1_Cup),2))
print("S3P2 mean: ",  round(statistics.mean(Q1S3P2_Cup),2))
print("S3P2 stddev: ",round(statistics.stdev(Q1S3P2_Cup),2))
print("S3P3 mean: ",  round(statistics.mean(Q1S3P3_Cup),2))
print("S3P3 stddev: ",round(statistics.stdev(Q1S3P3_Cup),2))
print("===============================================")

print("=================Q1_DOUGH======================")
print("S1P1 mean: ",  round(statistics.mean(Q1S1P1_Dough),2))
print("S1P1 stddev: ",round(statistics.stdev(Q1S1P1_Dough),2))
print("S1P2 mean: ",  round(statistics.mean(Q1S1P2_Dough),2))
print("S1P2 stddev: ",round(statistics.stdev(Q1S1P2_Dough),2))
print("S1P3 mean: ",  round(statistics.mean(Q1S1P3_Dough),2))
print("S1P3 stddev: ",round(statistics.stdev(Q1S1P3_Dough),2))
print("S2P1 mean: ",  round(statistics.mean(Q1S2P1_Dough),2))
print("S2P1 stddev: ",round(statistics.stdev(Q1S2P1_Dough),2))
print("S2P2 mean: ",  round(statistics.mean(Q1S2P2_Dough),2))
print("S2P2 stddev: ",round(statistics.stdev(Q1S2P2_Dough),2))
print("S2P3 mean: ",  round(statistics.mean(Q1S2P3_Dough),2))
print("S2P3 stddev: ",round(statistics.stdev(Q1S2P3_Dough),2))
print("S3P1 mean: ",  round(statistics.mean(Q1S3P1_Dough),2))
print("S3P1 stddev: ",round(statistics.stdev(Q1S3P1_Dough),2))
print("S3P2 mean: ",  round(statistics.mean(Q1S3P2_Dough),2))
print("S3P2 stddev: ",round(statistics.stdev(Q1S3P2_Dough),2))
print("S3P3 mean: ",  round(statistics.mean(Q1S3P3_Dough),2))
print("S3P3 stddev: ",round(statistics.stdev(Q1S3P3_Dough),2))
print("===============================================")

print("===============Q1_STRAWBERRY===================")
print("S1P1 mean: ",  round(statistics.mean(Q1S1P1_Strawberry),2))
print("S1P1 stddev: ",round(statistics.stdev(Q1S1P1_Strawberry),2))
print("S1P2 mean: ",  round(statistics.mean(Q1S1P2_Strawberry),2))
print("S1P2 stddev: ",round(statistics.stdev(Q1S1P2_Strawberry),2))
print("S1P3 mean: ",  round(statistics.mean(Q1S1P3_Strawberry),2))
print("S1P3 stddev: ",round(statistics.stdev(Q1S1P3_Strawberry),2))
print("S2P1 mean: ",  round(statistics.mean(Q1S2P1_Strawberry),2))
print("S2P1 stddev: ",round(statistics.stdev(Q1S2P1_Strawberry),2))
print("S2P2 mean: ",  round(statistics.mean(Q1S2P2_Strawberry),2))
print("S2P2 stddev: ",round(statistics.stdev(Q1S2P2_Strawberry),2))
print("S2P3 mean: ",  round(statistics.mean(Q1S2P3_Strawberry),2))
print("S2P3 stddev: ",round(statistics.stdev(Q1S2P3_Strawberry),2))
print("S3P1 mean: ",  round(statistics.mean(Q1S3P1_Strawberry),2))
print("S3P1 stddev: ",round(statistics.stdev(Q1S3P1_Strawberry),2))
print("S3P2 mean: ",  round(statistics.mean(Q1S3P2_Strawberry),2))
print("S3P2 stddev: ",round(statistics.stdev(Q1S3P2_Strawberry),2))
print("S3P3 mean: ",  round(statistics.mean(Q1S3P3_Strawberry),2))
print("S3P3 stddev: ",round(statistics.stdev(Q1S3P3_Strawberry),2))
print("===============================================")

print("===============Q1_RASPBERRY====================")
print("S1P1 mean: ",  round(statistics.mean(Q1S1P1_Raspberry),2))
print("S1P1 stddev: ",round(statistics.stdev(Q1S1P1_Raspberry),2))
print("S1P2 mean: ",  round(statistics.mean(Q1S1P2_Raspberry),2))
print("S1P2 stddev: ",round(statistics.stdev(Q1S1P2_Raspberry),2))
print("S1P3 mean: ",  round(statistics.mean(Q1S1P3_Raspberry),2))
print("S1P3 stddev: ",round(statistics.stdev(Q1S1P3_Raspberry),2))
print("S2P1 mean: ",  round(statistics.mean(Q1S2P1_Raspberry),2))
print("S2P1 stddev: ",round(statistics.stdev(Q1S2P1_Raspberry),2))
print("S2P2 mean: ",  round(statistics.mean(Q1S2P2_Raspberry),2))
print("S2P2 stddev: ",round(statistics.stdev(Q1S2P2_Raspberry),2))
print("S2P3 mean: ",  round(statistics.mean(Q1S2P3_Raspberry),2))
print("S2P3 stddev: ",round(statistics.stdev(Q1S2P3_Raspberry),2))
print("S3P1 mean: ",  round(statistics.mean(Q1S3P1_Raspberry),2))
print("S3P1 stddev: ",round(statistics.stdev(Q1S3P1_Raspberry),2))
print("S3P2 mean: ",  round(statistics.mean(Q1S3P2_Raspberry),2))
print("S3P2 stddev: ",round(statistics.stdev(Q1S3P2_Raspberry),2))
print("S3P3 mean: ",  round(statistics.mean(Q1S3P3_Raspberry),2))
print("S3P3 stddev: ",round(statistics.stdev(Q1S3P3_Raspberry),2))
print("===============================================")

print("=================Q1_CABLE======================")
print("S1P1 mean: ",  round(statistics.mean(Q1S1P1_Cable),2))
print("S1P1 stddev: ",round(statistics.stdev(Q1S1P1_Cable),2))
print("S1P2 mean: ",  round(statistics.mean(Q1S1P2_Cable),2))
print("S1P2 stddev: ",round(statistics.stdev(Q1S1P2_Cable),2))
print("S1P3 mean: ",  round(statistics.mean(Q1S1P3_Cable),2))
print("S1P3 stddev: ",round(statistics.stdev(Q1S1P3_Cable),2))
print("S2P1 mean: ",  round(statistics.mean(Q1S2P1_Cable),2))
print("S2P1 stddev: ",round(statistics.stdev(Q1S2P1_Cable),2))
print("S2P2 mean: ",  round(statistics.mean(Q1S2P2_Cable),2))
print("S2P2 stddev: ",round(statistics.stdev(Q1S2P2_Cable),2))
print("S2P3 mean: ",  round(statistics.mean(Q1S2P3_Cable),2))
print("S2P3 stddev: ",round(statistics.stdev(Q1S2P3_Cable),2))
print("S3P1 mean: ",  round(statistics.mean(Q1S3P1_Cable),2))
print("S3P1 stddev: ",round(statistics.stdev(Q1S3P1_Cable),2))
print("S3P2 mean: ",  round(statistics.mean(Q1S3P2_Cable),2))
print("S3P2 stddev: ",round(statistics.stdev(Q1S3P2_Cable),2))
print("S3P3 mean: ",  round(statistics.mean(Q1S3P3_Cable),2))
print("S3P3 stddev: ",round(statistics.stdev(Q1S3P3_Cable),2))
print("===============================================")

print("================Q1_PRISM======================")
print("S1P1 mean: ",  round(statistics.mean(Q1S1P1_Prism),2))
print("S1P1 stddev: ",round(statistics.stdev(Q1S1P1_Prism),2))
print("S1P2 mean: ",  round(statistics.mean(Q1S1P2_Prism),2))
print("S1P2 stddev: ",round(statistics.stdev(Q1S1P2_Prism),2))
print("S1P3 mean: ",  round(statistics.mean(Q1S1P3_Prism),2))
print("S1P3 stddev: ",round(statistics.stdev(Q1S1P3_Prism),2))
print("S2P1 mean: ",  round(statistics.mean(Q1S2P1_Prism),2))
print("S2P1 stddev: ",round(statistics.stdev(Q1S2P1_Prism),2))
print("S2P2 mean: ",  round(statistics.mean(Q1S2P2_Prism),2))
print("S2P2 stddev: ",round(statistics.stdev(Q1S2P2_Prism),2))
print("S2P3 mean: ",  round(statistics.mean(Q1S2P3_Prism),2))
print("S2P3 stddev: ",round(statistics.stdev(Q1S2P3_Prism),2))
print("S3P1 mean: ",  round(statistics.mean(Q1S3P1_Prism),2))
print("S3P1 stddev: ",round(statistics.stdev(Q1S3P1_Prism),2))
print("S3P2 mean: ",  round(statistics.mean(Q1S3P2_Prism),2))
print("S3P2 stddev: ",round(statistics.stdev(Q1S3P2_Prism),2))
print("S3P3 mean: ",  round(statistics.mean(Q1S3P3_Prism),2))
print("S3P3 stddev: ",round(statistics.stdev(Q1S3P3_Prism),2))
print("===============================================")


print("==================Q2_PAPER=====================")
print("S1P1 mean: ",  round(statistics.mean(Q2S1P1_Paper),2))
print("S1P1 stddev: ",round(statistics.stdev(Q2S1P1_Paper),2))
print("S1P2 mean: ",  round(statistics.mean(Q2S1P2_Paper),2))
print("S1P2 stddev: ",round(statistics.stdev(Q2S1P2_Paper),2))
print("S1P3 mean: ",  round(statistics.mean(Q2S1P3_Paper),2))
print("S1P3 stddev: ",round(statistics.stdev(Q2S1P3_Paper),2))
print("S2P1 mean: ",  round(statistics.mean(Q2S2P1_Paper),2))
print("S2P1 stddev: ",round(statistics.stdev(Q2S2P1_Paper),2))
print("S2P2 mean: ",  round(statistics.mean(Q2S2P2_Paper),2))
print("S2P2 stddev: ",round(statistics.stdev(Q2S2P2_Paper),2))
print("S2P3 mean: ",  round(statistics.mean(Q2S2P3_Paper),2))
print("S2P3 stddev: ",round(statistics.stdev(Q2S2P3_Paper),2))
print("S3P1 mean: ",  round(statistics.mean(Q2S3P1_Paper),2))
print("S3P1 stddev: ",round(statistics.stdev(Q2S3P1_Paper),2))
print("S3P2 mean: ",  round(statistics.mean(Q2S3P2_Paper),2))
print("S3P2 stddev: ",round(statistics.stdev(Q2S3P2_Paper),2))
print("S3P3 mean: ",  round(statistics.mean(Q2S3P3_Paper),2))
print("S3P3 stddev: ",round(statistics.stdev(Q2S3P3_Paper),2))
print("===============================================")

print("=================Q2_FABRICS====================")
print("S1P1 mean: ",  round(statistics.mean(Q2S1P1_Fabrics),2))
print("S1P1 stddev: ",round(statistics.stdev(Q2S1P1_Fabrics),2))
print("S1P2 mean: ",  round(statistics.mean(Q2S1P2_Fabrics),2))
print("S1P2 stddev: ",round(statistics.stdev(Q2S1P2_Fabrics),2))
print("S1P3 mean: ",  round(statistics.mean(Q2S1P3_Fabrics),2))
print("S1P3 stddev: ",round(statistics.stdev(Q2S1P3_Fabrics),2))
print("S2P1 mean: ",  round(statistics.mean(Q2S2P1_Fabrics),2))
print("S2P1 stddev: ",round(statistics.stdev(Q2S2P1_Fabrics),2))
print("S2P2 mean: ",  round(statistics.mean(Q2S2P2_Fabrics),2))
print("S2P2 stddev: ",round(statistics.stdev(Q2S2P2_Fabrics),2))
print("S2P3 mean: ",  round(statistics.mean(Q2S2P3_Fabrics),2))
print("S2P3 stddev: ",round(statistics.stdev(Q2S2P3_Fabrics),2))
print("S3P1 mean: ",  round(statistics.mean(Q2S3P1_Fabrics),2))
print("S3P1 stddev: ",round(statistics.stdev(Q2S3P1_Fabrics),2))
print("S3P2 mean: ",  round(statistics.mean(Q2S3P2_Fabrics),2))
print("S3P2 stddev: ",round(statistics.stdev(Q2S3P2_Fabrics),2))
print("S3P3 mean: ",  round(statistics.mean(Q2S3P3_Fabrics),2))
print("S3P3 stddev: ",round(statistics.stdev(Q2S3P3_Fabrics),2))
print("===============================================")

print("====================Q2_CUP=====================")
print("S1P1 mean: ",  round(statistics.mean(Q2S1P1_Cup),2))
print("S1P1 stddev: ",round(statistics.stdev(Q2S1P1_Cup),2))
print("S1P2 mean: ",  round(statistics.mean(Q2S1P2_Cup),2))
print("S1P2 stddev: ",round(statistics.stdev(Q2S1P2_Cup),2))
print("S1P3 mean: ",  round(statistics.mean(Q2S1P3_Cup),2))
print("S1P3 stddev: ",round(statistics.stdev(Q2S1P3_Cup),2))
print("S2P1 mean: ",  round(statistics.mean(Q2S2P1_Cup),2))
print("S2P1 stddev: ",round(statistics.stdev(Q2S2P1_Cup),2))
print("S2P2 mean: ",  round(statistics.mean(Q2S2P2_Cup),2))
print("S2P2 stddev: ",round(statistics.stdev(Q2S2P2_Cup),2))
print("S2P3 mean: ",  round(statistics.mean(Q2S2P3_Cup),2))
print("S2P3 stddev: ",round(statistics.stdev(Q2S2P3_Cup),2))
print("S3P1 mean: ",  round(statistics.mean(Q2S3P1_Cup),2))
print("S3P1 stddev: ",round(statistics.stdev(Q2S3P1_Cup),2))
print("S3P2 mean: ",  round(statistics.mean(Q2S3P2_Cup),2))
print("S3P2 stddev: ",round(statistics.stdev(Q2S3P2_Cup),2))
print("S3P3 mean: ",  round(statistics.mean(Q2S3P3_Cup),2))
print("S3P3 stddev: ",round(statistics.stdev(Q2S3P3_Cup),2))
print("===============================================")

print("=================Q2_DOUGH======================")
print("S1P1 mean: ",  round(statistics.mean(Q2S1P1_Dough),2))
print("S1P1 stddev: ",round(statistics.stdev(Q2S1P1_Dough),2))
print("S1P2 mean: ",  round(statistics.mean(Q2S1P2_Dough),2))
print("S1P2 stddev: ",round(statistics.stdev(Q2S1P2_Dough),2))
print("S1P3 mean: ",  round(statistics.mean(Q2S1P3_Dough),2))
print("S1P3 stddev: ",round(statistics.stdev(Q2S1P3_Dough),2))
print("S2P1 mean: ",  round(statistics.mean(Q2S2P1_Dough),2))
print("S2P1 stddev: ",round(statistics.stdev(Q2S2P1_Dough),2))
print("S2P2 mean: ",  round(statistics.mean(Q2S2P2_Dough),2))
print("S2P2 stddev: ",round(statistics.stdev(Q2S2P2_Dough),2))
print("S2P3 mean: ",  round(statistics.mean(Q2S2P3_Dough),2))
print("S2P3 stddev: ",round(statistics.stdev(Q2S2P3_Dough),2))
print("S3P1 mean: ",  round(statistics.mean(Q2S3P1_Dough),2))
print("S3P1 stddev: ",round(statistics.stdev(Q2S3P1_Dough),2))
print("S3P2 mean: ",  round(statistics.mean(Q2S3P2_Dough),2))
print("S3P2 stddev: ",round(statistics.stdev(Q2S3P2_Dough),2))
print("S3P3 mean: ",  round(statistics.mean(Q2S3P3_Dough),2))
print("S3P3 stddev: ",round(statistics.stdev(Q2S3P3_Dough),2))
print("===============================================")

print("===============Q2_STRAWBERRY===================")
print("S1P1 mean: ",  round(statistics.mean(Q2S1P1_Strawberry),2))
print("S1P1 stddev: ",round(statistics.stdev(Q2S1P1_Strawberry),2))
print("S1P2 mean: ",  round(statistics.mean(Q2S1P2_Strawberry),2))
print("S1P2 stddev: ",round(statistics.stdev(Q2S1P2_Strawberry),2))
print("S1P3 mean: ",  round(statistics.mean(Q2S1P3_Strawberry),2))
print("S1P3 stddev: ",round(statistics.stdev(Q2S1P3_Strawberry),2))
print("S2P1 mean: ",  round(statistics.mean(Q2S2P1_Strawberry),2))
print("S2P1 stddev: ",round(statistics.stdev(Q2S2P1_Strawberry),2))
print("S2P2 mean: ",  round(statistics.mean(Q2S2P2_Strawberry),2))
print("S2P2 stddev: ",round(statistics.stdev(Q2S2P2_Strawberry),2))
print("S2P3 mean: ",  round(statistics.mean(Q2S2P3_Strawberry),2))
print("S2P3 stddev: ",round(statistics.stdev(Q2S2P3_Strawberry),2))
print("S3P1 mean: ",  round(statistics.mean(Q2S3P1_Strawberry),2))
print("S3P1 stddev: ",round(statistics.stdev(Q2S3P1_Strawberry),2))
print("S3P2 mean: ",  round(statistics.mean(Q2S3P2_Strawberry),2))
print("S3P2 stddev: ",round(statistics.stdev(Q2S3P2_Strawberry),2))
print("S3P3 mean: ",  round(statistics.mean(Q2S3P3_Strawberry),2))
print("S3P3 stddev: ",round(statistics.stdev(Q2S3P3_Strawberry),2))
print("===============================================")

print("===============Q2_RASPBERRY====================")
print("S1P1 mean: ",  round(statistics.mean(Q2S1P1_Raspberry),2))
print("S1P1 stddev: ",round(statistics.stdev(Q2S1P1_Raspberry),2))
print("S1P2 mean: ",  round(statistics.mean(Q2S1P2_Raspberry),2))
print("S1P2 stddev: ",round(statistics.stdev(Q2S1P2_Raspberry),2))
print("S1P3 mean: ",  round(statistics.mean(Q2S1P3_Raspberry),2))
print("S1P3 stddev: ",round(statistics.stdev(Q2S1P3_Raspberry),2))
print("S2P1 mean: ",  round(statistics.mean(Q2S2P1_Raspberry),2))
print("S2P1 stddev: ",round(statistics.stdev(Q2S2P1_Raspberry),2))
print("S2P2 mean: ",  round(statistics.mean(Q2S2P2_Raspberry),2))
print("S2P2 stddev: ",round(statistics.stdev(Q2S2P2_Raspberry),2))
print("S2P3 mean: ",  round(statistics.mean(Q2S2P3_Raspberry),2))
print("S2P3 stddev: ",round(statistics.stdev(Q2S2P3_Raspberry),2))
print("S3P1 mean: ",  round(statistics.mean(Q2S3P1_Raspberry),2))
print("S3P1 stddev: ",round(statistics.stdev(Q2S3P1_Raspberry),2))
print("S3P2 mean: ",  round(statistics.mean(Q2S3P2_Raspberry),2))
print("S3P2 stddev: ",round(statistics.stdev(Q2S3P2_Raspberry),2))
print("S3P3 mean: ",  round(statistics.mean(Q2S3P3_Raspberry),2))
print("S3P3 stddev: ",round(statistics.stdev(Q2S3P3_Raspberry),2))
print("===============================================")

print("=================Q2_CABLE======================")
print("S1P1 mean: ",  round(statistics.mean(Q2S1P1_Cable),2))
print("S1P1 stddev: ",round(statistics.stdev(Q2S1P1_Cable),2))
print("S1P2 mean: ",  round(statistics.mean(Q2S1P2_Cable),2))
print("S1P2 stddev: ",round(statistics.stdev(Q2S1P2_Cable),2))
print("S1P3 mean: ",  round(statistics.mean(Q2S1P3_Cable),2))
print("S1P3 stddev: ",round(statistics.stdev(Q2S1P3_Cable),2))
print("S2P1 mean: ",  round(statistics.mean(Q2S2P1_Cable),2))
print("S2P1 stddev: ",round(statistics.stdev(Q2S2P1_Cable),2))
print("S2P2 mean: ",  round(statistics.mean(Q2S2P2_Cable),2))
print("S2P2 stddev: ",round(statistics.stdev(Q2S2P2_Cable),2))
print("S2P3 mean: ",  round(statistics.mean(Q2S2P3_Cable),2))
print("S2P3 stddev: ",round(statistics.stdev(Q2S2P3_Cable),2))
print("S3P1 mean: ",  round(statistics.mean(Q2S3P1_Cable),2))
print("S3P1 stddev: ",round(statistics.stdev(Q2S3P1_Cable),2))
print("S3P2 mean: ",  round(statistics.mean(Q2S3P2_Cable),2))
print("S3P2 stddev: ",round(statistics.stdev(Q2S3P2_Cable),2))
print("S3P3 mean: ",  round(statistics.mean(Q2S3P3_Cable),2))
print("S3P3 stddev: ",round(statistics.stdev(Q2S3P3_Cable),2))
print("===============================================")

print("================Q1_PRISM======================")
print("S1P1 mean: ",  round(statistics.mean(Q2S1P1_Prism),2))
print("S1P1 stddev: ",round(statistics.stdev(Q2S1P1_Prism),2))
print("S1P2 mean: ",  round(statistics.mean(Q2S1P2_Prism),2))
print("S1P2 stddev: ",round(statistics.stdev(Q2S1P2_Prism),2))
print("S1P3 mean: ",  round(statistics.mean(Q2S1P3_Prism),2))
print("S1P3 stddev: ",round(statistics.stdev(Q2S1P3_Prism),2))
print("S2P1 mean: ",  round(statistics.mean(Q2S2P1_Prism),2))
print("S2P1 stddev: ",round(statistics.stdev(Q2S2P1_Prism),2))
print("S2P2 mean: ",  round(statistics.mean(Q2S2P2_Prism),2))
print("S2P2 stddev: ",round(statistics.stdev(Q2S2P2_Prism),2))
print("S2P3 mean: ",  round(statistics.mean(Q2S2P3_Prism),2))
print("S2P3 stddev: ",round(statistics.stdev(Q2S2P3_Prism),2))
print("S3P1 mean: ",  round(statistics.mean(Q2S3P1_Prism),2))
print("S3P1 stddev: ",round(statistics.stdev(Q2S3P1_Prism),2))
print("S3P2 mean: ",  round(statistics.mean(Q2S3P2_Prism),2))
print("S3P2 stddev: ",round(statistics.stdev(Q2S3P2_Prism),2))
print("S3P3 mean: ",  round(statistics.mean(Q2S3P3_Prism),2))
print("S3P3 stddev: ",round(statistics.stdev(Q2S3P3_Prism),2))
print("===============================================")




