import {Modal, Button} from '@react95/core'
import {Computer} from '@react95/icons'
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import styled from 'styled-components';


function OptionsPannel({options}) {
    const [chosenOption, setChosenOptions] = useState({});


    const StyledModal = styled(Modal)`
    position: fixed;
    top: 65%;
    left: calc(50% - 15vw); /* Adjust the offset as needed */
    transform: translateY(+50%);
    width: 30vw;
    height: 25vh;
    // Other modal styles
    `;

    const StyledButton = styled(Button)`
    width: 100%; /* Set width to 100% of the modal content area */
    margin-top: 5px; /* Add some margin for spacing */
    `;

    const optionClicked = (element) =>  {
        setChosenOptions(element)
    }



    return(
        <>
        <StyledModal  
            icon={<Computer variant="16x16_4" />} 
            title="Options" 
        >
            {options.map(element => (
                <StyledButton key={element} onClick={(element) => optionClicked(element)}>
                    {element.text}
                </StyledButton>
            ))}
            
        </StyledModal>
            
        </>
    );
        
};
export default OptionsPannel;