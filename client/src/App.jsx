import React, { useState } from 'react';
import axios from'axios'
function App() {
  const [data, setData] = useState(null);
  const [postData,setPostData]=useState({
    flipperLength: '',
    culmenLength: '',
    culmenDepth: '',
    bodyMass: '',
    gender:'',
    island:''
  })
  const [output,setOutput]=useState(null)
  const sendData = async () => {
    try {
      const response = await axios.post('http://localhost:8080/model',{
        postData
      })
      if (response.ok) {
        const jsonData = await response.json();
        setOutput(jsonData);
      } else {
        console.log('Response not OK');
      }
    } catch (err) {
      console.error('Error fetching data:', err.message);
    }
  };

  const handleChange = (e)=>{
    const {name,value} =e.target
    setPostData(prevData=>({
      ...prevData,
      [name]:value

    }))
  }

  console.log(postData)
  
  return (
    <div>


        <h1>Penguin prediction model based on</h1>
        <h4>Flipper length (mm)</h4>
        <input type="text" name='flipperLength'  onChange={handleChange} />
        <h4>Culmen length (mm)</h4>
        <input type="text" name='culmenLength' onChange={handleChange} />
        <h4>Culmen depth (mm)</h4>
        <input type="text" name='culmenDepth' onChange={handleChange} />
        <h4>Body mass (g)</h4>
        <input type="text" name='bodyMass' onChange={handleChange} /><br />
        <select name="gender" id="genders" onChange={handleChange}>
          <option value="0">Male</option>
          <option value="1">Female</option>
        </select><br />
        <select name="island" id="islands" onChange={handleChange}>
            <option value='0'>Torgersen</option>
            <option value="1">Biscoe</option>
            <option value="2">Dream</option>
        </select><br />
        <button onClick={sendData}>Predict</button>

      
    </div>
  );
}

export default App;