import matplotlib.pyplot as p
# Create a function that will evaluate f(n) for specific values of n
def f(n):
    if n<=9: #Condition where n is less than or equal to 9
        return((n**2)-7)
    return f(n-10) # n is reduced by 10 if n>9 and returns the main function f(n), where it is evluated again

# condition wherein the main function f(n) is called, so that f(n) can be evaluated
if __name__ == '__main__':
    #create and empty array for the x-values(n-values) and another for the corresponding y-value evaluated from the function f(n)
    x = []
    y = []
    for i in range(0,100): #range i from 0 to 99 will serve as the value for n 
        # append the values of m t array x
        x.append(i)
        # append the values of f(i) to array y, where the value of f(i) comes from the main function f(n)
        y.append(f(i))
        
        # show the graph of f(n) from n = 0 to n = 99
        p.stem(x,y,use_line_collection=True) #PLot the graph using stem() and insert use_line_collection=True to plot the graph faster
        p.xlabel("n") #label the x-axis 'n'
        p.ylabel("f(n)") #label the y-axis 'f(n)'
        p.title("Graph of f(n) from n = 0 to n = 99") #set the title of the graph
        p.show #show the plot
        
    