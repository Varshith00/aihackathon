import React, { useState } from "react";
import "./styles.css";

function App() {
  const [prompt, setPrompt] = useState("");
  const [answer, setAnswer] = useState("");

  const handleGenerate = async () => {
    try {
      const response = await fetch("http://localhost:8000/generate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt }),
      });
  
      const data = await response.json();
      setAnswer(data.answer);
    } catch (error) {
      setAnswer("Error contacting backend: " + error.message);
    }
  };

  
  return (
    <div className="container">
      <div className="header">Hello</div>
      <div className="subHeader">
        <span>How can</span> I assist you today?
      </div>
      <div className="promptBox">
        <input
          type="text"
          placeholder="Enter a prompt..."
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleGenerate()}
        />
        <button onClick={handleGenerate}>Generate</button>
      </div>
      <div className="answerBox">{answer}</div>
      <div className="footer">Powered by groq</div>
    </div>
  );
}

export default App;