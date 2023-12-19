import axios from "axios";
function App() {
  const handleclick = async () => {
    axios
      .get("http://127.0.0.1:8000/get/2")
      .then((res) => {
        console.log(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <div>
      <h1>hello</h1>
      <button onClick={handleclick}>Get Data</button>
    </div>
  );
}

export default App;
