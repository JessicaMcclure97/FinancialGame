import {Modal, Frame} from '@react95/core'
import {Computer} from '@react95/icons'
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import styled from 'styled-components';


function QuestionPannel() {
    const [question, setQuestion] = useState('Test Question right here');

    /*
    * Get current question from server
    */
    useEffect(() => {
    axios.get('http://localhost:8000/hello-world/')
        .then(response => {
        setQuestion(response.data.message);
        })
        .catch(error => {
        console.log(error);
        });
    })

    const StyledModal = styled(Modal)`
        position: fixed;
        top: 10%;
        left: calc(50% - 15vw); /* Adjust the offset as needed */
        transform: translateY(-50%);
        width: 30vw;
        height: 50vh;
        // Other modal styles
        `;


    return(
        <>
        <StyledModal 
            
            icon={<Computer variant="16x16_4" />} 
            title="Question" 
        >

            <Frame bg="white" boxShadow="in" h="100%" w="100%" padding="0px 5px">
                {question}
            </Frame>
            
        </StyledModal>
        </>    

    );
        
};
export default QuestionPannel;