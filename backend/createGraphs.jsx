// General plot
<Plot
      data={[
        {
          x: [1, 2, 3],
          y: [2, 6, 3],
          type: 'scatter',
          mode: 'lines+markers',
          marker: {color: 'red'},
        },
        {type: 'bar', x: [1, 2, 3], y: [2, 5, 3]},
      ]}
      layout={ {
            width: 320, 
            height: 240, 
            title: 'A Fancy Plot',
            legend: {x: 0, y: 1.0} // Manually position the legend at the top-left corner
      } } />

const IncomeVsExpenses = (props) =>{
  var data = [
    {
         x: [1, 2, 3, 4], // months
         y: [0, 2, 3, 5], // income = salary + returns
         type: 'scatter',
         name: 'Income',
         line: {color: '#4daf4a'} 
       },
       {
         x: [1, 2, 3, 4], // months
         y: [3, 5, 1, 7], // expenses = transport + rent + food + tax + savings + extras + pension + investment + purchase
         type: 'scatter',
         name: 'Expenses',
         line: {color: '##e41a1c'},
         marker: { symbol: 'x', size: 10, line: {width: 2, color: '#e41a1c'} }
       }
  ];
    return(
       <Plot
       data={data}
       layout={ {width: 500, height: 500, title: 'Area Chart'} } />
    )
}

const BankBalance = (props) =>{
  var data = [
    {
         x: [1, 2, 3, 4], // months
         y: [0, 2, 3, 5], // income - expenses
         type: 'scatter',
         name: 'Balance',
         line: {color: '#377eb8'} 
       }
  ];
    return(
       <Plot
       data={data}
       layout={ {width: 500, height: 500, title: 'Area Chart'} } />
    )
}
