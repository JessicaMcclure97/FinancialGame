import json

initial_variables = {
    "age": 10,
    "wellbeing": 100,
    "bank_account": 0,
    "salary": 0,
    "returns": 0,
    "transports": 0,
    "rent": 0,
    "food": 200,
    "tax": 0,
    "savings": 0,
    "extras": 0,
    "pension": 0,
    "investment": 0,
    "purchase": 0,
    "amount_saved" : 0,
    "amount_invested" : 0
}

selected_option = {}




def get_option(op_id):
    for option in questions["edges"]:
        if option["option_id"] == op_id:
            selected_option = option
            break
    return selected_option

def outcome(selected_option, global_vars):

    var_name = selected_option["variables"]
    amount = selected_option["amount"]
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
    target = selected_option["target"]
    
    for Q in questions["nodes"]:
        if Q["id"] == target:
            q_return = Q
            break
    
    for option in questions["edges"]:
        if option["source"] == Q["id"]:
            o_return.append(option)

    return {"question" : q_return, "options" : o_return, "state" : global_variables}

selected_option = get_option(37)

print(initial_variables)

global_var_updated = outcome(selected_option, initial_variables)

test = next_question(selected_option,global_var_updated)
print(test)