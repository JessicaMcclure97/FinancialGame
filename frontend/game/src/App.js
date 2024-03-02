import './App.css';
import React, { useState, useEffect } from 'react';
import axios from 'axios';

import HelloWorld from './helloWorls'

//Layout 
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

// React95 
import { GlobalStyle, ThemeProvider } from '@react95/core'
import { createGlobalStyle } from 'styled-components'

//Components 
import TaskBar from './components/Taskbar'
import QuestionPannel from './components/QuestionPannel';
import OptionsPannel from './components/OptionsPannel';
import AboutPannel from './components/AboutPannel';
import { background, backgroundColor } from '@xstyled/styled-components';
import GraphPannel from './components/GraphPannel';

const CustomGlobalStyle = createGlobalStyle`
  body {
    user-select: none;

    a {
      color: ${(props) => props.theme.colors.black};
    }
    ul a {
      text-decoration: none;
    }
  }
`


//HomePage 
function App() {
  const [currentQuestion, setQuestion] = useState({id: 0, text:"This is a test question"});
  const [options, setOptions] = useState([]);
  const [chosenOption, setChosenOption] = useState(null)
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
    amount_invested: 0
  })

  /*
  API to get question everytime question is chosen 
  */
  useEffect(() => {
    const fetchQuestion = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/getQuestion',{
          params: {
            currentQuestion: currentQuestion.id,
            chosenOption: JSON.stringify(chosenOption),
            state: JSON.stringify(state), 
          }
        }); 
        
        //Await response for next Question
        const data = await response.data;
        console.log(data)
        setQuestion({id: data.question.id, text: data.question.question}); // Update state with the fetched question
        setOptions(data.options);
        setState((data.state));
      } catch (error) {
        console.error('Error fetching question:', error);
        // Handle errors appropriately, e.g., display an error message to the user
      }
    };

    fetchQuestion();
  }, [chosenOption]);

  const optionChosen = (option) =>{
    console.log("CHOSEN OPTION")
    console.log(option)
    setChosenOption(option)
  }

  return (
    <div className="App">
       <ThemeProvider
        breakpoints={['xxxl', 'xxl', 'xl', 'lg', 'md', 'sm', 'xs', 'xxs']}
       >
        <GlobalStyle />
        <CustomGlobalStyle />
        <h1 style={{"font-size": "2vw"}}> Level Up Your Finances </h1>
        <QuestionPannel question={currentQuestion.text}/>
        <OptionsPannel options={options} chosen={(e) => optionChosen(e)} />
        <AboutPannel state={state}/>
        <GraphPannel state={state}/>
        <TaskBar />
        </ThemeProvider>

     
    </div>

  );
}

export default App;
