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
   const [showIncomeAndExpense, setIncomeAndExpense] = useState(true)
   const [showBankBalance, setBankBalance] = useState(false)

    var data = [
        {
             x: [1, 2, 3, 4],
             y: [0, 2, 3, 5],
             fill: 'tozeroy',
             type: 'scatter',
             name: 'Vendor'
           },
           {
             x: [1, 2, 3, 4],
             y: [3, 5, 1, 7],
             fill: 'tonexty',
             type: 'scatter',
             name: 'Provider'
           }
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

    }

    const showBankGraph = () => {
        setIncomeAndExpense(false)
        setBankBalance(true)

    }

    return(
        <>
        <StyledModal1 buttons={[{
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
            {showIncomeAndExpense && <Plot 
                data={data}
                layout={ {title: 'Income and Expenses over A Number of Months'} }
                config={{responsive:true}}
            />}

            {showBankBalance && <Plot 
                data={data}
                layout={ {title: 'Bank Balance over A Number of Months'} }
                config={{responsive:true}}
            />}

        </StyledModal1>
        </>    

    );
        
};
export default GraphPannel;