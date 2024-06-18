import matplotlib.pyplot as plt

def plot_data(data):
    # Example of a bar chart
    categories = ['A', 'B', 'C', 'D']
    plt.bar(categories, data)
    plt.xlabel('Category')
    plt.ylabel('Values')
    plt.title('Bar Chart Example')
    plt.show()

# Usage
data = [10, 20, 15, 25]
plot_data(data)
