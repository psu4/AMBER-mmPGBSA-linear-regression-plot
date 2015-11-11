# Amber MMP(G)BSA Energy Terms Post Processing: Linear Regression Plot

# Written by Pin-Chih Su. Last modified on Nov 11,2015

# Tested in python 2.7.6, scipy-0.13.3, matplotlib.pyplot-1.3.1, and Linux Redhat 5.0/Windows 7

from scipy import stats

import matplotlib.pyplot as plt

import pylab

import csv         

import sys, getopt

def main(argv):
    
    inputfile = ''
   
    outputfile = ''
   
    try:
       
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
      
    except getopt.GetoptError:
       
        print 'python mmPBSA_linear_regression.py -i <inputfile> -o <outputfile>'
      
        sys.exit(2)
      
    for opt, arg in opts:
       
        if opt == '-h':
          
            print '\n'+'(1) Usage: python mmPBSA_linear_regression.py -i <inputfile> -o <outputfile>'

            print '\n'+'(2) Output plots are jpg files'
            
            print '\n'+'(3) Please make sure you have python, scipy, matplotlib installed'
            
            print '\n'+'(4) Tested in python 2.7.6, scipy-0.13.3, matplotlib.pyplot-1.3.1, and Linux Redhat 5.0/Windows 7'

            print '\n'+'(5) Written by Dr.Pin-Chih Su and Cheng-Chieh Tsai'

            print '\n'+'(6) If you use this script, please cite: Journal of Computational Chemistry, 2015, 36,1859-1873'

            sys.exit()
         
        elif opt in ("-i", "--ifile"):
          
            inputfile = arg
         
        elif opt in ("-o", "--ofile"):
          
            outputfile = arg

    file=open(inputfile,'r')

    dg_e=[]

    dg_c=[]
            
    for row in csv.reader(file):

        dg_e.append(float(row[1])) # Read the 2rd column of the csv (experimental dG)

        dg_c.append(float(row[2])) # Read the 3rd column of the csv (calculated dG)

# Calculate statistical values

    slope, intercept, r_value, p_value, std_err = stats.linregress(dg_e,dg_c)

# Plot 

    pylab.title("Linear Regression "+"R^2"+" "+"="+" "+str("%.2f" %(r_value**2))) # plot title

    pylab.xlabel('Experimental Binding Free Energy (kcal/mol)')         # xlabel

    pylab.ylabel('Predicted Binding Free Energy (kcal/mol)')            # ylable     

    pylab.plot(dg_e,dg_c,'ko')  # Plot data points

##    print dg_e

# ko means black filled circle. More option please consult  http://matplotlib.org/api/pyplot_api.html 

    line=[]

    predict_y=[]

    for each in dg_e:

        predict_y.append(intercept+slope*each)  # Plot the regression line

    pylab.plot(dg_e, predict_y, 'k-')   # k- = black solid line. More option please consult  http://matplotlib.org/api/pyplot_api.html

    plt.savefig(outputfile+".jpg")  # save the plot

    plt.clf()

if __name__ == "__main__":
    
   main(sys.argv[1:])

