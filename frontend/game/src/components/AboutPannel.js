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
        purchase: 0,
        amount_saved: 0,
        amount_invested: 0,
        holidays: 0,
        going_out: 0,
        hobbies: 0
    });
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
                    Health and Wellbeing
                </h2>
                <h3>
                    Wellbeing: <ProgressBar width={"15vw"} percent={state.wellbeing} />
                </h3>
                <h1>
                    Financial Overview 
                </h1>
                <h4>
                    One off Purchases: £{state.purchase}
                </h4>
                <h2>
                    Available Income: £{state.bank_account}
                </h2>
                <h3>
                    Money Spent on Needs: £{state.transports+state.food+state.rent+state.tax}
                </h3>
                <h4>
                    Transport: £{state.transports}
                </h4>
                <h4>
                    Food: £{state.food}
                </h4>
                <h4>
                    Rent: £{state.rent} 
                </h4>
                <h4>
                    Tax: £{state.tax} 
                </h4>
                <h3>
                    Money Spent on Future: £{state.savings+state.pension+state.returns}
                </h3>
                <h4>
                    Savings: £{state.savings}
                </h4>
                <h4>
                    Pension: £{state.pension}
                </h4>
                <h4>
                    Investment Returns: £{state.returns}
                </h4>
                <h3>
                    Money Spent on Extras: £{state.holidays+state.going_out+state.hobbies} {/**split up into sections */}
                </h3>
                <h4>
                    Holidays: £{state.holidays} {/**split up into sections */}
                </h4>
                <h4>
                    Going out: £{state.going_out} {/**split up into sections */}
                </h4>
                <h4>
                    Hobbies: £{state.hobbies} {/**split up into sections */}
                </h4>

            </Frame>
            
        </StyledModal>
        </>    

    );
        
};
export default AboutPannel;