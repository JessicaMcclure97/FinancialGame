from django.shortcuts import render
import json

# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

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
        { "id": 9, "category" : 5, "sub-category" : 4, "question": "Choose your investment plan:"},
        { "id": 10, "category" : 5, "sub-category" : 5, "question": "Choose your pension plan:"},
        { "id": 11, "category" : 4, "sub-category" : 3, "question": "You have decided to sort out your extra expenses! Which would you like to sort out?"},
        { "id": 12, "category" : 5, "sub-category" : 6, "question": "How often and how much do you choose to spend on a holiday?"},
        { "id": 13, "category" : 5, "sub-category" : 7, "question": "How expensive are your hobbies per month?"},
        { "id": 14, "category" : 5, "sub-category" : 8, "question": "How much on average do you want to spend per month going out? For example to the cinema, eating at restaurants or getting takeout, getting your hair cut"},
    ],
    
"edges": 
[
    {"source": 1, "option_id": 1, "option_label": "Rent a property [Advice about sorting out income before making decisions that result in expenses]", "target": 1},
    {"source": 1, "option_id": 2, "option_label": "Get a job", "target": 2},

    {"source": 2, "option_id": 3, "option_label": "£36k ~ you are in the basic tax bracket (20%)", "target": 3, "variables": ["salary", "tax"], "amount": [3000, 267]},
    {"source": 2, "option_id": 4, "option_label": "£42k ~ you are in the modified rate tax bracket (30%)", "target": 3, "variables": ["salary", "tax"], "amount": [3500, 383]},
    {"source": 2, "option_id": 5, "option_label": "£51k ~ you are in the higher rate tax bracket (45%)", "target": 3, "variables": ["salary", "tax"], "amount": [4250, 420]},

    {"source": 3, "option_id": 6, "option_label": "Needs (i.e. rent, bills, food, transport)", "target": 4},
    {"source": 3, "option_id": 7, "option_label": "Future (i.e. savings, investments, pension)", "target": 7},
    {"source": 3, "option_id": 8, "option_label": "Extras (i.e. going out, holidays, hobbies)", "target": 11},

    {"source": 4, "option_id": 9, "option_label": "Rent & bills", "target": 5},
    {"source": 4, "option_id": 10, "option_label": "Transport", "target": 6},
    {"source": 4, "option_id": 11, "option_label": "Back", "target": 3},

    {"source": 5, "option_id": 12, "option_label": "Basic (£650)", "target": 4, "variables": ["rent", "wellbeing"], "amount": [650, -3]},
    {"source": 5, "option_id": 13, "option_label": "Intermediate (£800)", "target": 4, "variables": ["rent", "wellbeing"], "amount": [800,1]},
    {"source": 5, "option_id": 14, "option_label": "Fancy (£1100)", "target": 4, "variables": ["rent", "wellbeing"], "amount": [1100,3]},

    {"source": 6, "option_id": 15, "option_label": "Cycle (Initial bike cost £200) [worst wellbeing wise]", "target": 4, "variables": ["transport", "purchase", "wellbeing"], "amount": [0, 200,-3]},
    {"source": 6, "option_id": 16, "option_label": "Public transport (monthly ticket cost of £50 and no maintenance)", "target": 4, "variables": ["transport", "purchase", "wellbeing"], "amount": [50, 0,-1]},
    {"source": 6, "option_id": 17, "option_label": "Buy Car (large initial cost £8k, maintenance £30 and insurance £50)", "target": 4, "variables": ["transport", "purchase", "wellbeing"], "amount": [80, 8000,3]},
    {"source": 6, "option_id": 18, "option_label": "Lease Car (monthly cost £380, maintenance £30 and insurance £50)", "target": 4, "variables": ["transport", "purchase", "wellbeing"], "amount": [450, 0,3]},

    {"source": 7, "option_id": 19, "option_label": "Savings", "target": 8},
    {"source": 7, "option_id": 20, "option_label": "Investments", "target": 9},
    {"source": 7, "option_id": 21, "option_label": "Pension", "target": 10},
    {"source": 7, "option_id": 22, "option_label": "Back", "target": 3},

    {"source": 8, "option_id": 23, "option_label": "£0", "target": 7, "variables": ["savings"], "amount": [0]},
    {"source": 8, "option_id": 24, "option_label": "£150", "target": 7, "variables": ["savings"], "amount": [50]},
    {"source": 8, "option_id": 25, "option_label": "£300", "target": 7, "variables": ["savings"], "amount": [100]},

    {"source": 9, "option_id": 26, "option_label": "Compounded annually at 5% per year (interest is calculated and added to your account once each year)", "target": 7, "variables": ["investment"], "amount": [1.00407]}, #(1 + 0.05)^(1/12)
    {"source": 9, "option_id": 27, "option_label": "Compunded each quarter at 5% per year (interested is calculated and added to your account 3 times per year)", "target": 7, "variables": ["investment"], "amount": [1.00414]}, #(1 + 0.05/3)^(1/4)

    {"source": 10, "option_id": 28, "option_label": "Defined contribution pension", "target": 7, "variables": ["pension"], "amount": [0]},
    {"source": 10, "option_id": 29, "option_label": "Defined benefit pension", "target": 7, "variables": ["pension"], "amount": [150]},
    {"source": 10, "option_id": 30, "option_label": "State pension", "target": 7, "variables": ["pension"], "amount": [300]},

    {"source": 11, "option_id": 31, "option_label": "Holiday", "target": 12},
    {"source": 11, "option_id": 32, "option_label": "Hobbies", "target": 13},
    {"source": 11, "option_id": 33, "option_label": "Going out (i.e. restaurants, cinema)", "target": 14},
    {"source": 11, "option_id": 34, "option_label": "Back", "target": 3},

    {"source": 12, "option_id": 35, "option_label": "No holiday", "target": 11, "variables": ["extras", "wellbeing"], "amount": [0,-3]},
    {"source": 12, "option_id": 36, "option_label": "Small holiday (£400/year)", "target": 11, "variables": ["extras", "wellbeing"], "amount": [34,-1]},
    {"source": 12, "option_id": 37, "option_label": "Medium holiday (£800/year)", "target": 11, "variables": ["extras", "wellbeing"], "amount": [67,1]},
    {"source": 12, "option_id": 38, "option_label": "Big holiday (£1800/year)", "target": 11, "variables": ["extras", "wellbeing"], "amount": [150,3]},

    {"source": 13, "option_id": 39, "option_label": "£0", "target": 11, "variables": ["extras","wellbeing"], "amount": [0,-3]},
    {"source": 13, "option_id": 40, "option_label": "£30", "target": 11, "variables": ["extras", "wellbeing"], "amount": [30,-1]},
    {"source": 13, "option_id": 41, "option_label": "£60", "target": 11, "variables": ["extras", "wellbeing"], "amount": [60,1]   },
    {"source": 13, "option_id": 42, "option_label": "£120", "target": 11, "variables": ["extras", "wellbeing"], "amount": [120,3]},

    {"source": 14, "option_id": 43, "option_label": "£30", "target": 11, "variables": ["extras", "wellbeing"], "amount": [30,-3]},
    {"source": 14, "option_id": 44, "option_label": "£75", "target": 11, "variables": ["extras", "wellbeing"], "amount": [75,-1]},
    {"source": 14, "option_id": 45, "option_label": "£150", "target": 11, "variables": ["extras", "wellbeing"], "amount": [150,1]},
    {"source": 14, "option_id": 46, "option_label": "£250", "target": 11, "variables": ["extras", "wellbeing"], "amount": [250,3]}
]
}


json_object = json.dumps(questions, indent=5)

with open("sample.json", "w") as outfile:
    outfile.write(json_object)


# APIs 
@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, world!'})

@api_view(['GET'])
def get_question(request):
    print("HERE")
    print(request.GET.get('state'))
    # Get parameters 
    #json_data = json.loads(request.text)
    currentQuestion = int(request.GET.get('currentQuestion'))
    chosenOption = json.loads(request.GET.get('chosenOption'))
    state = json.loads(request.GET.get('state'))

    print(f"cureent q = {currentQuestion} ")
    print(f"option =  {chosenOption} ")
    print(f"State = {state}")

    # First Question therefore just need to get the first question!
    if currentQuestion == 0 :
        for Q in questions["nodes"]:
            if Q["id"] == 1:
                q_return = Q
                break

        o_return = []
        for option in questions["edges"]:
            if option["source"] == Q["id"]:
                o_return.append(option)

        response = {"question" : q_return, "options" : o_return, "state" : state}

    else:
        # get the new state 
        print(type(state))
        new_state = outcome(chosenOption, state)
        #Get the next question using the new state 
        response = next_question(chosenOption, new_state)

    return JsonResponse(response)


# Methods 
def get_option(op_id):
    for option in questions["edges"]:
        if option["option_id"] == op_id:
            selected_option = option
            break
    return selected_option


def outcome(selected_option, global_vars):

    try:
        var_name = selected_option["variables"]
    except:
        var_name = ""
    try:
        amount = selected_option["amount"]
    except:
        var_name = ""

    wellbeing_change = 0
    global_vars_updated = global_vars
    global_vars_updated["purchase"] = 0

    for i in range(len(var_name)):
        if var_name[i] == "salary":
            global_vars_updated["salary"] = amount[i]
        elif var_name[i] == "transports":
            global_vars_updated["transports"] = amount[i]
        elif var_name[i] == "rent":
            global_vars_updated["rent"] = amount[i]
        elif var_name[i] == "tax":
            global_vars_updated["tax"] = amount[i]
        elif var_name[i] == "savings":
            global_vars_updated["savings"] = amount[i]
        elif var_name[i] == "investment":
            global_vars_updated["investment"] = amount[i]
        elif var_name[i] == "purchase":
            global_vars_updated["purchase"] = amount[i]
        elif var_name[i] == "extras":
            global_vars_updated["extras"] += amount[i]
        elif var_name[i] == "pension":
            global_vars_updated["pension"] += amount[i]
        elif var_name[i] == "amount_saved":
            global_vars_updated["amount_saved"] += global_vars_updated["savings"]
        elif var_name[i] == "amount_invested":
            global_vars_updated["amount_invested"] += global_vars_updated["investment"]
        elif var_name[i] == "wellbeing":
            wellbeing_change += amount[i]

    global_vars_updated["wellbeing"] = min(100, global_vars_updated["wellbeing"] + wellbeing_change)
     #returns = xxx
    
    income = global_vars_updated["salary"]  #+ returns
    expenses = global_vars_updated["transports"] + global_vars_updated["rent"] + global_vars_updated["food"] + global_vars_updated["tax"] + global_vars_updated["savings"] + global_vars_updated["extras"] + global_vars_updated["pension"] + global_vars_updated["investment"] + global_vars_updated["purchase"] 

    
    global_vars_updated["bank_account"] = income - expenses

    return global_vars_updated



def next_question(selected_option, global_variables):

    o_return = []
    q_return = {}
    target = selected_option["target"]
    
    for Q in questions["nodes"]:
        if Q["id"] == target:
            q_return = Q
            break
    
    for option in questions["edges"]:
        if option["source"] == Q["id"]:
            o_return.append(option)   


    response = {"question" : q_return, "options" : o_return, "state" : global_variables}
    return response 
