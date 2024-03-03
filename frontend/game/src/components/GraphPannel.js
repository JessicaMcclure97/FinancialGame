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

   const [showIncomeAndExpense, setIncomeAndExpense] = useState(false)
   const [showBankBalance, setBankBalance] = useState(false) // UNSURE BUDGET PI CHART EQUIVALENT
   const [showBudget, setBudget] = useState(false)
   const [incomeOverTime, setIncomeOverTime] = useState([0])


   useEffect(() => {
    const income = state.salary+state.returns
    
    setIncomeAndExpense(incomeOverTime.concat(income)); // Concatenate and update state
    

    console.log("INCOME OVER TIME")
    console.log(incomeOverTime)
   },[state]);

   var dataIncomeVsExpenses = [
    {
         x: [Array.from({ length: incomeOverTime.length+1 }, (_, i) => i + 1)], // months
         y: [incomeOverTime], // income = salary + returns
         type: 'scatter',
         name: 'Income',
         line: {color: '#4daf4a'},
         marker: { size: 9 } 
       },
       {
         x: [Array.from({length: incomeOverTime.length }, (_, i) => i + 1)], // months
         y: [incomeOverTime], // expenses = transport + rent + food + tax + savings + extras + pension + purchase
         type: 'scatter',
         name: 'Expenses',
         line: {color: '#e41a1c'},
         marker: { symbol: 'x', size: 9, line: {color: '#e41a1c'} }
       }
    ];
    var dataBankBalance = [
        {
            x: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], // months
            y: [612, 647, 621, 633, 625, 654, 602, 629, 645, 603, 616, 618, 658, 610, 631, 611, 650, 622, 640, 627, 614, 639, 608, 655], // income - expenses
            type: 'scatter',
            name: 'Balance',
            line: {color: '#377eb8'},
            marker: { size: 9 }
        }
    ];
    var dataBudget = [
        {
        values: [20,30,50],//[(state.rent+state.transport+state.food+state.tax),(state.savings+state.pension),(state.extras)], //state.rent+state.transport+state.food+state.tax, state.savings+state.pension, state.extras],
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

    const showBudgetChart = () => {
        setIncomeAndExpense(false)
        setBankBalance(false)
        setBudget(true)
    }

    return(
        <>
        <StyledModal1 buttons={[{
                value: 'Income and Expenses Overview',
                onClick: () => showIncomeGraph()
            }, {
                value: 'Bank Balance Overview',
                onClick: () => showBankGraph()
            }, {
                value: 'Budget Overview',
                onClick: () => showBudgetChart()

            }]} menu={[{
                name: 'File',
            }]}
            
            icon={<Computer variant="16x16_4" />} 
            title="Graphic Reports" 
        >   
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

            {showBudget && <Plot 
                data={dataBudget}
                layout={ {title: 'Monthly Budget'} }
                config={{responsive:true}}
            />}

        </StyledModal1>
        </>    

    );
        
};
export default GraphPannel;