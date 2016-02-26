#!/usr/bin/env python


def FuncOut(name,age):

    print " HI! my name is ", name + " and my age is ",age
    print " HI! my name is %s  and my age is %d" %(name,age)
    print " HI! my name is {} and my age is{}".format(name,age)

FuncOut("Mary",19)
