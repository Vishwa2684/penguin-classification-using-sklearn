// import React from 'react'
// import { useState,useEffect } from 'react'
// function App() {
//   const [data,setData]=useState({})
 
//   const getData=async()=>{
//     try{
//       const response = await fetch('http://localhost:8080/data')
//     if(response.ok){
//       let jsonData=await response.json()
//       console.log(jsonData)
//       setData(jsonData)
//     }else{
//       console.log()
//     }
//     }catch(err){
//       console.log(err.message)
//     }
    
//   }

//   console.log(data.data)
//   return (
//     <div>
//     <button onClick={getData}>Get data</button>

//       {/* {(data!==null)?(data.data.map(elem=><p>{elem}</p>)):<p>No data available</p>} */}
//     </div>
//   )
// }

// export default App

import React, { useState } from 'react';

function App() {
  const [data, setData] = useState(null);

  const getData = async () => {
    try {
      const response = await fetch('http://localhost:8080/data');
      if (response.ok) {
        const jsonData = await response.json();
        setData(jsonData);
      } else {
        console.log('Response not OK');
      }
    } catch (err) {
      console.error('Error fetching data:', err.message);
    }
  };

  return (
    <div>
      <button onClick={getData}>Get data</button>
      {data !== null ? (
        <ul>
          {data.data.map((elem) => (
            <li >{elem}</li>
          ))}
        </ul>
      ) : (
        <p>No data available</p>
      )}
    </div>
  );
}

export default App;