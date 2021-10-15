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
        console.log('onmount',data);
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

function handleFilter(event) {
  event.preventDefault();
 if(filter!== '') {
 console.log('FILTER', filter)
 axios.get("/words/filter", {params: {pattern: filter}}).then(
   ({data})=>{
     console.log('data from backend', data)
     for(const wordId in data){
      for(const wordKey in data[wordId]){
        let filteredWords = words.filter((word)=> word===data[wordId][wordKey]);
        setWords(filteredWords);
      }
    }
   }
 )}
}

  return (
    <div className="App">
      <div className= "flexbox-container">
        <div className = "flexbox-forms">
          <form>
            <input
              placeholder = "add word"
              onChange={(evt) =>{setNewWord(evt.target.value)}}
            />
            <button onClick={handleSubmit}> Add Word </button>
          </form>
          <form>
            <input
              placeholder = "filter for..."
              onChange={(evt) =>{setFilter(evt.target.value)}}
            />
            <button onClick={handleFilter}> Filter </button>
          </form>
        </div>
        <div className = "flexbox-word-list">
          <div className = "title">Word List</div>
          <div className="list">
            {words.map((word,idx) => <p key={idx}>{word}</p>)}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
