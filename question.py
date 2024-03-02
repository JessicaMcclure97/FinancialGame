import json

wellbeing = 100
bank_account = 0

salary = 0
returns = 0

transports = 0
rent = 0
food = 150
#loans = 0
tax = 0
savings = 0
extras = 0
pension = 0
investment = 0
purchase = 0




questions = { 
    
    "nodes": 
    [ 
        { "id": 1, "category" : 1, "sub-category" : 1, "question": "You have decided to move out and become start your journey of being financially independant! What do you want to sort out first?" }, 
        { "id": 2, "category" : 2, "sub-category" : 1, "question": "You have decided to job hunt! You have 3 job offers, with the given tax bracket information which one do you choose? # DO WE HAVE A HELP BUTTON EXPLAINING TAX BRACKETS?" },
        { "id": 3, "category" : 3, "sub-category" : 1, "question": "You have accepted a job offer! Now you should decide what part of your budget to organise first:"},
        { "id": 4, "category" : 4, "sub-category" : 1, "question": "You have decided to sort out your needs! Which would you like to sort out?"},
        { "id": 5, "category" : 5, "sub-category" : 1, "question": "Which house rental and bill option do you choose? Given below"},
        { "id": 6, "category" : 5, "sub-category" : 2, "question": "Which mode of transportation do you choose?"},
        { "id": 7, "category" : 4, "sub-category" : 2, "question": "You have decided to sort out your future! Which would you like to sort out?"},
        { "id": 8, "category" : 5, "sub-category" : 3, "question": "How much do you decide to transfer to your savings account per month:"},

        { "id": 10, "category" : 5, "sub-category" : 5, "question": "Choose your pension plan:"},
        { "id": 11, "category" : 4, "sub-category" : 3, "question": "You have decided to sort out your extra expenses! Which would you like to sort out?"},
        { "id": 12, "category" : 5, "sub-category" : 6, "question": "How often and how much do you choose to spend on a holiday?"},
        { "id": 13, "category" : 5, "sub-category" : 7, "question": "How expensive are your hobbies per month?"},
        { "id": 14, "category" : 5, "sub-category" : 8, "question": "How much on average do you want to spend per month going out? For example to the cinema, eating at restaurants or getting takeout, getting your hair cut"},
    ],
    
    "edges": 
    [
        {"source": 1, "option_id": 1, "option_label": "Rent a property [Advice about sorting out income before making decisions that result in expenses]", "target": 0},
        {"source": 1, "option_id": 2, "option_label": "Get a job", "target": 2},

        {"source": 2, "option_id": 3, "option_label": "£36k ~ you are in the basic tax bracket (20%)", "target": 3, "variables": ["salary", "tax"], "amount": [3000, 267]},
        {"source": 2, "option_id": 4, "option_label": "£42k ~ you are in the modified rate tax bracket (30%)", "target": 3, "variables": ["salary", "tax"], "amount": [3500, 383]},
        {"source": 2, "option_id": 5, "option_label": "£51k ~ you are in the higher rate tax bracket (45%)", "target": 3, "variables": ["salary", "tax"], "amount": [4250, 420]},

        {"source": 3, "option_id": 6, "option_label": "Needs (i.e. rent, bills, food, transport)", "target": 4},
        {"source": 3, "option_id": 7, "option_label": "Future (i.e. savings, investments, pension)", "target": 7},
        {"source": 3, "option_id": 8, "option_label": "Extras (i.e. going out, holidays, hobbies)", "target": 0},

        {"source": 4, "option_id": 9, "option_label": "Rent & bills", "target": 5},
        {"source": 4, "option_id": 10, "option_label": "Transport", "target": 6},

        {"source": 5, "option_id": 11, "option_label": "Basic (£550)", "target": 4, "variables": ["rent"], "amount": [550]},
        {"source": 5, "option_id": 12, "option_label": "Intermediate (£625)", "target": 4, "variables": ["rent"], "amount": [625]},
        {"source": 5, "option_id": 13, "option_label": "Fancy (£800)", "target": 4, "variables": ["rent"], "amount": [800]},

        {"source": 6, "option_id": 14, "option_label": "Cycle (Initial bike cost £200) [worst wellbeing wise]", "target": 3, "variables": ["transport", "purchase"], "amount": [0, 200]},
        {"source": 6, "option_id": 15, "option_label": "Public transport (monthly ticket cost of £40 and no maintenance)", "target": 3, "variables": ["transport", "purchase"], "amount": [40, 0]},
        {"source": 6, "option_id": 16, "option_label": "Buy Car (large initial cost £8k, maintenance £15 and insurance £35)", "target": 3, "variables": ["transport", "purchase"], "amount": [50, 8000]},
        {"source": 6, "option_id": 17, "option_label": "Lease Car (monthly cost £380, maintenance £12 and insurance £34)", "target": 3, "variables": ["transport", "purchase"], "amount": [426, 0]},

        {"source": 7, "option_id": 18, "option_label": "Savings", "target": 8},
        {"source": 7, "option_id": 19, "option_label": "Investments", "target": 9},
        {"source": 7, "option_id": 20, "option_label": "Pension", "target": 10},

        {"source": 8, "option_id": 21, "option_label": "£0", "target": 7, "variables": ["savings"], "amount": [0]},
        {"source": 8, "option_id": 22, "option_label": "£50", "target": 7, "variables": ["savings"], "amount": [50]},
        {"source": 8, "option_id": 23, "option_label": "£100", "target": 7, "variables": ["savings"], "amount": [100]},

        {"source": 10, "option_id": 24, "option_label": "Defined contribution pension", "target": 7, "variables": ["pension"], "amount": [0]},
        {"source": 10, "option_id": 25, "option_label": "Defined benefit pension", "target": 7, "variables": ["pension"], "amount": [50]},
        {"source": 10, "option_id": 26, "option_label": "State pension", "target": 7, "variables": ["pension"], "amount": [100]},

        {"source": 11, "option_id": 27, "option_label": "Holiday", "target": 12},
        {"source": 11, "option_id": 28, "option_label": "Hobbies", "target": 13},
        {"source": 11, "option_id": 29, "option_label": "Going out (i.e. restaurants, cinema)", "target": 14},

        {"source": 12, "option_id": 30, "option_label": "No holiday", "target": 11, "variables": ["extras"], "amount": [0]},
        {"source": 12, "option_id": 31, "option_label": "Small holiday (£300/year)", "target": 11, "variables": ["extras"], "amount": [25]},
        {"source": 12, "option_id": 32, "option_label": "Medium holiday (£800/year)", "target": 11, "variables": ["extras"], "amount": [67]},
        {"source": 12, "option_id": 33, "option_label": "Big holiday (£1200/year)", "target": 11, "variables": ["extras"], "amount": [100]},

        {"source": 13, "option_id": 34, "option_label": "£0", "target": 11, "variables": ["extras"], "amount": [0]},
        {"source": 13, "option_id": 35, "option_label": "£20", "target": 11, "variables": ["extras"], "amount": [20]},
        {"source": 13, "option_id": 36, "option_label": "£50", "target": 11, "variables": ["extras"], "amount": [50]},
        {"source": 13, "option_id": 37, "option_label": "£80", "target": 11, "variables": ["extras"], "amount": [80]},

        {"source": 14, "option_id": 38, "option_label": "£15", "target": 11, "variables": ["extras"], "amount": [15]},
        {"source": 14, "option_id": 39, "option_label": "£30", "target": 11, "variables": ["extras"], "amount": [30]},
        {"source": 14, "option_id": 40, "option_label": "£50", "target": 11, "variables": ["extras"], "amount": [50]},
        {"source": 14, "option_id": 41, "option_label": "£100", "target": 11, "variables": ["extras"], "amount": [100]}
    ]   

}


json_object = json.dumps(questions, indent=5)

with open("sample.json", "w") as outfile:
    outfile.write(json_object)


def outcome(var_name, amount):
    for i in range(len(var_name)):
        if var_name[i] == "salary":
            global salary
            salary = amount[i]
        elif var_name[i] == "transports":
            global transports
            transports = amount[i]
        elif var_name[i] == "rent":
            global rent
            rent = amount[i]
        elif var_name[i] == "tax":
            global tax 
            tax = amount[i]
        elif var_name[i] == "savings":
            global savings
            savings = amount[i]
        elif var_name[i] == "investment":
            global investment
            investment = amount[i]
        elif var_name[i] == "purchase":
            global purchase
            purchase = amount[i]
        elif var_name[i] == "extras":
            global extras
            extras += amount[i]

# id = questions["edges"][21]
# outcome(id["variables"], id["amount"])
