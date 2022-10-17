'''
Compare distances at start and end
Choose the largest one
'''
import math

kx0, ky0, ox0, oy0, kx1, ky1, ox1, oy1 = input().split()

print(max(
    math.sqrt((int(kx0) - int(ox0))**2 + (int(ky0) - int(oy0))**2), 
    math.sqrt((int(kx1) - int(ox1))**2 + (int(ky1) - int(oy1))**2)
))