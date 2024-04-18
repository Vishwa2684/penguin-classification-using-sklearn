import React,{useState} from 'react'
import axios from 'axios'
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

export default function Estimator() {
    const [data, setData] = useState(null);
    const [postData,setPostData]=useState({
      flipperLength: null,
      culmenLength: null,
      culmenDepth: null,
      bodyMass: null,
      gender:null,
      island:null
    })
    //axios has no such method as json()
    const [output,setOutput]=useState(null)
    const sendData = async () => {
      try {
        if (Object.values(postData).some(value => value === null)) {
            toast.error('Fill all the fields'); // Display toast notification
            console.log(`fill all fields`)
            return; // Stop the function if any field is null
        }
        const response = await axios.post('http://localhost:8080/model',postData)
        if (response.status===200) {
          const jsonData = await response.data.predictions;
          setOutput(jsonData);
          console.log(response)
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
    console.log(output)
    
    return (
      <div>
  
            <ToastContainer/>
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
        {output!==null?<center><div>The penguin can be: {output}</div></center>:null}
        
      </div>
    );
}

