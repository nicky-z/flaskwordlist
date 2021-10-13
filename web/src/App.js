import React from 'react';
import axios  from 'axios';
import './App.css';

function App() {
  const [words, setWords] = React.useState([]);
  const [newWord, setNewWord] = React.useState('')
  const [filter, setFilter] = React.useState('')

 React.useEffect(() => {
  async function fetchWords() {
    axios.get("/words").then(
      ({data}) => {
        //console.log(data);
        for(const wordId in data){
          for(const wordKey in data[wordId]){
            setWords(prevWords =>[...prevWords, data[wordId][wordKey]])
          }
        }
      }
    )
  }
  fetchWords();
 },[])


 function handleSubmit(event) {
   event.preventDefault();
  console.log('SUBMITTED!', newWord)
  if(newWord!== '') {
  axios.post("/words", {"word": newWord}).then(
    ({data})=>{
      console.log(data)
      window.location.reload()
    }
  )}
}


const listOfWords = words.map((word,idx) => <p key={idx}>{word}</p>);

//console.log(words)
  return (
    <div className="App">
      <span>Word List</span>
      <div className="list">
      {words.map((word,idx) => <p key={idx}>{word}</p>)}
      </div>
    <div className="form">
      <form>
        <input
          placeholder = "add word"
          onChange={(evt) =>{setNewWord(evt.target.value)}}
         />
         <button className="button" onClick={handleSubmit}> Add Word </button>
    </form>
    <form>
        <input
          placeholder = "filter for..."
          onChange={(evt) =>{setFilter(evt.target.value)}}
         />
         <button className="button" onClick={handleSubmit}> Filter </button>
    </form>
    </div>
    </div>
  );
}

export default App;
