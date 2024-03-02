import {Modal, Frame, ProgressBar} from '@react95/core'
import {Computer} from '@react95/icons'
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import styled from 'styled-components';
import PropTypes from 'prop-types';

function AboutPannel({state}) {
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

    const StyledModal = styled(Modal)`
        position: fixed;
        top: 10%;
        left: calc(10%); /* Adjust the offset as needed */
        transform: translateY(-50%);
        width: 20vw;
        height: 80vh;
        // Other modal styles
        `;


    return(
        <>
        <StyledModal 
            
            icon={<Computer variant="16x16_4" />} 
            title="About" 
        >

            <Frame bg="white" boxShadow="in" h="100%" w="100%" padding="0px 5px">
                <h2>
                    Current Age: {state.age}
                </h2>
                <h3>
                    Wellbeing
                </h3>
                <ProgressBar width={"15vw"} percent={state.wellbeing} />
                <h2>
                    Total Money: £{state.bank_account+state.savings}
                </h2>
                <h3>
                    Current Account: £{state.bank_account}
                    <br/>
                    Savings Account: £{state.savings}
                </h3>
            </Frame>
            
        </StyledModal>
        </>    

    );
        
};
export default AboutPannel;