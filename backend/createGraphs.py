import matplotlib.pyplot as plt
import numpy as np

# Code adapted from notes from another course: https://moody.st-andrews.ac.uk/moodle/pluginfile.php/1788932/mod_resource/content/13/_book/data-visualisation.html

def plotIncomeVsExpenses(income, expenses):
    months = [k for k in range(len(income))]
    
    # create figure and axes
    fig, ax = plt.subplots()
    # plot income over given time
    ax.plot(months, income, label='Income', color='#4daf4a') # colourblind friendly colours used: https://gist.github.com/thriveth/8560036
    ax.scatter(months, income, color='#4daf4a')
    # plot expenses over given time
    plt.plot(months, expenses, label="Expenses", color='#e41a1c')
    plt.scatter(months, expenses, color='#e41a1c')

    # add labels to the x and y axis
    ax.set_xlabel('Months since last Statement')
    ax.set_ylabel('Money')

    # set the title of the figure
    ax.set_title('Income and Expenses over %i months' % len(income)) # title: https://stackoverflow.com/questions/43757820/how-to-add-a-variable-to-python-plt-title

    # add a legend
    ax.legend()

    # TODO: WHAT METHOD OF STORAGE FOR GRAPH TO UPDATE IN REAL TIME
    #plt.savefig('plots/income_expenses.png')
    plt.show()

def plotBankAccount(bank_account):
    months = [k for k in range(len(income))]
    # create figure and axes
    fig, ax = plt.subplots()
    # plot bank account value over given time
    ax.plot(months, bank_account, label='Bank Account Value', color='#377eb8')
    ax.scatter(months, bank_account, color='#377eb8')
    ax.set_xlabel('Months since last Statement')
    ax.set_ylabel('Money')
    ax.set_title('Bank Account Value over %i months' % len(income))
    ax.legend()
    #plt.savefig('plots/time_complexities.png') # TODO: WHAT METHOD OF STORAGE FOR GRAPH TO UPDATE IN REAL TIME
    plt.show()
