
import statistics
import numpy as np
import matplotlib.pyplot as plt
import stemgraphic


def solve(data):
    #call each of the functions for each data set
    
    #number of data points in the set
    x = len(data)
    print("\n ")
    print("The number of data points in the set is: ", x)
    print("\n ")
    mean(data)
    mode(data)
    stdev(data)
    variance(data)
    
    
    IQR(data,x)
    median2(data)
    print("\n ")
    boxplot(data)
    print("\n ")
    print( stemplot(data) )

def mean(data):
    x = statistics.mean(data)
    x = round(x,3)
    print("The mean is : ", x)     

def median2(data):
    x = statistics.median(data)
    print("The median is: ",x)

def mode(data):
    x = statistics.mode(data)
    print("The mode is: ",x)

def stdev(data):
    x = statistics.stdev(data)
    x = round(x,3)
    print("The standard deviation is: ",x)

def variance(data):
    x = statistics.variance(data)
    x = round(x,3)
    print("The variance is: ",x)
  
def median(a, l, r): #Helper method for IQR to find median
    n = r - l + 1
    n = (n + 1) // 2 - 1
    return n + l 

    
def IQR(data, n): 
    data.sort() 
      
    # Index of median of entire data 
    mid_index = median(data, 0, n) 
  
    # Median of first half 
    Q1 = data[median(data, 0, mid_index)] 
  
    # Median of second half 
    Q3 = data[median(data, mid_index + 1, n)] 
    
    IQRvalue = Q3-Q1
    IQRvalue = round(IQRvalue, 3)
    print("\n ")
    print("The min value is: ",min(data))
    print("Q1 is: ",Q1)
    print("Q3 is: ",Q3)
    print("The IQR is: ",IQRvalue)
    print("The max value is: ",max(data))
  
def boxplot(data):
    fig4, ax4 = plt.subplots()
    ax4.set_title('Boxplot')
    ax4.boxplot(data, vert=False, showfliers=False)
    
def stemplot(data):
    stemgraphic.stem_graphic(data, scale = 10) 



data1 = [4.6, 12.3, 7.1, 7.0, 4.0, 9.2, 6.7, 6.9, 11.5, 5.1, 11.2, 10.5, 14.3,
            8.0, 8.8, 6.4, 5.1, 5.6, 9.6, 7.5, 0.2, 1.6, 7.5, 6.2, 5.8, 2.3, 3.4,
            10.4, 9.8, 6.6, 3.7, 6.4, 8.3, 6.5, 7.6, 9.3, 9.2, 7.3, 5.0, 6.3, 13.8,
            6.2, 23.4, 0.4, 31.1, 5.4, 4.8, 7.5, 6.0, 6.9, 10.8, 7.5, 6.6, 5.0,
            3.3, 7.6, 3.9, 11.9, 2.2, 15.0, 7.2, 6.1, 15.3, 18.9, 7.2, 26.7, 5.4,
            5.5, 4.3, 9.0, 12.7, 11.3, 7.4, 5.0, 3.5, 8.2, 8.4, 7.3, 10.3, 11.9,
            6.0, 5.6, 9.5, 9.3, 10.4, 9.7, 1.2, 0.8, 5.1, 6.7, 10.2, 6.2, 8.4,
            7.0, 4.8, 5.6, 10.5, 14.6, 10.8, 15.5, 7.5, 6.4, 3.4, 5.5, 6.6, 5.9,
            15.0, 9.6, 18.2, 7.8, 7.0, 6.9, 4.1, 3.6, 11.9, 3.7, 5.7, 33.1, 6.8,
            11.3, 9.3, 9.6, 10.4, 9.3, 6.9, 9.8, 9.1, 10.6, 4.5, 6.2, 26.1, 8.3,
            3.2, 4.9, 5.0, 2.5, 6.0, 8.2, 6.3, 3.8, 6.0, 1.5, 3.1]
    
print("Now running calculations for problem #1")
solve(data1)
