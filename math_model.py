import statistics
import matplotlib.pyplot as plt
import stemgraphic
import math

def solve(data):
    #call each of the functions for each data set
    
    #number of data points in the set
    x = len(data)
    print("\n ")
    print("The number of data points in the set is: ", x)
    print("\n ")
    mean(data)
    median2(data)
    try:
        mode(data)
    except:
        print("Mode: There is no mode for this data set")
    stdev(data)
    variance(data)
    
    
    IQR(data,x)
    print("\n ")
    boxplot(data)
    print("\n ")
    print( stemplot(data) )
    print("\n ")
    print( histogram(data, x) )
    print("\n ")
    print( ogive(data,x) )

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
    
    upperOut = (1.5*IQRvalue)+Q3
    upperOut = round(upperOut, 3)
    
    lowerOut = Q1-(1.5*IQRvalue)
    lowerOut = round(lowerOut, 3)
    
    print("\n ")
    print("The min value is: ",min(data))
    print("Q1 is: ",Q1)
    print("Q2 is: ",data[mid_index])
    print("Q3 is: ",Q3)
    print("The IQR is: ",IQRvalue)
    print("The max value is: ",max(data))
    print("The upper bound outliers would be any number higher than: ",upperOut)
    print("The lower bound outliers would be any number lower than: ",lowerOut)
    
def boxplot(data):
    fig4, ax4 = plt.subplots()
    ax4.set_title('Boxplot')
    ax4.boxplot(data, vert=False, showfliers=False)
    plt.show()
    
def stemplot(data):
    stemgraphic.stem_graphic(data, scale = 1) 

def histogram(data, x):
    n_bins = int(math.sqrt(x))
    plt.hist(x, n_bins)
    plt.show()
    
    
def ogive(data, x):
    fig, ax = plt.subplots()
    n_bins = int(math.sqrt(x))

    # plot the cumulative histogram
    n, bins, patches = ax.hist(data, n_bins, density=True, histtype='step',
    cumulative=True, label='Ogive')
    plt.show()

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

data2 = [16.35, 18.85, 16.20, 17.75, 19.58, 17.73, 22.75, 23.78, 9.12, 10.22, 
         23.25, 19.08, 19.62, 33.05, 19.20, 20.05, 17.85, 19.17, 19.48, 20.00, 
         19.97, 42.13, 11.42, 03.28, 41.56, 17.48, 17.15, 19.07, 19.90, 18.68,
         18.82, 19.03, 19.45, 19.37, 19.20, 18.00, 19.60, 19.33, 21.22, 19.50,
         15.30, 22.25] 

data3 = [1067, 919, 1196, 785, 1126, 936, 918, 1156, 920, 948, 855, 1092, 1162,
         1170, 929, 950, 905, 972, 1035, 1045, 1157, 1195, 1195, 1340, 1122,
         938, 970, 1237, 956, 1102, 1022, 978, 832, 1009, 1157, 1151, 1009,
         765, 958, 902, 923, 1333, 811, 1217, 1085, 896, 958, 1311, 1037, 702,
         521, 933, 928, 1153, 946, 858, 1071, 1069, 830, 1063, 930, 807, 954,
         1063, 1002, 909, 1077, 1021,1062, 1157, 999, 932, 1035, 944, 1049,
         940, 1122, 1115, 833, 1320, 901, 1324, 818, 1250, 1203, 1078, 890,
         1303, 1011, 1102, 996, 780, 900, 1106, 704, 621, 854, 1178, 1138, 951,
         1187, 1067, 1118, 1037, 958, 760, 1101, 949, 992, 966, 824, 653, 980,
         935, 878, 934, 910, 1058, 730, 980, 844, 814, 1103, 1000, 788, 1143,
         935, 1069, 1170, 1067, 1037, 1151, 863, 990, 1035, 1112, 931, 970,
         932, 904, 1026, 1147, 883, 867, 990, 1258, 1192, 922, 1150, 1091,
         1039, 1083, 1040, 1289, 699, 1083, 880, 1029, 658, 912, 1023, 984,
         856, 924, 801, 1122, 1292, 1116, 880, 1173, 1134, 932, 938, 1078,
         1180, 1106, 1184, 954, 824, 529, 998, 996, 1133, 765, 775, 1105,
         1081, 1171, 705, 1425, 610, 916, 1001, 895, 709, 860, 1110,
         1149, 972, 1002]


print("Now running calculations for problem #1")
solve(data1)
print("\nNow running calculations for problem #2")
solve(data2)
print("\nNow running calculations for problem #3")
solve(data3)
