import {Modal, Button, ProgressBar} from '@react95/core'
import {Computer} from '@react95/icons'
import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import Plot from 'react-plotly.js';

function GraphPannel({state}) {
    /*
    const [state, setState] = useState({
        age: 10,
        wellbeing: 100,
        bank_account: 0,
        salary: 0,
        returns: 0,
        transports: 0,
        rent: 0,
        food: 150,
        tax: 0,
        savings: 0,
        extras: 0,
        pension: 0,
        investment: 0,
        purchase: 0
    })
    */

    const [showBudget, setBudget] = useState(true)
   const [showIncomeAndExpense, setIncomeAndExpense] = useState(false)
   const [showBankBalance, setBankBalance] = useState(false) // UNSURE BUDGET PI CHART EQUIVALENT
   const [incomeOverTime, setIncomeOverTime] = useState([])
   const [expensesOverTime, setExpensesOverTime] = useState([])
   const [needs, setNeeds] = useState(0);
   const [extras, setExtras] = useState(0);
   const [future, setFuture] = useState(0);


   useEffect(() => {
    const income = state.salary + state.returns
    setIncomeOverTime(prevIncome => [...prevIncome, income]); // Add new income to the array

    const expenses = state.transports+state.rent+state.food+state.tax+state.savings+state.holidays+state.going_out+state.hobbies+state.pension+state.purchase
    setExpensesOverTime(prevExpense => [...prevExpense, expenses]);

    const needs = state.rent+state.transports+state.food+state.tax
    const extras = state.holidays + state.hobbies + state.going_out
    const future = state.savings+state.pension
    setNeeds(needs);
    setExtras(extras);
    setFuture(future);
   },[state.salary, state.returns, state.transports, state.rent, state.food, state.tax, state.savings, state.holidays, state.going_out, state.hobbies, state.pension, state.purchase]); // Re-run effect whenever salary or returns change

   var dataIncomeVsExpenses = [
    {
         x: Array.from({ length: incomeOverTime.length+1 }, (_, i) => i + 1), // months
         y: incomeOverTime, // income = salary + returns
         type: 'scatter',
         name: 'Income',
         line: {color: '#4daf4a'},
         marker: { size: 9 } 
       },
       {
         x: Array.from({length: expensesOverTime.length }, (_, i) => i + 1), // months
         y: expensesOverTime, // expenses = transports + rent + food + tax + savings + extras + pension + purchase
         type: 'scatter',
         name: 'Expenses',
         line: {color: '#e41a1c'},
         marker: { symbol: 'x', size: 9, line: {color: '#e41a1c'} }
       }
    ];
    var dataBankBalance = [
        {
            x: Array.from({length: expensesOverTime.length }, (_, i) => i + 1), // months
            y: incomeOverTime - expensesOverTime, // income - expenses
            type: 'scatter',
            name: 'Balance',
            line: {color: '#377eb8'},
            marker: { size: 9 }
        }
    ];
    var dataBudget = [
        {
        values: [needs, future, extras], //state.rent+state.transport+state.food+state.tax, state.savings+state.pension, state.extras],
        labels: ["Needs", "Future", "Extras"],
        type: "pie",
        marker: {
            colors: ["#999999", "#984ea3", "#ff7f00"] // Specify custom colors for each section
        }
        },
    ];

    const StyledModal1 = styled(Modal)`
    position: fixed;
    top: 10%;
    right: calc(2%); /* Adjust the offset as needed */
    transform: translateY(-100%);
    width: 30vw;
    height: 60vh;
    // Other modal styles
    `;

    const showBudgetChart = () => {
        setIncomeAndExpense(false)
        setBankBalance(false)
        setBudget(true)
    }

    const showIncomeGraph = () => {
        setIncomeAndExpense(true)
        setBankBalance(false)
        setBudget(false)

    }

    const showBankGraph = () => {
        setIncomeAndExpense(false)
        setBankBalance(true)
        setBudget(false)

    }

    return(
        <>
        <StyledModal1 buttons={[{
                value: 'Budget Overview',
                onClick: () => showBudgetChart()
            }, {
                value: 'Income and Expenses Overview',
                onClick: () => showIncomeGraph()
            }, {
                value: 'Bank Balance Overview',
                onClick: () => showBankGraph()
            }]} menu={[{
                name: 'File',
            }]}
            
            icon={<Computer variant="16x16_4" />} 
            title="Graphic Reports" 
        >   
            {showBudget && <Plot 
                data={dataBudget}
                layout={ {title: 'Monthly Budget'} }
                config={{responsive:true}}
            />}

            {showIncomeAndExpense && <Plot 
                data={dataIncomeVsExpenses}
                layout={ {title: 'Income and Expenses over A Number of Months', legend: {x: 0, y: 1.0}} }
                config={{responsive:true}}
            />}

            {showBankBalance && <Plot 
                data={dataBankBalance}
                layout={ {title: 'Bank Balance over A Number of Months'} }
                config={{responsive:true}}
            />}


        </StyledModal1>
        </>    

    );
        
};
export default GraphPannel;