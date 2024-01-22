import React, { useEffect } from 'react';
import './App.css';

function App() {

  useEffect(()=>{
    fetchData()
  }, [])

  const [data, setData] = React.useState([{'temp': -1.0, 'time': '', 'date': ''}]);

  const fetchData = async () => {
    let response = await fetch('http://localhost:5000/api');
    let data = await response.json()
    setData(data)
    console.log(data);  
    
    setTimeout(fetchData, 60 * 1000);
  }

  return (
    <div className="App">
      <header className="App-header">        
        <span id="top">現在中央大學溫度</span>
        <p id="temp">
          {Math.floor(data[0].temp)}<span style={{fontSize:'0.7em'}}>.{Math.floor(data[0].temp*10%10)}</span>
          <span style={{fontSize:'0.35em'}}> ℃</span>
        </p>
        <span id="bottom">
          上次更新：{data[0].date} {data[0].time}<br />
          24 小時內最低：{Math.min(...data.map(item => item.temp))} 最高：{Math.max(...data.map(item => item.temp))}
        </span>
      {/* <span id="lbicon">🥶</span> */}
      </header>
    </div>
  );
}

export default App;
